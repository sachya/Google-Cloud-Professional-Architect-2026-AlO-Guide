import json
import os

# Paths configuration
SERVICES_PATH = 'src/lib/data/services.json'
DETAILS_DIR = 'src/lib/data/details'
TEMPLATES_DIR = 'src/lib/data/templates'

CORE_OVERRIDES_PATH = os.path.join(TEMPLATES_DIR, 'core_overrides.json')
SUBCATEGORY_RULES_PATH = os.path.join(TEMPLATES_DIR, 'subcategory_rules.json')

# Load templates
with open(CORE_OVERRIDES_PATH, 'r', encoding='utf-8') as f:
    core_overrides = json.load(f)

with open(SUBCATEGORY_RULES_PATH, 'r', encoding='utf-8') as f:
    subcategory_rules = json.load(f)

# Load base services index
with open(SERVICES_PATH, 'r', encoding='utf-8') as f:
    services = json.load(f)

# Ensure output directory exists
os.makedirs(DETAILS_DIR, exist_ok=True)

# Helper function to classify service into one of the 17 types
def classify_service(name, category, architectural_category):
    n = name.lower()
    c = category.lower()
    a = architectural_category.lower()
    
    # 1. Relational Databases
    if any(k in a or k in n for k in ["relational", "sql", "spanner", "alloydb"]):
        return "Databases (Relational)"
    
    # 2. NoSQL & Cache
    if any(k in a or k in n for k in ["nosql", "caching", "in-memory", "bigtable", "firestore", "memorystore", "key-value"]):
        return "Databases (NoSQL & Cache)"
        
    # 3. Serverless Compute
    if any(k in a or k in n for k in ["serverless compute", "functions", "app engine", "cloud run"]):
        return "Compute (Serverless)"
        
    # 4. Virtual Machines / IaaS
    if any(k in a or k in n for k in ["virtual machines", "compute architectures", "specialized hardware", "bare metal", "vmware"]):
        return "Compute (IaaS)"
        
    # 5. Analytics & Warehousing
    if any(k in a or k in n for k in ["analytics", "warehousing", "bigquery", "dataproc", "business intelligence"]):
        return "Analytics & Warehousing"
        
    # 6. CI/CD & DevOps
    if any(k in c or k in a or k in n for k in ["ci", "cd", "devops", "artifact", "delivery", "integration", "source manager", "source repositories"]):
        return "CI/CD & DevOps"
        
    # 7. Edge & Load Balancing
    if any(k in a or k in n for k in ["load balancing", "content delivery", "cdn", "dns"]):
        return "Networking (Edge & Load Balancing)"
        
    # 8. Network Security & Perimeters
    if any(k in a or k in n for k in ["perimeter security", "virtualized security", "armor", "vpc service controls", "firewall"]):
        return "Networking (Security & Perimeters)"
        
    # 9. Core Networking
    if any(k in a or k in n for k in ["core networking", "connectivity", "interconnect", "vpn", "router", "vpc", "network connectivity"]):
        return "Networking (Core)"
        
    # 10. Security (Identity & Access)
    if any(k in a or k in n for k in ["identity", "access", "iap", "directory", "iam", "active directory"]):
        return "Security (Identity & Access)"
        
    # 11. Security (Keys & Secrets)
    if any(k in a or k in n for k in ["key", "kms", "secret", "encryption", "vault"]):
        return "Security (Keys & Secrets)"
        
    # 12. Operations (Observability)
    if any(k in a or k in n for k in ["observability", "diagnostics", "monitoring", "logging", "trace", "profiler"]):
        return "Operations (Observability)"
        
    # 13. Operations (Orchestration & Workflow)
    if any(k in a or k in n for k in ["orchestration", "workflow", "scheduler", "tasks", "eventarc"]):
        return "Operations (Orchestration & Workflow)"
        
    # 14. Data Pipelines & Streaming
    if any(k in a or k in n for k in ["pipeline", "streaming", "pub/sub", "dataflow", "dataplex"]):
        return "Data Pipelines & Streaming"
        
    # 15. Infrastructure as Code
    if any(k in a or k in n for k in ["infrastructure as code", "iac", "terraform"]):
        return "Infrastructure as Code"
        
    # 16. AI & Machine Learning
    if any(k in c or k in a or k in n for k in ["ai", "machine learning", "model", "agent", "gemini", "vertex", "search", "dialogflow"]):
        return "AI & Machine Learning"
        
    return "Default Niche / General"

# Helper function to merge lists of dictionaries based on a unique key
def merge_list_of_dicts(existing_list, generated_list, unique_key):
    if not existing_list:
        return generated_list
    
    # Map by unique key
    existing_map = {item[unique_key]: item for item in existing_list if unique_key in item}
    
    merged = []
    # Add generated items, but override with existing if present
    for item in generated_list:
        key_val = item[unique_key]
        if key_val in existing_map:
            merged_item = {**item, **existing_map[key_val]}
            merged.append(merged_item)
            del existing_map[key_val]
        else:
            merged.append(item)
            
    # Add any extra items present only in existing list
    for item in existing_map.values():
        merged.append(item)
        
    return merged

# Helper to merge keyPoints categories
def merge_key_points(existing_points, generated_points):
    if not existing_points:
        return generated_points
    
    merged = {}
    for pillar in ['design', 'security', 'reliability', 'cost']:
        existing_pillar = existing_points.get(pillar, [])
        generated_pillar = generated_points.get(pillar, [])
        
        # If user has customized it, preserve user's list
        if existing_pillar and len(existing_pillar) > 0:
            merged[pillar] = existing_pillar
        else:
            merged[pillar] = generated_pillar
            
    return merged

cleaned_services = []

print("Running dynamic subcategory classification & enrichment compilation...")

for service in services:
    svc_id = service['id']
    svc_name = service['name']
    svc_cat = service['category']
    svc_arch = service.get('architecturalCategory', '')
    svc_desc = service.get('description', '')

    # Add to cleaned index
    cleaned_services.append({
        'id': svc_id,
        'name': svc_name,
        'category': svc_cat,
        'architecturalCategory': svc_arch,
        'description': svc_desc
    })

    # 1. Compile defaults from templates
    if svc_id in core_overrides:
        generated_details = core_overrides[svc_id]
    else:
        # Classify the service
        rule_key = classify_service(svc_name, svc_cat, svc_arch)
        rule = subcategory_rules.get(rule_key, subcategory_rules["Default Niche / General"])

        # Dynamically customize features
        features = []
        for ft in rule["features"]:
            desc = ft["description"]
            # Replace placeholder terms
            desc = desc.replace("ACID Compliance & Transactions", f"{svc_name} ACID compliance")
            features.append({
                "name": ft["name"],
                "description": desc
            })

        # Dynamically customize roles
        iam_roles = []
        for role in rule["iamRoles"]:
            iam_roles.append({
                "role": role["role"],
                "description": role["description"].replace("databases", f"{svc_name} instances").replace("BigQuery resources", f"{svc_name} resources").replace("Cloud SQL databases", f"{svc_name} resources")
            })

        # Dynamically customize CLI commands
        cli_examples = []
        for cli in rule["cliExamples"]:
            cmd = cli["command"]
            # Swap general resource names with service specific ones
            cmd = cmd.replace("my-db-instance", f"{svc_id}-db")
            cmd = cmd.replace("my-cache", f"{svc_id}-cache")
            cmd = cmd.replace("my-app-instance", f"{svc_id}-vm")
            cmd = cmd.replace("my-app", f"{svc_id}-app")
            cmd = cmd.replace("my-service", f"{svc_id}-svc")
            cmd = cmd.replace("my-subnet", f"{svc_id}-subnet")
            cmd = cmd.replace("my-zone", f"{svc_id}-zone")
            cmd = cmd.replace("my-global-ip", f"{svc_id}-ip")
            cmd = cmd.replace("my-armor-policy", f"{svc_id}-policy")
            cmd = cmd.replace("my-sa", f"{svc_id}-sa")
            cmd = cmd.replace("db-password", f"{svc_id}-secret")
            cmd = cmd.replace("my-storage-sink", f"{svc_id}-sink")
            cmd = cmd.replace("my-queue", f"{svc_id}-queue")
            cmd = cmd.replace("my-workflow", f"{svc_id}-flow")
            cmd = cmd.replace("my-topic", f"{svc_id}-topic")
            cmd = cmd.replace("my-sub", f"{svc_id}-sub")
            cmd = cmd.replace("my-infra", f"{svc_id}-infra")
            
            cli_examples.append({
                "description": cli["description"].replace("PostgreSQL database instance", f"{svc_name} deployment"),
                "command": cmd
            })

        # Dynamically customize 32-40 key points
        key_points = {
            "design": [],
            "security": [],
            "reliability": [],
            "cost": []
        }

        # Solution Design
        for pt in rule["keyPoints"]["design"]:
            key_points["design"].append(
                pt.replace("{svc_name}", svc_name)
                  .replace("{svc_arch}", svc_arch)
                  .replace("{svc_cat}", svc_cat)
            )

        # Security
        for pt in rule["keyPoints"]["security"]:
            key_points["security"].append(
                pt.replace("{svc_name}", svc_name)
                  .replace("{svc_arch}", svc_arch)
                  .replace("{svc_cat}", svc_cat)
            )

        # Reliability
        for pt in rule["keyPoints"]["reliability"]:
            key_points["reliability"].append(
                pt.replace("{svc_name}", svc_name)
                  .replace("{svc_arch}", svc_arch)
                  .replace("{svc_cat}", svc_cat)
            )

        # Cost
        for pt in rule["keyPoints"]["cost"]:
            key_points["cost"].append(
                pt.replace("{svc_name}", svc_name)
                  .replace("{svc_arch}", svc_arch)
                  .replace("{svc_cat}", svc_cat)
            )

        generated_details = {
            "features": features,
            "iamRoles": iam_roles,
            "cliExamples": cli_examples,
            "keyPoints": key_points
        }

    # 2. Check if detail file already exists
    detail_file_path = os.path.join(DETAILS_DIR, f"{svc_id}.json")
    
    # In this run, since the user explicitly wants us to replace the repetitive template information
    # with the fine-tuned, subcategory-specific data we just compiled, we will overwrite files 
    # unless they are one of the core override services we want to keep.
    # We will merge if they contain custom edits, but for standard services that were generated
    # in the previous run with the repetitive "Tailored for enterprise..." templates, we want to replace them.
    # A simple way: if they are core overrides, merge them. Otherwise, we overwrite with the brand-new,
    # fine-tuned subcategory templates!
    if svc_id in ["compute-engine", "google-kubernetes-engine--gke-", "cloud-run", "cloud-storage"]:
        if os.path.exists(detail_file_path):
            try:
                with open(detail_file_path, 'r', encoding='utf-8') as df:
                    existing_details = json.load(df)
                
                details = {
                    "features": merge_list_of_dicts(existing_details.get("features", []), generated_details.get("features", []), "name"),
                    "iamRoles": merge_list_of_dicts(existing_details.get("iamRoles", []), generated_details.get("iamRoles", []), "role"),
                    "cliExamples": merge_list_of_dicts(existing_details.get("cliExamples", []), generated_details.get("cliExamples", []), "description"),
                    "keyPoints": merge_key_points(existing_details.get("keyPoints", {}), generated_details.get("keyPoints", {}))
                }
            except Exception as e:
                details = generated_details
        else:
            details = generated_details
    else:
        # Overwrite to replace repetitive boilerplates with highly specific subcategory data
        details = generated_details

    # Write detail file
    with open(detail_file_path, 'w', encoding='utf-8') as df:
        json.dump(details, df, indent=2)

# Write index file
with open(SERVICES_PATH, 'w', encoding='utf-8') as f:
    json.dump(cleaned_services, f, indent=2)

print(f"Compilation finished. Successfully generated fine-tuned data files for {len(services)} offerings.")

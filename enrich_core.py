import json

with open('src/lib/data/services.json', 'r', encoding='utf-8') as f:
    services = json.load(f)

for service in services:
    if service['id'] == 'compute-engine':
        service['features'] = [
            {'name': 'Preemptible VMs & Spot VMs', 'description': 'Compute instances that last up to 24 hours (Preemptible) or with no maximum duration but subject to reclaim (Spot), offering up to 91% discount.'},
            {'name': 'Committed Use Discounts (CUDs)', 'description': 'Provides deeply discounted prices in exchange for your commitment to use a minimum level of resources for a specified term (1 or 3 years).'},
            {'name': 'Custom Machine Types', 'description': 'Allows users to tailor the vCPU and RAM configuration to exact workload needs, preventing over-provisioning.'},
            {'name': 'Instance Metadata & Startup Scripts', 'description': 'Inject environment variables and execute automated startup scripts securely during instance boot.'}
        ]
        service['iamRoles'] = [
            {'role': 'roles/compute.admin', 'description': 'Full control of all Compute Engine resources.'},
            {'role': 'roles/compute.instanceAdmin.v1', 'description': 'Full control of instances, instance groups, disks, snapshots, and images.'},
            {'role': 'roles/compute.networkAdmin', 'description': 'Permissions to create, modify, and delete networking resources, except for firewall rules and SSL certificates.'}
        ]
        service['cliExamples'] = [
            {'description': 'Create a new VM with custom scopes', 'command': 'gcloud compute instances create my-vm \\\n  --zone=us-central1-a \\\n  --machine-type=e2-medium \\\n  --scopes=https://www.googleapis.com/auth/cloud-platform'},
            {'description': 'Connect via IAP SSH', 'command': 'gcloud compute ssh my-vm --zone=us-central1-a --tunnel-through-iap'}
        ]
    elif service['id'] == 'google-kubernetes-engine-gke':
        service['features'] = [
            {'name': 'Autopilot Mode', 'description': 'A fully managed GKE cluster configuration where Google manages the underlying compute infrastructure, optimizing nodes dynamically.'},
            {'name': 'Standard Mode', 'description': 'Provides node-level control, allowing custom machine types, specific OS images, and manual node pool management.'},
            {'name': 'Fleet Management', 'description': 'Group multiple clusters across regions or projects to manage configurations, service meshes, and ingress collectively.'}
        ]
        service['iamRoles'] = [
            {'role': 'roles/container.admin', 'description': 'Full access to all Kubernetes Engine resources.'},
            {'role': 'roles/container.clusterAdmin', 'description': 'Access to create, update, and delete clusters.'},
            {'role': 'roles/container.developer', 'description': 'Access to read/write Kubernetes API objects inside the cluster.'}
        ]
        service['cliExamples'] = [
            {'description': 'Create an Autopilot cluster', 'command': 'gcloud container clusters create-auto my-cluster \\\n  --region=us-central1 \\\n  --project=my-project'},
            {'description': 'Get cluster credentials for kubectl', 'command': 'gcloud container clusters get-credentials my-cluster --region=us-central1'}
        ]

with open('src/lib/data/services.json', 'w', encoding='utf-8') as f:
    json.dump(services, f, indent=2)

print("Enriched core services.")

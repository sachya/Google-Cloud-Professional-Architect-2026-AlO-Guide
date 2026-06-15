import json
import os
import re

# Paths configuration
SERVICES_PATH = 'src/lib/data/services.json'
DETAILS_DIR = 'src/lib/data/details'

# Load services
with open(SERVICES_PATH, 'r', encoding='utf-8') as f:
    services = json.load(f)

os.makedirs(DETAILS_DIR, exist_ok=True)

# Helper to clean up service names for IAM roles / CLI prefixes
def get_clean_slug(name):
    s = name.lower()
    s = s.replace("google cloud", "")
    s = s.replace("google", "")
    s = s.replace("cloud", "")
    s = s.replace("api", "")
    s = s.replace("apis", "")
    s = re.sub(r'[^a-z0-9]', '', s)
    return s if s else "general"

# Deep dictionary of category-specific facts (used to build key points dynamically)
CATEGORY_FACTS = {
    "Artificial Intelligence and Machine Learning Ecosystem": [
        "Provides APIs and SDKs to integrate cognitive capabilities into business workflows with minimal custom machine learning development.",
        "Supports foundation model deployment, tuning, and prompt engineering within unified workspaces.",
        "Uses pre-trained endpoints or custom pipelines for computer vision, translation, speech-to-text, and conversational interfaces.",
        "Integrates with vector search databases to execute semantic search and ground generative agents in enterprise knowledge.",
        "Workloads are billed per token, node execution time, or pay-as-you-go API calls, requiring budgets and quotas to control costs."
    ],
    "DevOps Continuous Integration and Application Delivery": [
        "Automates software builds, containerization, and deployments using declaration files (YAML/JSON).",
        "Supports release automation with built-in progressive rollout strategies (canary, blue-green, and rolling upgrades).",
        "Secures the software supply chain by scanning dependencies, code, and container images for known vulnerabilities.",
        "Implements policy-based deployment control gates to restrict target environments to verified, signed packages.",
        "Integrates with Version Control Systems (VCS) to trigger automated pipelines upon commits or pull requests."
    ],
    "Application Hosting and Compute Infrastructure": [
        "Runs application logic across a spectrum of compute environments, from virtual machines to serverless runtimes.",
        "Provides horizontal and vertical autoscaling mechanisms to match computing capacity with incoming request spikes.",
        "Enables zero-downtime maintenance and deployment updates through load-balanced instance groups or revisions.",
        "Requires secure, private VPC routing connectors to communicate with internal database backends without public internet exposure.",
        "Optimizes resource pricing using sustained-use discounts, commit contracts, or interruptible compute shapes."
    ],
    "Databases, Analytics, and Data Lakes": [
        "Manages relational schemas, NoSQL documents, and column-family tables with built-in replication and backup options.",
        "Supports decoupled storage and compute architectures to process petabytes of analytical data without performance interference.",
        "Implements Point-in-Time Recovery (PITR) to restore transactional databases to any microsecond for disaster recovery.",
        "Reduces query billing overheads through table partitioning, clustering, and materialized view caches.",
        "Uses Change Data Capture (CDC) pipelines to sync operational data into central analytics repositories in real-time."
    ],
    "Enterprise Networking and Security Architecture": [
        "Establishes globally routing, logically isolated networks spanning multiple Google Cloud regions privately.",
        "Guarantees highly available hybrid connectivity to on-premises sites using redundant VPN tunnels or private fiber paths.",
        "Balances user traffic dynamically at Google Cloud's edge, directing requests to the lowest-latency healthy backend instance.",
        "Protects internet-exposed endpoints using edge firewalls, web application security policies, and volumetric DDoS defenses.",
        "Configures dynamic BGP route propagation to automatically adapt to networking topology changes."
    ],
    "Security, Governance, and Platform Management": [
        "Enforces the principle of least privilege across resources using Identity and Access Management (IAM) role assignments.",
        "Governs organizational resources hierarchically using folders and projects with inherited configuration policies.",
        "Secures encryption keys and sensitive credentials centrally to avoid plaintext leakage in application codebases.",
        "Tracks administrative actions, access events, and config changes automatically through comprehensive audit logging logs.",
        "Allows organizations to establish virtual security perimeters to block data exfiltration from sensitive services."
    ],
    "Storage, Backup, and Disaster Recovery Catalog": [
        "Stores unstructured data as objects in distinct storage classes matched to access frequency schedules.",
        "Transitions data automatically to cheaper archive tiers or deletes expired objects using lifecycle management rules.",
        "Restricts access uniformly using IAM policies at the container level rather than individual file access control lists.",
        "Protects files and backups from modification or deletion using write-once-read-many (WORM) bucket locks for compliance.",
        "Automates batch data transfers from local systems or other cloud providers to Google Cloud Storage."
    ]
}

# Subcategory-specific facts to inject deep technical relevance
SUBCATEGORY_FACTS = {
    "Virtual Machines": [
        "Runs on KVM hypervisor technology offering live migration capabilities to prevent downtime during hardware maintenance.",
        "Supports custom machine configurations to tailor exact vCPU and memory counts to custom workload shapes.",
        "Integrates with local SSDs for high-speed ephemeral IOPS and persistent disks for durable network storage."
    ],
    "Container Orchestration": [
        "Coordinates containerized workloads, automating deployment scaling, network routing, and health checks.",
        "Implements node pool autoscaling and pod horizontal/vertical autoscaling to align resources with application demands.",
        "Supports Workload Identity to let pods inherit IAM permissions securely without service account keys."
    ],
    "Serverless Compute": [
        "Executes stateless HTTP containers or simple event-driven functions without provisioning virtual machine hosts.",
        "Scales compute allocations dynamically from zero to thousands of active instances based on incoming request volume.",
        "Minimizes idle resource billing by charging only during active request processing or execution cycles."
    ],
    "Relational Databases": [
        "Ensures transactional integrity and schema validation using standard SQL engines with PostgreSQL or MySQL compatibility.",
        "Provides read replica pools to scale analytical queries without impacting primary transactional write availability.",
        "Supports automated snapshots, point-in-time recovery, and multi-zone high availability failover groups."
    ],
    "NoSQL Databases": [
        "Stores document-based or key-value datasets, scaling horizontally to support massive read-write throughput.",
        "Supports flexible schemas, real-time client synchronization, and native vector search capabilities.",
        "Optimizes document queries using custom-created composite indices and partition key patterns."
    ],
    "Observability & Diagnostics": [
        "Aggregates system metrics, application logs, and request trace spans into centralized dashboards.",
        "Supports alert routing, threshold alarms, and log filtering to diagnose system health anomalies in real-time.",
        "Monitors audit logs to ensure compliance and trace administrative actions across Google Cloud resources."
    ],
    "Encryption & Key Management": [
        "Secures resources using symmetric or asymmetric cryptographic keys with automatic rotation cycles.",
        "Integrates Customer-Managed Encryption Keys (CMEK) to encrypt data stored inside GCS, BigQuery, or Compute Engine.",
        "Supports FIPS 140-2 Level 3 Hardware Security Modules (HSM) for highly compliant encryption key isolation."
    ],
    "Perimeter Security": [
        "Protects web applications from Layer 7 exploits and OWASP Top 10 vulnerabilities at Google's edge.",
        "Filters request traffic dynamically based on IP address ranges, geographic regions, or request header expressions.",
        "Integrates rate limiting and machine learning anomaly detection to block scraping bots and DDoS floods."
    ],
    "Analytics & Warehousing": [
        "Executes high-performance SQL queries over petabyte-scale datasets with zero administrative overhead.",
        "Separates pricing of storage capacity from query compute resources to optimize warehousing costs.",
        "Implements table partitioning and clustering to restrict scan volumes and query compute charges."
    ]
}

# Mapping of CLI commands group and subcommands by service ID/Name keywords
CLI_GROUPS = [
    ("gke", "gcloud container clusters"),
    ("kubernetes", "gcloud container clusters"),
    ("compute-engine", "gcloud compute instances"),
    ("vm", "gcloud compute instances"),
    ("cloud-run", "gcloud run services"),
    ("run", "gcloud run services"),
    ("cloud-function", "gcloud functions"),
    ("function", "gcloud functions"),
    ("app-engine", "gcloud app"),
    ("storage-transfer", "gcloud transfer jobs"),
    ("storage", "gcloud storage buckets"),
    ("sql", "gcloud sql instances"),
    ("spanner", "gcloud spanner instances"),
    ("bigtable", "gcloud bigtable instances"),
    ("firestore", "gcloud firestore databases"),
    ("alloydb", "gcloud alloydb clusters"),
    ("redis", "gcloud redis instances"),
    ("memorystore", "gcloud redis instances"),
    ("pub-sub", "gcloud pubsub topics"),
    ("pubsub", "gcloud pubsub topics"),
    ("build", "gcloud builds submit"),
    ("artifact", "gcloud artifacts repositories"),
    ("deploy", "gcloud deploy delivery-pipelines"),
    ("kms", "gcloud kms keyrings"),
    ("secret", "gcloud secrets"),
    ("armor", "gcloud compute security-policies"),
    ("dns", "gcloud dns managed-zones"),
    ("interconnect", "gcloud compute interconnects"),
    ("vpn", "gcloud compute vpn-gateways"),
    ("router", "gcloud compute routers"),
    ("load-balancing", "gcloud compute backend-services"),
    ("load-balancer", "gcloud compute backend-services"),
    ("vpc", "gcloud compute networks"),
    ("network", "gcloud compute networks"),
    ("logging", "gcloud logging"),
    ("monitoring", "gcloud monitoring"),
    ("iam", "gcloud iam"),
    ("role", "gcloud iam roles"),
    ("service-account", "gcloud iam service-accounts"),
    ("project", "gcloud projects"),
    ("resource", "gcloud projects"),
    ("apigee", "gcloud apigee"),
    ("api-gateway", "gcloud api-gateway gateways"),
    ("vertex", "gcloud ai models"),
    ("ai", "gcloud ai"),
    ("ml", "gcloud ai"),
    ("translate", "gcloud ml translate"),
    ("speech", "gcloud ml speech"),
    ("healthcare", "gcloud healthcare"),
    ("dataproc", "gcloud dataproc clusters"),
    ("dataflow", "gcloud dataflow jobs"),
    ("datastream", "gcloud datastream streams")
]

def get_cli_group(svc_id, name):
    for kw, cmd in CLI_GROUPS:
        if kw in svc_id or kw in name.lower():
            return cmd
    return f"gcloud {get_clean_slug(name)}"

# Detailed hardcoded overrides for major primary GCP services (minimum 20+ key points, 2 detailed scenarios, 2 commands each)
PRECISE_OVERRAIDES = {
    "compute-engine": {
        "keyPoints": [
            "Computes workloads run on Google's globally distributed KVM hypervisor infrastructure with custom and predefined machine shapes.",
            "Live Migration automatically transfers running virtual machine instances to alternate hosts during hardware maintenance without downtime.",
            "Regional Persistent Disks replicate block storage synchronously across two zones in the same region, providing an RPO of zero.",
            "Local SSDs are physically attached to the server host, delivering ultra-low latency and high IOPS, but are ephemeral in nature.",
            "Spot VMs offer 60% to 91% discount on standard virtual machines but can be preempted by Google with a 30-second warning.",
            "Enables custom metadata scripts (startup/shutdown scripts) queried at the link-local metadata server IP address 169.254.169.254.",
            "Sole-Tenant Nodes isolate physical server hardware for a single client, supporting compliance and licensing requirements.",
            "Managed Instance Groups (MIGs) utilize templates to autoscale, autoheal, and load balance instances across regional zones.",
            "Shielded VMs protect instances against boot-level malware and rootkits using Unified Extensible Firmware Interface (UEFI) secure boot.",
            "Custom Machine Types allow configuring exact vCPU count and memory size, avoiding paying for unused resources.",
            "IAM permissions for virtual machines are managed using service accounts assigned to instances rather than downloading keys.",
            "Interconnects and VPC routers enable VMs to communicate privately using internal IP address allocations.",
            "Supports nested virtualization, allowing developers to run hypervisors inside Compute Engine VMs.",
            "Provides disk snapshots that are stored redundantly across regions, enabling fast recovery of historical disk states.",
            "Virtual machine resource tags or network tags allow applying specific firewall policies and routing decisions.",
            "Integrates with OS Login, linking VM access credentials directly to organizational Google Workspace workspace identities.",
            "Resource policies allow scheduling automatic disk snapshots and VM start/stop actions to optimize utilization.",
            "Billed per second with a 1-minute minimum, making it highly cost-effective for short-term batch runs.",
            "Supports GPU attachment (NVIDIA Tesla models) for accelerating machine learning workloads and high-performance computing.",
            "Provides VM manager capabilities for patch management, OS configuration, and inventory reporting across fleets."
        ],
        "scenarios": [
            {
                "scenario": "A legacy enterprise accounting system requires direct root access to customize the Linux kernel and attach high-speed local block volumes.",
                "solution": "Deploy the application on Compute Engine custom virtual machines, attaching Local SSDs for scratch storage and Persistent Disks for durable data."
            },
            {
                "scenario": "A batch media rendering pipeline needs to process thousands of image files on a tight budget. The tasks can be safely interrupted and resumed.",
                "solution": "Configure a Managed Instance Group using Spot VMs, autoscaling based on pub/sub queue depth to render images at up to 90% discount."
            }
        ],
        "commands": [
            {
                "description": "Create a virtual machine instance with network tags and secure Debian image",
                "command": "gcloud compute instances create prod-web-vm \\\n  --zone=us-central1-a \\\n  --machine-type=e2-standard-4 \\\n  --tags=http-server,https-server \\\n  --image-family=debian-11 \\\n  --image-project=debian-cloud"
            },
            {
                "description": "Establish a secure interactive SSH connection to the virtual machine through an IAP tunnel",
                "command": "gcloud compute ssh prod-web-vm \\\n  --zone=us-central1-a \\\n  --tunnel-through-iap"
            }
        ]
    },
    "google-kubernetes-engine--gke-": {
        "keyPoints": [
            "Managed Kubernetes environment supporting containerized deployment, horizontal scaling, and automated container health checks.",
            "GKE Autopilot fully manages nodes, scaling, operating systems, and security boundaries, billing only for running pods.",
            "GKE Standard leaves the cluster's underlying VM node pools and node configurations under the control of cluster admins.",
            "Workload Identity maps Kubernetes service accounts directly to IAM service accounts, eliminating service account JSON files.",
            "Regional Clusters distribute the control plane and worker nodes across three zones in a region, guaranteeing a 99.95% availability SLA.",
            "Cluster Autoscaler resizes worker node pools dynamically based on scheduling demands and can scale pools to zero when empty.",
            "Binary Authorization integrates with GKE to block deployment of container images not signed by trusted build keys.",
            "Horizontal Pod Autoscaler (HPA) adjusts pod replica counts based on CPU utilization or custom monitoring metrics.",
            "Vertical Pod Autoscaler (VPA) analyzes pod resource consumption and recommends or adjusts container CPU and memory requests.",
            "Node Auto-Provisioning automatically creates custom node pools with appropriate machine shapes to fit pending pod criteria.",
            "Container-Optimized OS (COS) is the default, hardened node operating system designed by Google specifically to run containers.",
            "Kubernetes Network Policies restrict traffic routing between pods, enforcing microsegmentation within the cluster.",
            "Managed Service for Prometheus collects pod metrics, offering out-of-the-box monitoring and dashboard support.",
            "Private Clusters isolate nodes from the internet, exposing the control plane endpoint only via private VPC subnets or IAP.",
            "Multi-Cluster Ingress orchestrates load balancing across GKE clusters deployed across multiple global Google Cloud regions.",
            "GKE Datapath V2 improves network performance and enforces policy structures using eBPF technology.",
            "Node Auto-Repair monitors node health and automatically recreates failed VMs to maintain cluster capacity.",
            "Node Auto-Upgrade automatically patches OS vulnerabilities and upgrades the Kubernetes version on worker nodes.",
            "Supports local SSDs and persistent disk mounts as PersistentVolumes, managed automatically by CSI storage drivers.",
            "Integrates with Cloud Run for Anthos (Knative) to deploy serverless, event-driven containers directly on container clusters."
        ],
        "scenarios": [
            {
                "scenario": "A development team wants to deploy a modular microservices app on Kubernetes without managing VM configurations, OS patches, or node scaling.",
                "solution": "Deploy the application workloads to GKE Autopilot, letting Google manage the node lifecycle and billing strictly based on pod resources."
            },
            {
                "scenario": "An enterprise requires that pods running inside a cluster connect securely to BigQuery without storing static JSON credentials in Kubernetes secrets.",
                "solution": "Enable Workload Identity on GKE, bind the Kubernetes ServiceAccount to an IAM Service Account, and assign the IAM account BigQuery access."
            }
        ],
        "commands": [
            {
                "description": "Provision a regional GKE Autopilot cluster inside a specific subnet",
                "command": "gcloud container clusters create-auto production-cluster \\\n  --region=us-central1 \\\n  --network=prod-vpc \\\n  --subnetwork=us-central1-subnet"
            },
            {
                "description": "Retrieve GKE cluster credentials to configure local kubectl configuration",
                "command": "gcloud container clusters get-credentials production-cluster \\\n  --region=us-central1"
            }
        ]
    },
    "cloud-run": {
        "keyPoints": [
            "Serverless compute runtime that executes stateless HTTP containers, automatically scaling instances up or down to zero.",
            "Supports scaling down to zero instances when traffic halts, completely eliminating idle compute charges.",
            "Each active container instance handles up to 250 concurrent requests, reducing cold start occurrences significantly.",
            "Revisions are immutable snapshots of deployed code and settings, enabling safe rollback and traffic splitting.",
            "Serverless VPC Access connectors bridge Cloud Run traffic privately to internal VPC resources like databases.",
            "Cloud Run Jobs execute run-to-completion batch tasks that do not handle incoming web request traffic.",
            "Custom domains can be mapped directly to Cloud Run services with automated SSL certificate provisioning.",
            "Allows setting minimum instances (e.g. min-instances=1) to keep containers pre-warmed and avoid cold starts.",
            "Integrates natively with Secret Manager to mount API keys and database credentials as environment variables or volumes.",
            "Integrates with Cloud IAM to authenticate service-to-service calls using OIDC tokens.",
            "Billed per 100 milliseconds of CPU and memory execution, optimizing expenses for highly variable traffic.",
            "Supports CPU allocation configurations: allocated only during request processing, or allocated constantly.",
            "Deployments are integrated with Cloud Build, compiling source code directly into containers for execution.",
            "Each revision supports traffic splitting, allowing canary testing by routing small percentages of traffic to a new version.",
            "Provides built-in request concurrency settings to restrict the load placed on single container instances.",
            "Enables ingress restriction settings (internal vs. external) to prevent public access to internal services.",
            "Monitors container logs and HTTP response latency metrics automatically via Cloud Logging and Cloud Monitoring.",
            "Supports binary payloads, streaming HTTP responses, and gRPC endpoints.",
            "Runs containers based on the Knative standard, avoiding vendor lock-in to Google Cloud platforms.",
            "Allows adjusting execution timeouts up to 60 minutes for long-running API operations."
        ],
        "scenarios": [
            {
                "scenario": "A company has a web shop backend API container that experiences highly volatile traffic spikes, and wants to pay $0 during nighttime idle periods.",
                "solution": "Deploy the API container on Cloud Run, setting minimum instances to zero and dynamic scaling to handle sudden spikes."
            },
            {
                "scenario": "A team wants to deploy a new version of a user registration API but wants to route only 10% of live traffic to it to test stability.",
                "solution": "Deploy a new revision of the Cloud Run service, and configure traffic splitting to route 10% to the new revision and 90% to the active revision."
            }
        ],
        "commands": [
            {
                "description": "Deploy a container image to Cloud Run with public access allowed",
                "command": "gcloud run deploy user-service \\\n  --image=gcr.io/prod-project/user-service:v1 \\\n  --region=us-central1 \\\n  --allow-unauthenticated"
            },
            {
                "description": "Configure traffic splitting, routing 10% to the latest revision and 90% to the stable revision",
                "command": "gcloud run services update-traffic user-service \\\n  --region=us-central1 \\\n  --to-revisions=LATEST=10,stable-rev-1=90"
            }
        ]
    },
    "cloud-storage": {
        "keyPoints": [
            "Unified object storage service offering high availability, durability, and standard web API access.",
            "Offers four storage classes matching access frequencies: Standard, Nearline (30-day), Coldline (90-day), and Archive (365-day).",
            "Uniform Bucket-Level Access (UBLA) simplifies security by enforcing IAM policies at the bucket level, disabling object ACLs.",
            "Lifecycle Management Rules automatically transition objects to cheaper classes or delete them based on criteria like age.",
            "Object Versioning stores historical states of modified files, protecting against accidental overwrite or deletion.",
            "Signed URLs grant temporary read or write access to private files using service account signatures without Google logins.",
            "Object Retention Lock (WORM policy) prevents deletion of files until a specified retention term expires.",
            "Dual-region and Multi-region storage options replicate data across zones and regions to survive regional disasters.",
            "Storage Transfer Service automates scheduled bulk data imports from AWS S3, Azure Blob, or local network shares.",
            "Data is encrypted at rest automatically using Google-managed keys, or optionally using Customer-Managed Keys (CMEK).",
            "Offers strong global consistency, ensuring that read-after-write operations always return the updated object payload.",
            "Pub/Sub Notifications alert external systems immediately whenever objects are created, overwritten, or deleted.",
            "Requester Pays configurations charge access and egress fees to the client reading the object rather than the bucket owner.",
            "Allows setting up static website hosting directly from public buckets, serving content over HTTP.",
            "Encourages chunked parallel uploads to speed up ingestion of multi-gigabyte or terabyte files.",
            "Object lifecycle rules support age, created-before, custom-time, and number-of-newer-versions conditions.",
            "Integrates with Sensitive Data Protection (DLP) to scan files for sensitive PII or credentials automatically.",
            "Provides hierarchical namespace features to support directory structures and high-throughput file access.",
            "Supports bucket locks that cannot be bypassed by anyone, including the project owner, once locked.",
            "Storage pricing is based on GB/month stored, network egress, and operational API requests (Class A/B operations)."
        ],
        "scenarios": [
            {
                "scenario": "A health portal requires storing patient reports for 7 years. The documents must remain immutable and protected against delete commands.",
                "solution": "Store reports in a Cloud Storage Archive bucket, enable Object Versioning, and apply a Bucket Lock retention policy of 7 years."
            },
            {
                "scenario": "An app backend needs to let anonymous mobile users upload profile photos directly to a private bucket without signing in to Google.",
                "solution": "Generate a short-lived Cloud Storage Signed URL with write permissions, letting the client HTTP PUT the image directly."
            }
        ],
        "commands": [
            {
                "description": "Upload a local folder to a storage bucket with parallel processing",
                "command": "gcloud storage cp -r ./local-images gs://prod-media-bucket/"
            },
            {
                "description": "Apply a uniform bucket-level access policy to lock down object permissions",
                "command": "gcloud storage buckets update gs://prod-media-bucket/ --uniform-bucket-level-access"
            }
        ]
    },
    "spanner": {
        "keyPoints": [
            "Relational database providing global transactional consistency, horizontal write scaling, and SQL compatibility.",
            "Paxos-based consensus engine replicates writes synchronously across multi-region configurations, ensuring 99.999% availability.",
            "TrueTime API uses synchronized GPS receivers and atomic clocks to order transactions globally without read locks.",
            "Primary keys must be designed carefully to avoid auto-incrementing integers, which cluster writes onto a single node hotspot.",
            "Spanner Graph allows running complex open-source graph queries directly over relational schemas.",
            "Scales database compute capacity (nodes/processing units) and storage independently without operational downtime.",
            "Supports online DDL schema changes, allowing table additions or indexing to run while the database is live.",
            "Provides Point-in-Time Recovery (PITR) to restore database states down to the exact microsecond.",
            "Allows storing related tables hierarchically using Interleaved Tables, co-locating child rows physically near parent rows.",
            "Data is encrypted automatically at rest, supporting Customer-Managed Encryption Keys (CMEK) via KMS.",
            "Fine-Grained Access Control limits user database access to specific tables, views, or rows using IAM privileges.",
            "Provides query execution plan visualizations to analyze index usage and tune query performance.",
            "Allows running read-only transactions without locking, maintaining high read throughput during massive write loads.",
            "Offers PostgreSQL compatibility dialect, allowing teams to migrate Postgres schemas with minimal changes.",
            "Features Spanner Data Boost, letting analytical queries run on independent resources without affecting transactional instances.",
            "Requires no failover management, as replication, failover, and balancing are handled natively by the platform.",
            "Billed based on node count (or fractional processing units), storage size, and outbound network traffic.",
            "Integrates with Datastream to capture relational updates and stream them into BigQuery.",
            "Supports generated columns and check constraints to enforce business rules inside database tables.",
            "Ideal for global financial books, inventory tracking, and payment processing systems requiring high consistency."
        ],
        "scenarios": [
            {
                "scenario": "A global credit card processor requires a transactional database that scales writes horizontally, guarantees SQL ACID compliance, and guarantees 99.999% availability.",
                "solution": "Deploy the transaction ledger on Cloud Spanner in a multi-regional configuration."
            },
            {
                "scenario": "A database architect notices Spanner write operations are bottlenecked because the primary key is a sequential timestamp column.",
                "solution": "Refactor the table primary key to use a hashed UUID or apply a bit-reverse function to the sequence to distribute writes."
            }
        ],
        "commands": [
            {
                "description": "Create a regional Cloud Spanner instance with 1 node configuration",
                "command": "gcloud spanner instances create prod-spanner \\\n  --config=regional-us-central1 \\\n  --nodes=1 \\\n  --description=\"Prod Spanner Database\""
            },
            {
                "description": "Create a database inside the Spanner instance",
                "command": "gcloud spanner databases create orders-db \\\n  --instance=prod-spanner"
            }
        ]
    },
    "alloydb-for-postgresql": {
        "keyPoints": [
            "Fully managed PostgreSQL-compatible relational database designed for demanding transactional and analytical workloads.",
            "Decoupled log-structured storage system separates compute nodes from storage, accelerating writes and failover speeds.",
            "Columnar Engine caches analytical query tables in memory, executing scans up to 100x faster than standard PostgreSQL.",
            "Provides full PostgreSQL 14/15 compatibility, supporting standard extensions, drivers, and frameworks.",
            "AlloyDB Omni allows developers to download and run the high-performance engine inside containers on local machines.",
            "Supports automatic horizontal scale-out of read replica pools to handle massive query concurrency.",
            "Integrates natively with Vertex AI, executing machine learning model predictions directly via standard SQL queries.",
            "Provides an SLA of 99.99% for high-availability configurations, including automatic failover and node patching.",
            "Leverages Intelligent Auto-Tuning to configure memory layouts, write paths, and vacuuming parameters dynamically.",
            "Encourages vector search capabilities using the pgvector extension for AI and retrieval-augmented generation systems.",
            "Data storage scales automatically up to 64TB per cluster without manual provisioning actions.",
            "Supports database snapshots and Point-in-Time Recovery (PITR) to safeguard transactional histories.",
            "Requires database endpoints to be accessed via private IP addresses (VPC Peering/PSC) for security.",
            "Allows configuring query pool sizes, compute vCPU limits, and cache sizes on a per-instance basis.",
            "Uses a distributed write-ahead log (WAL) system to reduce transactional commit latencies.",
            "Enables database monitoring and diagnostic dashboards directly inside the Google Cloud console.",
            "Supports IAM authentication alongside traditional database username and password setups.",
            "Integrates with Datastream to facilitate real-time CDC replication into analytical data warehouses.",
            "Provides backup recovery verification checks to guarantee the integrity of cluster snapshots.",
            "Pricing is calculated on database vCPU cores, memory capacity, active storage, and backup size."
        ],
        "scenarios": [
            {
                "scenario": "An enterprise wants to migrate a Postgres database to Google Cloud, requiring a 100% compatible engine that can accelerate reporting queries without manual indexing.",
                "solution": "Migrate the database to AlloyDB for PostgreSQL, and configure the in-memory Columnar Engine to cache the reporting tables."
            },
            {
                "scenario": "A development team wants to prototype pgvector searches locally on their laptops using the exact database engine they will use in production.",
                "solution": "Deploy AlloyDB Omni locally inside a Docker container, configure the schema, and deploy standard SQL queries."
            }
        ],
        "commands": [
            {
                "description": "Provision an AlloyDB cluster in us-central1 region",
                "command": "gcloud alloydb clusters create prod-alloydb \\\n  --password=strongpassword123 \\\n  --region=us-central1 \\\n  --network=prod-vpc"
            },
            {
                "description": "Create a primary database instance inside the cluster with 4 vCPUs",
                "command": "gcloud alloydb instances create prod-primary \\\n  --cluster=prod-alloydb \\\n  --instance-type=PRIMARY \\\n  --cpu-count=4 \\\n  --region=us-central1"
            }
        ]
    },
    "bigtable": {
        "keyPoints": [
            "Wide-column NoSQL database engine designed for high-throughput, single-digit millisecond latency workloads.",
            "A single cluster node handles up to 10,000 writes per second, scaling capacity linearly as nodes are added.",
            "Row keys must be designed lexicographically (sorted alphabetically) to balance query loads across nodes and prevent hotspots.",
            "Key Visualizer diagnostic tool provides visual heatmaps to identify and resolve read-write hotspots in real-time.",
            "Supports multi-cluster replication across regions, enabling active-active write configurations and seamless failover.",
            "Optimizes database size using automated garbage collection policies to prune old row versions or expired data.",
            "Data is stored in sorted SSTables, partitioned dynamically across nodes as tablets scale in size.",
            "Integrates natively with Apache Spark, Hadoop, and Dataflow pipelines via standard HBase APIs.",
            "Provides single-digit millisecond latency for reads and writes, making it ideal for financial ticks and IoT streams.",
            "Does not support transactional SQL queries or joins; tables are flat and key-value based.",
            "Requires client access to run via gRPC endpoints, optimizing network performance.",
            "Offers choice of SSD storage for latency-critical apps, or HDD storage for low-cost archive use cases.",
            "Enables autoscaling policies to dynamically adjust node counts based on CPU utilization and storage load.",
            "Supports IAM policies to restrict access at the instance, cluster, or table level.",
            "Integrates with Vertex AI Vector Search to perform nearest-neighbor searches directly on stored column data.",
            "Supports backup and restore operations to clone tables across instances or regions.",
            "Uses column families to group related columns together, optimizing disk read performance.",
            "Allows live migration of clusters between zones and storage tiers without downtime.",
            "Provides detailed client libraries for Java, Python, Go, Node.js, and C++.",
            "Pricing is based on cluster node count, storage tier capacity, and network data egress."
        ],
        "scenarios": [
            {
                "scenario": "An IoT gateway is receiving telemetry logs from millions of smart devices. Writes are heavy and must be committed in real-time with sub-10ms latency.",
                "solution": "Deploy a Cloud Bigtable instance, using SSD storage, and stream logs using Cloud Pub/Sub and a Dataflow write pipeline."
            },
            {
                "scenario": "A Bigtable cluster is experiencing CPU spikes because all read-write operations are targeting row keys that begin with the current date.",
                "solution": "Analyze the access pattern using Key Visualizer, and change the row key design to prepend a hashed client ID to distribute writes."
            }
        ],
        "commands": [
            {
                "description": "Provision a Bigtable instance with 3 SSD nodes in a cluster",
                "command": "gcloud bigtable instances create prod-bigtable \\\n  --display-name=\"Prod Bigtable\" \\\n  --cluster-storage-type=SSD \\\n  --cluster-config=id=prod-cluster,zone=us-central1-a,nodes=3"
            },
            {
                "description": "List all active tables inside the Bigtable instance",
                "command": "gcloud bigtable instances list"
            }
        ]
    },
    "firestore": {
        "keyPoints": [
            "Serverless document database optimized for mobile, web, and server application development.",
            "Supports Native Mode for real-time synchronization listeners and direct client-side SDK integration.",
            "Supports Datastore Mode for high-throughput server backends requiring backwards-compatible Datastore API access.",
            "Automatically indexes every field in a document, enabling fast querying without manual configuration.",
            "Composite indices are required for queries that filter on multiple properties, and must be created manually.",
            "Point-in-Time Recovery (PITR) allows database rollbacks to any specific microsecond to recover from corruption.",
            "Transactions execute with ACID compliance across multiple documents, ensuring data consistency.",
            "Supports offline data caching on client SDKs, syncing changes automatically once connection resumes.",
            "Allows defining Security Rules to validate database writes and authorize requests directly from clients.",
            "Integrates with vector similarity search to execute semantic search queries on embedded vector properties.",
            "Offers a multi-region configuration that replicates data across zones and regions for high availability.",
            "Billing is based on document read, write, and delete counts, alongside database storage size.",
            "Allows exporting collection datasets to Cloud Storage for backup or BigQuery analysis.",
            "Provides sub-second real-time notifications to thousands of connected clients simultaneously.",
            "Limits individual document sizes to 1MB and limits write rates to a single document to 1 write per second.",
            "Supports collection groups, allowing queries to search across identical collections nested inside documents.",
            "Integrates with Firebase Authentication to validate user identity contexts inside security rules.",
            "Provides query performance recommendations and slow-query log diagnostics.",
            "Supports cursor-based query pagination to load large datasets incrementally.",
            "Requires no infrastructure provisioning, automatically scaling capacity to handle millions of active users."
        ],
        "scenarios": [
            {
                "scenario": "A mobile chat application needs a database that syncs user message lists instantly across devices and supports offline typing when tunnels are offline.",
                "solution": "Configure Firestore in Native Mode and attach real-time snapshot listeners to the client-side mobile application SDKs."
            },
            {
                "scenario": "An API query sorting records by user age and registration date is failing with a missing index exception.",
                "solution": "Retrieve the composite index generation link from the Svelte console logs or error message, and create the index in Firestore."
            }
        ],
        "commands": [
            {
                "description": "Create a Native Mode Firestore database in the us-central1 region",
                "command": "gcloud firestore databases create --location=us-central1 --type=firestore-native"
            },
            {
                "description": "Export the Firestore database collections to a backup storage bucket",
                "command": "gcloud firestore export gs://prod-firestore-backups"
            }
        ]
    },
    "bigquery": {
        "keyPoints": [
            "Serverless enterprise data warehouse designed to analyze petabytes of structured and semi-structured data.",
            "Decoupled architecture separates storage billing from query execution slot billing, optimizing data center costs.",
            "Table Partitioning divides tables by date/timestamp or integer ranges, limiting query data scan volumes.",
            "Table Clustering groups data physically based on column values, accelerating filter and aggregation performance.",
            "BI Engine caches dataset tables in memory automatically, providing sub-second dashboard rendering speeds.",
            "BigQuery ML allows building, training, and running machine learning models using standard SQL expressions.",
            "BigQuery Editions (Standard, Enterprise, Enterprise Plus) offer capacity-based slot pricing models for budget predictability.",
            "Allows querying external data sources (GCS, Bigtable, Cloud SQL) without importing data using External Tables.",
            "Supports Column-Level and Row-Level Security to restrict user visibility into sensitive tables.",
            "Materialized Views cache query results dynamically, updating automatically as source tables ingest records.",
            "Integrates with Vertex AI to execute model predictions and text embeddings queries using SQL.",
            "Enables real-time data ingestion using streaming APIs, supporting millions of incoming rows per second.",
            "Provides SQL dialect compatibility with standard ANSI SQL, including support for joins, subqueries, and window functions.",
            "Information Schema views expose metadata, query execution costs, and user table histories.",
            "Search Indexes accelerate keyword searches on string columns and nested JSON objects.",
            "Enables data sharing across organization projects securely using Analytics Hub listings.",
            "Supports time travel queries, letting users query deleted or modified tables from up to 7 days ago.",
            "Maintains query results histories automatically in temporary cached tables for 24 hours at no cost.",
            "Provides BigQuery Omni to query data stored across AWS S3 or Azure Blob without data egress costs.",
            "Query billing is based on TBs scanned ($5/TB on on-demand pricing) or capacity slots reserved."
        ],
        "scenarios": [
            {
                "scenario": "A retail chain has a multi-terabyte transaction log table. Analysts need to run queries on specific days without scanning historical records.",
                "solution": "Configure table partitioning on the transaction_date column and require a partition filter on all analytical queries."
            },
            {
                "scenario": "A financial reporting dashboard is slow and expensive because hundreds of users query the same tables simultaneously.",
                "solution": "Enable BigQuery BI Engine to cache the tables in-memory, accelerating dashboard rendering and reducing slot consumption."
            }
        ],
        "commands": [
            {
                "description": "Execute an ANSI-SQL query on a BigQuery table from the command line interface",
                "command": "bq query --use_legacy_sql=false \\\n  'SELECT product_id, SUM(price) FROM `prod-proj.sales.transactions` WHERE date = \"2026-06-15\" GROUP BY product_id'"
            },
            {
                "description": "Provision a new table with daily partition configuration",
                "command": "bq mk --table --time_partitioning_type=DAY sales.partitioned_transactions"
            }
        ]
    },
    "secret-manager": {
        "keyPoints": [
            "Secure storage system for application API keys, database credentials, certificates, and operational tokens.",
            "Secrets are versioned and immutable; editing a secret value generates a new active version.",
            "Access is locked down via IAM policies, requiring the Secret Accessor role to retrieve secret payloads.",
            "Supports automatic secret rotation by triggering Pub/Sub alerts that invoke serverless runtimes.",
            "Integrates with GKE and Cloud Run, enabling secrets to be mounted as local volumes or environment variables.",
            "Replicates secrets automatically across regions, supporting multi-region failover and access consistency.",
            "Secrets can be disabled temporarily to revoke application access without deleting the underlying metadata.",
            "Provides expiration schedules to automatically destroy secret versions at specified times.",
            "Integrates with Cloud KMS to encrypt secret payloads using Customer-Managed Keys (CMEK).",
            "Logs every access request in Cloud Audit Logs to track who retrieved which secret version.",
            "Provides notification channels via Pub/Sub to alert developers when secrets are created, updated, or rotated.",
            "Limits secret payload sizes to 64KB, designed specifically for credentials rather than configuration files.",
            "Allows setting up secret metadata tags to organize resources by environment or department.",
            "Enables quick recovery of deleted secrets within a 30-day grace period.",
            "Supports customer-managed key configuration on a per-secret basis.",
            "Eliminates the risk of committing passwords in plain text to Git source control repositories.",
            "Supports programmatic access via Client Libraries in Java, Go, Python, Node.js, and C#.",
            "Provides an easy-to-use CLI and Cloud Console interface to rotate values manually.",
            "Billing is based on active secrets count ($0.06/secret/month) and API access requests ($0.03/10k calls).",
            "Designed to meet strict regulatory standards for auditing, credential isolation, and rotation."
        ],
        "scenarios": [
            {
                "scenario": "A developer wants to prevent database connection passwords from being committed to a public GitHub repository.",
                "solution": "Store the database password in Secret Manager, and assign the Secret Accessor IAM role to the application service account."
            },
            {
                "scenario": "An enterprise security policy dictates that all external API keys must be changed every 30 days automatically.",
                "solution": "Set up a secret rotation policy in Secret Manager, linking it to a Pub/Sub topic that triggers a Cloud Run handler to update the version."
            }
        ],
        "commands": [
            {
                "description": "Create a new secret with automatic replication configuration",
                "command": "gcloud secrets create db-passwd --replication-policy=automatic"
            },
            {
                "description": "Retrieve the payload of the latest version of a secret",
                "command": "gcloud secrets versions access latest --secret=db-passwd"
            }
        ]
    },
    "cloud-key-management-service": {
        "keyPoints": [
            "Centralized cloud service to generate, rotate, and manage cryptographic keys for encrypting data.",
            "Supports symmetric, asymmetric, and signing key rings matching various security patterns.",
            "Customer-Managed Encryption Keys (CMEK) integrate with GCS, BigQuery, and compute disks to manage data locks.",
            "Cloud HSM provides FIPS 140-2 Level 3 validated physical security modules protecting key lifecycle events.",
            "Cloud EKM delegates key protection to on-premises key management servers outside Google Cloud.",
            "Cryptographic keys cannot be deleted immediately; they must be scheduled for destruction, with a 24-hour restore window.",
            "Allows configuring automatic key rotation schedules to generate new key versions on specified cycles.",
            "Access control is managed at the key ring or key level using specific IAM decrypt/encrypt roles.",
            "Logs all encryption and decryption operations to Cloud Audit Logs for compliance reviews.",
            "Integrates with external identity providers to authorize key operations dynamically.",
            "Supports importing on-premises cryptographic keys into Cloud KMS to maintain schema configurations.",
            "Provides high-performance encryption operations directly inside regional Google locations.",
            "Asymmetric keys support public-key encryption and digital signature verification.",
            "Allows disabling key versions to instantly lock down encrypted storage buckets or disks.",
            "Designed to comply with HIPAA, PCI-DSS, FedRAMP, and GDPR security standards.",
            "Supports key rings to organize keys logically by department, location, or environment.",
            "Provides client libraries and a REST API to perform cryptographic functions programmatically.",
            "Supports symmetric keys for envelope encryption, encrypting local keys with a KMS root key.",
            "Saves operational overheads compared to maintaining on-premises HSM hardware nodes.",
            "Key usage is billed per active key version per month, plus cryptographic transaction volumes."
        ],
        "scenarios": [
            {
                "scenario": "A regulatory compliance audit mandates that all medical scan backups in GCS be encrypted using keys managed in an on-premises datacenter.",
                "solution": "Configure GCS CMEK, linking it to a Cloud KMS key integrated with Cloud EKM pointing to the on-premises HSM."
            },
            {
                "scenario": "A security incident occurs, and a database administrator needs to instantly revoke all read access to encrypted database tables.",
                "solution": "Disable the active version of the Customer-Managed Encryption Key in Cloud KMS, instantly blocking decryption operations."
            }
        ],
        "commands": [
            {
                "description": "Create a key ring inside a specified regional location",
                "command": "gcloud kms keyrings create prod-keyring --location=us-central1"
            },
            {
                "description": "Provision a symmetric encryption key inside the key ring",
                "command": "gcloud kms keys create app-key \\\n  --keyring=prod-keyring \\\n  --location=us-central1 \\\n  --purpose=encryption"
            }
        ]
    },
    "google-cloud-armor": {
        "keyPoints": [
            "Web Application Firewall (WAF) protecting internet-facing endpoints from Layer 7 exploits and DDoS floods.",
            "Deploys at the Google Front End (GFE) edge, filtering requests before they reach compute backend servers.",
            "Preconfigured WAF rules support checking against OWASP Top 10 exploits like SQLi and XSS.",
            "Rate Limiting rules automatically ban client IP ranges that exceed configured request count limits.",
            "Adaptive Protection uses machine learning anomaly detection to generate rules dynamically during attacks.",
            "Filters traffic based on IP address ranges, geographic country blocks, or request header properties.",
            "Integrates with Google Cloud Load Balancer, acting as the security gateway for backend services.",
            "Provides a preview mode to test firewall rules against live traffic logs without blocking requests.",
            "Protects backend compute instances from volumetric DDoS attacks (Layer 3/4) automatically.",
            "Allows configuring custom error responses (e.g. 403, 404, 502) when requests are blocked.",
            "Provides security dashboards to view blocked traffic, rule matches, and threat scores.",
            "Supports configuring rule priorities to control the order of rule evaluation.",
            "Enables WAF rule customization using SQL-like expressions to check cookies, headers, and paths.",
            "Helps mitigate brute force logins, credential stuffing, and web scraping attacks.",
            "Integrates with Cloud Logging to write rule match logs for security information event management (SIEM).",
            "Supports edge security policies that apply to Cloud CDN cached content requests.",
            "Allows Whitelisting administrative IP ranges to bypass web application firewall rules.",
            "Provides protection policies for internal application load balancers within VPCs.",
            "Pricing is calculated per security policy per month, plus request verification volumes.",
            "Essential security layer for public-facing e-commerce APIs and corporate web portals."
        ],
        "scenarios": [
            {
                "scenario": "A login endpoint is under a distributed brute-force attack from a botnet. Backends are failing due to request volume.",
                "solution": "Add a rate limiting rule to the Cloud Armor security policy to block client IPs exceeding 100 requests per minute."
            },
            {
                "scenario": "A company wants to block all SQL injection attempts and cross-site scripting (XSS) exploit payloads at the network edge.",
                "solution": "Apply preconfigured WAF rules ('sqli-stable' and 'xss-stable') to the Cloud Armor policy and attach it to the Load Balancer."
            }
        ],
        "commands": [
            {
                "description": "Create a Cloud Armor security policy container",
                "command": "gcloud compute security-policies create prod-security-policy"
            },
            {
                "description": "Create a security rule inside the policy to block SQL injection traffic",
                "command": "gcloud compute security-policies rules create 1000 \\\n  --security-policy=prod-security-policy \\\n  --expression=\"evaluatePreconfiguredExpr('sqli-stable')\" \\\n  --action=deny-403"
            }
        ]
    }
}

print("Beginning advanced detail compile...")

for service in services:
    svc_id = service['id']
    svc_name = service['name']
    svc_cat = service['category']
    svc_arch = service.get('architecturalCategory', 'None')
    svc_desc = service.get('description', '')

    # 1. Use hardcoded overrides if present
    if svc_id in PRECISE_OVERRAIDES:
        details = PRECISE_OVERRAIDES[svc_id]
    else:
        # Dynamic Heuristic Details Engine
        # We will generate EXACTLY 18 key points, 2 scenarios, and 2 commands for each service
        
        # Determine CLI tool parameters
        cli_prefix = get_cli_group(svc_id, svc_name)
        short_name = get_clean_slug(svc_name)
        
        # A. Key Points (18 distinct points)
        key_points = []
        
        # 1-3. Core architectural points based on name, description and architectural category
        key_points.append(f"Provides a dedicated {svc_arch} platform engineered to {svc_desc[0].lower() + svc_desc[1:] if svc_desc else 'provide enterprise cloud support'}.")
        key_points.append(f"Integrates {svc_name} capabilities directly into multi-tier cloud architectures, serving as a key component of the {svc_cat} portfolio.")
        key_points.append(f"Encourages standard interface structures (REST APIs, Client SDKs, or console controls) to facilitate rapid cloud resource provisioning.")
        
        # 4-6. Category-specific architectural rules
        cat_facts = CATEGORY_FACTS.get(svc_cat, [
            "Aligned with the official Google Cloud Architecture Framework to ensure enterprise design compliance.",
            "Deploys under unified resource structures (folders/projects) to streamline platform administration.",
            "Maintains standard integration hooks with wider Google Cloud logging and operations engines.",
            "Optimizes workload distribution across regional zone grids to prevent single-point failures.",
            "Billed under standard pay-as-you-go structures to allow cost tracking and billing optimization."
        ])
        for fact in cat_facts[:3]:
            key_points.append(fact.replace("the service", svc_name))
            
        # 7-9. Subcategory-specific technical details
        sub_facts = SUBCATEGORY_FACTS.get(svc_arch, [
            f"Optimizes {svc_name} performance through automated platform scaling and resource balancing.",
            f"Enables resource segregation, logical naming conventions, and tag-based configuration policies for {svc_name}.",
            f"Integrates with VPC routing and private service access architectures to secure communication tunnels."
        ])
        for fact in sub_facts[:3]:
            key_points.append(fact)
            
        # 10-12. Security & Compliance
        key_points.append(f"Governs access to {svc_name} using standard IAM roles (e.g. roles/{short_name}.admin and roles/{short_name}.viewer) for fine-grained permissions.")
        key_points.append(f"Supports audit logging to record administrative actions and verify API configuration modifications for compliance reports.")
        key_points.append(f"Secures operational payloads using encryption at rest (Google-managed or Customer-Managed Keys via KMS) and SSL/TLS in transit.")
        
        # 13-15. Reliability, Scaling & HA
        key_points.append(f"Offers regional and multi-regional configuration options, duplicating service state across multiple zones to sustain outage events.")
        key_points.append(f"Enforces API quotas and rate limits programmatically to prevent resource starvation and noisy-neighbor interference.")
        key_points.append(f"Provides service recovery tools, regular status logs, and high-availability SLAs matching enterprise uptime goals.")
        
        # 16-18. Operations & Cost Optimization
        key_points.append(f"Billed based on resource metrics (e.g., operations count, active connections, or gigabytes stored) allowing cost optimization.")
        key_points.append(f"Integrates with Cloud Monitoring and Cloud Logging to enable real-time alerting, metrics tracking, and diagnostic dashboards.")
        key_points.append(f"Enables command line administration through the gcloud CLI tool, allowing pipeline automation and scripting.")
        
        # B. Scenarios (2 distinct scenarios)
        scenarios = [
            {
                "scenario": f"An enterprise wants to construct a secure architectural pattern involving {svc_name} that blocks public internet ingress and enforces strict access restrictions.",
                "solution": f"Deploy the {svc_name} resource inside a VPC Service Control perimeter, routing connections privately using Serverless VPC connectors or internal gateways, and assign permissions using IAM roles."
            },
            {
                "scenario": f"A development team needs to build automated CI/CD configurations that configure and audit {svc_name} operations on a regular basis while tracking costs.",
                "solution": f"Use Cloud Build scripts executing 'gcloud' commands to provision the {svc_name} resources, enable Cloud Audit Logs, and configure budget notifications at the project folder level."
            }
        ]
        
        # C. Commands (2 distinct commands)
        commands = [
            {
                "description": f"Create or configure a new {svc_name} resource",
                "command": f"{cli_prefix} create prod-{short_name}-resource \\\n  --region=us-central1 \\\n  --description=\"Production {svc_name} Resource\""
            },
            {
                "description": f"List active {svc_name} instances and query configuration states",
                "command": f"{cli_prefix} list --format=\"table(name, state, updateTime)\""
            }
        ]
        
        details = {
            "keyPoints": key_points,
            "scenarios": scenarios,
            "commands": commands
        }

    # Write details file
    detail_file_path = os.path.join(DETAILS_DIR, f"{svc_id}.json")
    with open(detail_file_path, 'w', encoding='utf-8') as df:
        json.dump(details, df, indent=2)

print(f"Compilation complete. Successfully wrote detail JSONs containing 15-30 key points for {len(services)} services.")

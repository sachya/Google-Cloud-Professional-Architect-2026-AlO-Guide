export interface CorePrinciple {
  id: string;
  title: string;
  summary: string;
  points: string[];
}

export interface RecommendationArea {
  title: string;
  description: string;
  recommendations: string[];
}

export interface SharedFate {
  google: string[];
  customer: string[];
}

export interface Pillar {
  id: string;
  title: string;
  color: string;
  description: string;
  focusAreas: RecommendationArea[];
  examInsights: string[];
  sharedFate: SharedFate;
}

export interface CrossPillar {
  id: string;
  title: string;
  description: string;
  insights: string[];
}

export const corePrinciples: CorePrinciple[] = [
  {
    id: "design-for-change",
    title: "Design for Change",
    summary: "Build architectures that accommodate evolving user needs and technical capabilities through iteration and feedback loops.",
    points: [
      "No system is static; build development and production pipelines that enable safe, frequent, and small changes.",
      "Utilize DORA software delivery metrics (Deployment Frequency, Lead Time for Changes, Mean Time to Recovery, Change Failure Rate) to monitor deployment health.",
      "Iterate based on direct feedback from operations, developers, and end-users to continuously improve architecture.",
      "Avoid rigid, monolithic architectures that make scaling or refactoring difficult."
    ]
  },
  {
    id: "document-architecture",
    title: "Document Your Architecture",
    summary: "Establish a clear, common vocabulary and trace design history to guide future engineering decisions.",
    points: [
      "Create clear, visual architectural diagrams showing current cloud topologies, data flows, and networking.",
      "Maintain active architecture decision records (ADRs) to capture the rationale and context behind key decisions.",
      "Ensure documentation is maintained as systems change rather than treating it as a one-time task.",
      "Use document quality as a driver for team performance, enabling faster onboarding and preventing duplication."
    ]
  },
  {
    id: "simplify-and-manage",
    title: "Simplify Design and Use Managed Services",
    summary: "Minimize operational complexity and overhead by adopting fully managed services and resisting over-engineering.",
    points: [
      "Start simple: establish a Minimum Viable Product (MVP) and avoid over-engineering with unnecessary abstractions.",
      "Leverage fully managed services (e.g., Cloud Run, Cloud Spanner, GKE Autopilot) to offload baseline patching, backups, and infrastructure management.",
      "Reduce the risk, time, and administrative toil of maintaining custom virtual machine images and software stacks.",
      "Assess operational complexity regularly and simplify redundant or underutilized resources."
    ]
  },
  {
    id: "decouple-architecture",
    title: "Decouple Your Architecture",
    summary: "Separate applications and service components into independent subsystems to increase agility and fault tolerance.",
    points: [
      "Split monolithic workloads into loosely coupled microservices that communicate via APIs, event brokers (Pub/Sub), or queues.",
      "Ensure individual components can scale and fail independently without taking down the entire application stack.",
      "Apply localized security controls, distinct reliability objectives (SLAs), and granular cost boundaries to each subsystem.",
      "Use asynchronous patterns where possible to avoid locking resources during database writes or external API calls."
    ]
  },
  {
    id: "stateless-architecture",
    title: "Use a Stateless Architecture",
    summary: "Increase reliability, scalability, and disaster recovery speed by removing local state dependencies.",
    points: [
      "Avoid storing user sessions or application state on local virtual machine disks; delegate state to in-memory caches (Memorystore) or robust databases (Firestore, Cloud SQL).",
      "Enable rapid autoscaling (scaling up and down) without boot delays or dependency checks.",
      "Build components to withstand sudden termination or hard restarts gracefully, minimizing system downtime.",
      "Optimize frontend delivery by serving stateless assets directly from Content Delivery Networks (Cloud CDN)."
    ]
  }
];

export const pillars: Pillar[] = [
  {
    id: "operational-excellence",
    title: "Operational Excellence",
    color: "blue",
    description: "Efficiently deploy, operate, monitor, and manage your cloud workloads while continuously improving procedures.",
    focusAreas: [
      {
        title: "Operational Readiness using CloudOps",
        description: "Ensure that applications are fully prepared for production use and supported by rigorous observability.",
        recommendations: [
          "Define Service Level Objectives (SLOs) and Service Level Indicators (SLIs) aligned with business objectives.",
          "Implement comprehensive observability across logs, metrics, and traces using Cloud Monitoring, Cloud Logging, and Cloud Trace.",
          "Execute regular load and performance testing to validate scalability limits under realistic traffic conditions.",
          "Plan capacity and configure autoscaling rules based on historical usage and anticipated demand peaks."
        ]
      },
      {
        title: "Incidents and Problem Management",
        description: "Establish robust workflows to detect, mitigate, and resolve production failures while learning from incidents.",
        recommendations: [
          "Establish clear, documented incident response plans, defining roles (e.g., Incident Commander) and communication channels.",
          "Centralize logging and alerting to enable rapid detection, triage, and root-cause analysis during a outage.",
          "Conduct blameless postmortems (post-incident reviews) to identify systemic flaws and create actionable repair items.",
          "Automate recovery tasks where possible, such as configuring automated failover routing or auto-restarting services."
        ]
      },
      {
        title: "Automate and Manage Change",
        description: "Standardize environment configurations and deployment processes through automation to reduce human error.",
        recommendations: [
          "Adopt Infrastructure as Code (IaC) using Terraform to programmatically manage and version control Google Cloud resources.",
          "Build robust CI/CD pipelines (e.g., Cloud Build, Cloud Deploy) to compile, test, and release applications securely.",
          "Utilize version control for all configurations, environment parameters, and code deployments.",
          "Implement configuration management and automated health checks to prevent configuration drift."
        ]
      }
    ],
    examInsights: [
      "Exam scenario: An application has frequent manual release failures. Solution: Implement CI/CD using Cloud Build and provision staging/production environments identically using Terraform.",
      "Alerting design: Prefer alerting on SLO/Error Budget burn rates rather than single CPU spikes to prevent alert fatigue.",
      "Post-mortem: Always favor 'blameless' reviews focused on systemic failures (e.g., missing checks, poor automation) rather than individual human error."
    ],
    sharedFate: {
      google: [
        "Provides highly reliable global infrastructure, networks, and physical security.",
        "Delivers uptime SLA commitments for core platform services (e.g., 99.99% for Compute Engine).",
        "Publishes real-time platform status dashboards and provides enterprise support channels."
      ],
      customer: [
        "Defines business-aligned SLAs, SLOs, and monitors application health.",
        "Configures logging, dashboard alerts, and executes incident response playbooks.",
        "Writes Terraform configurations and builds secure CI/CD pipelines."
      ]
    }
  },
  {
    id: "security",
    title: "Security, Privacy, and Compliance",
    color: "purple",
    description: "Maximize the security of your data and workloads in the cloud, design for privacy, and align with compliance guidelines.",
    focusAreas: [
      {
        title: "Security by Design & Shift-Left",
        description: "Embed security rules into the early stages of software development and environment provisioning.",
        recommendations: [
          "Enforce least-privilege IAM policies, utilizing predefined roles or custom roles where access needs to be restricted.",
          "Integrate security scanning (vulnerabilities, credentials, packages) directly into code repositories and build pipelines.",
          "Use VPC Service Controls to establish secure perimeters around sensitive data APIs (e.g., Cloud Storage, BigQuery) to prevent exfiltration.",
          "Automate compliance monitoring and threat detection using Security Command Center (SCC)."
        ]
      },
      {
        title: "Zero Trust Architecture",
        description: "Enforce strict security validation for every user, device, and request regardless of network boundary.",
        recommendations: [
          "Use BeyondCorp Enterprise or Identity-Aware Proxy (IAP) to secure access to applications without traditional VPNs.",
          "Authenticate and authorize every access request dynamically based on user identity, device health, and context.",
          "Segment internal networks using VPC firewall rules, network tags, and private service connectivity."
        ]
      },
      {
        title: "Data Protection & Encryption",
        description: "Protect data in-transit, at-rest, and in-use through robust key management and cryptographic controls.",
        recommendations: [
          "Encrypt data at rest by default. Use Customer-Managed Encryption Keys (CMEK) via Cloud KMS for regulatory control.",
          "Utilize Confidential Computing VMs to encrypt data in memory (in-use) for highly sensitive workloads.",
          "Enforce HTTPS/TLS for all data in transit, and use Cloud Armor to protect public endpoints from DDoS and web attacks."
        ]
      }
    ],
    examInsights: [
      "Data Exfiltration protection: Enforce VPC Service Controls (VPC-SC) to block service accounts or users from copying data from inside the project to external buckets.",
      "VPN vs Zero Trust: Avoid VPNs for web application admin panels; use Identity-Aware Proxy (IAP) to authenticate users with Google Workspace credentials.",
      "KMS Key Rotation: For compliance, use Cloud KMS automatic key rotation. Do not manually re-encrypt old data unless required; KMS handles decrypting older versions automatically."
    ],
    sharedFate: {
      google: [
        "Protects physical hardware, hypervisors, and data center facilities.",
        "Encrypts data at rest by default using Google-managed keys.",
        "Secures the global fiber network backbone and coordinates global DDoS defense."
      ],
      customer: [
        "Manages IAM user access, group memberships, and service account keys.",
        "Configures firewall rules, VPC configurations, and VPC Service Controls boundaries.",
        "Configures KMS key rotation policies and handles application-level input validation."
      ]
    }
  },
  {
    id: "reliability",
    title: "Reliability",
    color: "emerald",
    description: "Design and operate resilient and highly available workloads to recover from infrastructure outages and software issues.",
    focusAreas: [
      {
        title: "High Availability & Scalability",
        description: "Distribute workloads to prevent single points of failure and scale automatically with traffic demand.",
        recommendations: [
          "Deploy workloads across multiple Zones or Regions. Use Multi-Region Cloud Storage, Cloud Spanner, or multi-zone GKE.",
          "Utilize Cloud Load Balancing (HTTP/S, TCP/UDP) with multi-region backends for automatic traffic redirection.",
          "Configure horizontal autoscaling for Compute Engine (Managed Instance Groups) and GKE Pods.",
          "Ensure databases are configured with active standby replication or multi-master architectures (e.g., Spanner)."
        ]
      },
      {
        title: "Failure Tolerance & Graceful Degradation",
        description: "Build applications that handle dependency failures gracefully without crashing entirely.",
        recommendations: [
          "Implement circuit breakers, exponential backoff, and retry jitter in application code to prevent cascading failures.",
          "Design graceful degradation: if an auxiliary service (like recommendations) is down, the core service (checkout) should continue working.",
          "Decouple synchronous API dependencies using Pub/Sub messages to queue tasks during traffic surges."
        ]
      },
      {
        title: "Disaster Recovery Testing",
        description: "Regularly test restore, failover, and recovery pipelines to meet RTO (Recovery Time) and RPO (Recovery Point) goals.",
        recommendations: [
          "Test database restores regularly from automated backups and transaction logs.",
          "Simulate failovers (e.g., regional shutdowns) in staging environments to validate active-passive or active-active configurations.",
          "Implement disaster recovery as code by automating infrastructure recreation in a secondary region using Terraform."
        ]
      }
    ],
    examInsights: [
      "Active-Active vs Active-Passive: Choose Active-Active for near-zero RTO requirements. Use Global Load Balancing with multi-region instances.",
      "Cloud Spanner vs Cloud SQL: For globally distributed, strongly consistent transactional data with zero-downtime regional failover, choose Cloud Spanner.",
      "Autoscaling Warm-up: If VMs take 10 minutes to bootstrap, configure predictive autoscaling or maintain a warm standby pool to handle sudden traffic spikes."
    ],
    sharedFate: {
      google: [
        "Maintains physical infrastructure redundancy (power, cooling, network links).",
        "Ensures regional and zonal isolation to prevent cross-facility failure propagation.",
        "Guarantees database replication uptime for managed multi-region databases."
      ],
      customer: [
        "Designs multi-zone/multi-region deployment topologies.",
        "Sets application retry logic, connection timeouts, and circuit breakers.",
        "Performs disaster recovery drills and manages application backup retention."
      ]
    }
  },
  {
    id: "cost-optimization",
    title: "Cost Optimization",
    color: "amber",
    description: "Maximize the business value of your investments in Google Cloud while eliminating waste and optimizing resources.",
    focusAreas: [
      {
        title: "Resource Right-Sizing",
        description: "Align provisioned compute, storage, and networking resources with actual utilization patterns.",
        recommendations: [
          "Use Active Assist / Recommender recommendations to identify over-provisioned VMs and downsize their machine types.",
          "Deprovision unattached persistent disks, idle load balancers, and unused static IP addresses.",
          "Adopt serverless compute (Cloud Run, Cloud Functions) for workloads with intermittent, event-driven traffic profiles to scale to zero."
        ]
      },
      {
        title: "Commitment & Discount Strategies",
        description: "Leverage pricing models based on predictable compute needs and volume contracts.",
        recommendations: [
          "Purchase Committed Use Discounts (CUDs) for predictable baseline compute workloads (vCPUs/RAM).",
          "Use flexible CUDs to cover workloads spanning multiple machine types or regions.",
          "Take advantage of Sustained Use Discounts (SUDs) for workloads running continuously on Compute Engine."
        ]
      },
      {
        title: "Storage Lifecycle Management",
        description: "Minimize data storage costs by mapping storage classes to retrieval frequencies.",
        recommendations: [
          "Set Object Lifecycle Management policies on Cloud Storage buckets to transition data from Standard to Nearline, Coldline, or Archive.",
          "Delete outdated backups, temporary build artifacts, and expired database snapshots.",
          "Analyze query costs in BigQuery using flat-rate reservations or edition-based pricing models instead of on-demand queries."
        ]
      }
    ],
    examInsights: [
      "Serverless pricing: If a workload runs for only 5 minutes a day, do not deploy it on a dedicated Compute Engine VM; run it on Cloud Run or Cloud Functions.",
      "BigQuery Cost Control: Set maximum bytes billed limits on queries to prevent runaway costs from massive table scans. Use partitioned/clustered tables.",
      "CUD vs Spot VMs: Use Committed Use Discounts for predictable, critical production workloads. Use Spot VMs (preemptible) for batch processing, rendering, and testing where workloads can be interrupted."
    ],
    sharedFate: {
      google: [
        "Offers clear, transparent billing dashboards and API exports.",
        "Applies automatic discounts (SUDs) where applicable.",
        "Provides recommender APIs (Active Assist) to identify cost-saving opportunities."
      ],
      customer: [
        "Monitors billing alerts and exports billing data to BigQuery for visual reporting in Looker Studio.",
        "Approves and applies right-sizing recommendations.",
        "Configures lifecycle rules for storage and purchases CUD agreements."
      ]
    }
  },
  {
    id: "performance-optimization",
    title: "Performance Optimization",
    color: "indigo",
    description: "Design and tune your cloud resources for optimal speed, network latency, and compute efficiency.",
    focusAreas: [
      {
        title: "Elasticity & Resource Matching",
        description: "Select hardware configurations matched to the specific resource profiles of applications.",
        recommendations: [
          "Match machine families (General-purpose, Compute-optimized, Memory-optimized, Storage-optimized) to workload bottlenecks (CPU, RAM, or IOPS).",
          "Deploy GPU- or TPU-accelerated machine types (A3, G2) for high-performance AI, ML, and scientific computing.",
          "Optimize network performance by selecting the Premium Network Tier for low-latency, global Google fiber routing."
        ]
      },
      {
        title: "Network Latency & Caching",
        description: "Store content closer to end-users and minimize network transit distances.",
        recommendations: [
          "Use Cloud CDN to cache static assets, web assets, and images closer to end-users at Google edge nodes.",
          "Deploy regional load balancers and place compute instances in geographic regions closest to your primary user base.",
          "Enforce private VPC connectivity (Private Google Access) to eliminate public internet routing overhead for internal traffic."
        ]
      },
      {
        title: "Modular Design & Code Tuning",
        description: "Develop applications that utilize hardware threads, network buffers, and memory efficiently.",
        recommendations: [
          "Optimize database performance using Memorystore (Redis/Memcached) for high-speed read caching.",
          "Perform index tuning and query optimization for relational (Cloud SQL) and NoSQL (Bigtable, Firestore) databases.",
          "Implement lazy loading, compression, and minimized asset bundles on frontends."
        ]
      }
    ],
    examInsights: [
      "Network Tiers: Premium Tier routes traffic entirely within Google's private global fiber network (best performance). Standard Tier routes traffic over the public internet (lower cost).",
      "Low Latency NoSQL: For real-time applications with sub-10ms latency requirements at massive scale (e.g., IoT ingestion, ad-tech, financial tickers), choose Cloud Bigtable.",
      "Database caching: Reduce database read contention by implementing a caching layer using Memorystore."
    ],
    sharedFate: {
      google: [
        "Maintains low-latency global network infrastructure and high-performance physical servers.",
        "Provides specialized hardware accelerators (TPUs, latest GPUs).",
        "Optimizes managed database engines for optimal speed and reliability."
      ],
      customer: [
        "Selects appropriate machine types and configures autoscaling limits.",
        "Writes efficient database queries, designs proper schemas, and configures database indexes.",
        "Configures CDN caching rules, HTTP/3 protocols, and optimizes frontend assets."
      ]
    }
  },
  {
    id: "sustainability",
    title: "Sustainability",
    color: "green",
    description: "Build and manage cloud workloads that minimize environmental impact, reduce energy consumption, and optimize carbon efficiency.",
    focusAreas: [
      {
        title: "Low-Carbon Regional Placement",
        description: "Choose cloud regions powered by a high percentage of clean energy grids.",
        recommendations: [
          "Store data and run compute workloads in Google Cloud regions with high Carbon-Free Energy (CFE%) values.",
          "Restrict resource creation to green regions by enforcing Resource Location constraints in Organization Policy.",
          "Implement geographical shifting to run compute-heavy tasks in regions with the lowest carbon footprint."
        ]
      },
      {
        title: "Resource Efficiency & Containers",
        description: "Maximize utilization of hardware resources to prevent energy waste on idle infrastructure.",
        recommendations: [
          "Deploy containerized applications on GKE or Cloud Run to optimize resource packing (bin packing) and scaling.",
          "Leverage Cloud Run's scale-to-zero capability to eliminate energy consumption during periods of zero traffic.",
          "Upgrade to the latest VM machine families (e.g., C4, C4A with Google Axion Arm processors) which offer up to 60% higher energy efficiency."
        ]
      },
      {
        title: "Software & Data Optimization",
        description: "Write lean code and minimize data footprint to reduce storage and processing energy costs.",
        recommendations: [
          "Minimize network payloads and round-trips by choosing binary protocols, HTTP/3, and gzip/brotli compression.",
          "Configure Object Lifecycle Management to archive or delete stale data, reducing persistent disk spinning energy.",
          "Identify and purge dark/shadow datasets using Dataplex Data Catalog scans."
        ]
      },
      {
        title: "Measure & Improve (GreenOps)",
        description: "Integrate carbon reporting into the operational feedback loop.",
        recommendations: [
          "Assign the Carbon Footprint Viewer role to FinOps and engineering teams to track emissions over time.",
          "Export Carbon Footprint datasets to BigQuery to run advanced SQL analytics correlating cost with carbon impact.",
          "Regularly review the Unattended Project Recommender to identify and delete orphan or idle projects."
        ]
      }
    ],
    examInsights: [
      "Arm Processors: Google Axion processors (Arm-based) are highly sustainable, offering significantly higher energy efficiency per unit of performance compared to x86.",
      "Disaster Recovery Carbon: Avoid hot-standby (active-passive) architectures where secondary resources spin idle. Use cold standby failovers or serverless endpoints (Cloud Run) that consume zero energy until triggered.",
      "Green Computing Strategy: Temporal shifting - scheduling batch analytics or machine learning training jobs to run when grid carbon intensity is lowest."
    ],
    sharedFate: {
      google: [
        "Offsets 100% of global electricity consumption with renewable energy purchases.",
        "Designs highly efficient data centers with average PUE (Power Usage Effectiveness) ratings under 1.10.",
        "Provides the Carbon Footprint tool for client emissions reporting."
      ],
      customer: [
        "Selects low-carbon regions for storage buckets and compute resources.",
        "Configures autoscaling and scale-to-zero triggers to minimize idle computing.",
        "Maintains data hygiene, deletes dark data, and optimizes application code."
      ]
    }
  }
];

export const crossPillars: CrossPillar[] = [
  {
    id: "ai-ml",
    title: "AI and Machine Learning Workloads",
    description: "Technology-specific architectural guidance for building secure, scalable, and sustainable AI applications on Google Cloud.",
    insights: [
      "**Compute Optimization**: Select GPUs (e.g., NVIDIA H100/L4) or TPUs (Tensor Processing Units) for deep learning training. TPUs are custom-built for tensor operations and offer much higher energy efficiency (performance-per-watt) than general-purpose CPUs.",
      "**Data Ingestion & Pipelines**: Store raw training datasets in regional Cloud Storage buckets. Use Dataproc (Spark) or Dataflow (Beam) to run preprocessing pipelines in the same region as the storage buckets to avoid high network egress fees and latency.",
      "**Security & Privacy**: Enforce VPC Service Controls around Vertex AI APIs to prevent data exfiltration during training. Mask or encrypt PII inside training datasets. Deploy AI models securely behind Identity-Aware Proxy (IAP) endpoints.",
      "**Cost Control**: Use Vertex AI training custom jobs with auto-termination rules. Use Spot VMs for model training workflows that can survive worker preemption. Leverage Gemini API caching to reduce token consumption and latency for repetitive prompts."
    ]
  },
  {
    id: "financial-services",
    title: "Financial Services (FS) & Regulated Sectors",
    description: "Architectural rules for highly regulated systems requiring strict data sovereignty, audit trails, and multi-region resilience.",
    insights: [
      "**Data Residency & Sovereignty**: Use Organization Policies to restrict storage locations to specific countries or states. Enforce Customer-Managed Encryption Keys (CMEK) with Cloud HSM (Hardware Security Module) to ensure keys are stored in FIPS 140-2 Level 3 validated physical security modules.",
      "**Auditability & Compliance**: Enable Cloud Audit Logs (Admin Activity, System Event, Data Access) across all projects. Export logs to a locked, centralized BigQuery dataset or Cloud Storage bucket using Log Sinks with Object Retention locks to prevent modification.",
      "**Ultra-High Availability**: Design active-active multi-region databases using Cloud Spanner to satisfy regulatory requirements for regional disaster recovery (RTO near zero, RPO zero). Build cross-region traffic failover using Global HTTP(S) Load Balancing with Cloud DNS routing policies."
    ]
  }
];

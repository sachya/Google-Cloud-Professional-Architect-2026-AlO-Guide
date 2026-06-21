# 🔄 Agent Instructions: GCP Professional Cloud Architect (PCA) Update Pipeline

This document is a comprehensive system prompt and instruction guide for an AI agent to execute updates on the **GCP Architect Hub** study materials, service sheets, and practice exam simulator. Follow this step-by-step checklist to ensure the content remains accurate, modern, and aligned with the official Google Cloud Professional Cloud Architect (PCA) certification.

---

## 🎯 Objective
Update the core databases and practice questions of the GCP Architect Hub without changing any UI elements. Ensure all updates reflect the latest Google Cloud product names, feature improvements, deprecations, and PCA exam specifications.

---

## 📅 Step 1: Audit Exam Guide and Case Studies
Locate and review the latest version of the official Google Cloud Professional Cloud Architect Exam Guide and its case studies.

1. **Locate the Latest Exam Guide**:
   - Check the official [Google Cloud Professional Cloud Architect Certification Page](https://cloud.google.com/learn/certification/guides/professional-cloud-architect).
   - Compare the current certification requirements with the existing [exam guide PDF](professional_cloud_architect_exam_guide_english.pdf) in the workspace.
2. **Review the Four Case Studies**:
   - Verify if the current case studies (**Altostrat Media**, **Cymbal Retail**, **EHR Healthcare**, and **KnightMotives Automotive**) are still active.
   - If any case study has been updated or replaced by Google, modify the corresponding entry in the JSON file at [src/lib/data/casestudies.json](src/lib/data/casestudies.json).
   - Maintain the existing keys (`id`, `name`, `industry`, `overview`, `concept`, `existingEnv`, `businessRequirements`, `technicalRequirements`, `proposedArchitecture`, `examTips`).
   - If updates are made to the case studies, make sure to update the bidirectionally linked GCP service IDs in `gcpServices`.

---

## 📦 Step 2: Audit Google Cloud Products & Services
Audit the 191 GCP offerings cataloged in the repository for rebranding, deprecations, or newly launched services.

1. **Identify Deprecations and Rebrands**:
   - Cross-reference the service listings in [src/lib/data/services.json](src/lib/data/services.json) against the official [Google Cloud Products and Services List](https://cloud.google.com/products).
   - If a service has been deprecated (e.g., *Cloud IoT Core*), add a warning prefix to its description: `"[DEPRECATED] ..."` and ensure its key exam points discuss migration paths to modern alternatives (e.g., Pub/Sub with edge buffering).
   - Update services that have been rebranded or consolidated.
2. **Inject Modern Architectural Best Practices**:
   - Focus on modern services and features like **AlloyDB**, **Spanner Graph**, **Vertex AI (Gemini, Imagen, Agent Builder)**, **Cross-Cloud Interconnect**, **Privileged Access Manager (PAM)**, and **BigQuery Editions**.
   - Ensure the template and override files under [src/lib/data/templates/](src/lib/data/templates/) are updated to match these technologies.
3. **Run the Data Pipeline**:
   - After updating [src/lib/data/services.json](src/lib/data/services.json) or templates, compile the final deep-dive sheets by running:
     ```powershell
     python enrich_all.py
     python enrich_details_advanced.py
     ```
   - Verify that individual service JSON files are generated/updated under [src/lib/data/details/](src/lib/data/details/).

---

## 📝 Step 3: Refresh 20% of Practice Exam Questions
Update exactly **20% of the questions** in [src/lib/data/practice_questions.json](src/lib/data/practice_questions.json). Since the database contains 5 sets of 90 questions (450 total), you must rewrite or refresh **90 questions** (18 questions per set).

### 🔍 Guidelines for Writing Tricky, Realistic PCA-Style Questions
The real PCA exam focuses heavily on decision-making, trade-offs, and architectural design patterns. Simple recall questions must be avoided. Use the following principles when drafting the new/updated questions:

#### 1. Scenario-Based Structure
Questions should describe a client's specific business state, legacy constraints, and technical requirements. Make sure to:
* Mention the client's current setup (e.g., "A legacy transaction system running on-premises on SQL Server...").
* Incorporate business constraints (e.g., "minimize hardware lead time", "RPO of zero and RTO of under 2 minutes", "strict compliance with GDPR", or "tight budget constraints").
* End with a clear objective (e.g., "Which strategy guarantees performance while optimizing costs?").

#### 2. Realistic Distractors (The "Tricky" Element)
Distractors should not be obviously wrong. They should look technically plausible but violate a constraint or represent a bad practice:
* **The "Deprecated Service" Trap**: Offering *Cloud IoT Core* for device management instead of using Pub/Sub + Cloud Run edge gateways.
* **The "Cost-Inefficient CUD" Trap**: Purchasing Committed Use Discounts (CUDs) for a batch job that runs only 48 hours once a month (on-demand compute is cheaper here).
* **The "Broad Access" Trap**: Granting persistent `roles/editor` or using static Service Account JSON keys instead of dynamic Service Account attachments, Workload Identity, or Privileged Access Manager (PAM).
* **The "Insecure Ingress/Egress" Trap**: Assigning external IP addresses to private GKE nodes instead of using Private Google Access, Cloud NAT, and Identity-Aware Proxy (IAP) tunnels.
* **The "Incorrect Database" Trap**: Selecting standard Cloud SQL for a multi-region database that requires horizontal write-scalability (which requires Cloud Spanner).

#### 3. Core Architectural Focus Areas
Ensure the refreshed questions are distributed across the official PCA exam categories:
* **Section 1: Designing and planning a cloud solution architecture** (Focus: Case studies mapping, capacity planning, global load balancing, Hybrid/Multi-cloud connectivity).
* **Section 2: Managing and provisioning a cloud solution infrastructure** (Focus: Terraform deployment, GKE Fleet configurations, Datastream CDC setups, Spanner schema optimization to prevent write hotspots).
* **Section 3: Designing for security and compliance** (Focus: VPC Service Controls, Sensitive Data Protection for PII redaction, Binary Authorization, Customer-Managed/External Key Management).
* **Section 4: Analyzing and optimizing technical and business processes** (Focus: Well-Architected Cost Optimization, SRE monitoring/alert fatigue mitigation using SLOs/Error Budgets).
* **Section 5: Managing implementation** (Focus: Cloud Build private pools, API gateway proxy decoupling with Apigee, progressive delivery with canary rollouts).
* **Section 6: Ensuring solution and operations reliability** (Focus: DR topologies, synchronous regional HA replication, circuit breakers, graceful degradation patterns).

### 🛠️ Schema Compliance
Every question object must strictly adhere to the following schema:
```json
{
  "id": "q-[set_number]-[question_number]", // e.g., "q-3-15"
  "type": "single" | "multi",               // "single" for one correct choice, "multi" for select 2 or more
  "category": "Section [Number]: [Category Name]",
  "question": "Scenario text. What architectural solution meets these exact requirements?",
  "options": [
    "Plausible Option A (Distractor)",
    "Plausible Option B (Correct Answer)",
    "Plausible Option C (Distractor)",
    "Plausible Option D (Distractor)"
  ],
  "answer": [1], // Array of 0-based indices of the correct options. For "multi", e.g., [0, 2]
  "explanation": "Deep dive into why Option B is correct based on the Well-Architected Framework, and why Options A, C, and D are incorrect or violate constraints."
}
```

---

## 🚦 Step 4: Verification and Quality Assurance
After implementing the updates, run the following verification checks:

1. **Verify JSON Format**:
   - Ensure [src/lib/data/practice_questions.json](src/lib/data/practice_questions.json) and [src/lib/data/casestudies.json](src/lib/data/casestudies.json) are valid JSON. Check for trailing commas or syntax errors using a linter or python:
     ```powershell
     python -m json.tool src/lib/data/practice_questions.json > $null
     ```
2. **Re-run the Enrichment Pipelines**:
   - Ensure the scripts execute without throwing exceptions.
3. **Verify Typescript and Application Build**:
   - Build the SvelteKit application locally to ensure there are no compilation or typing issues:
     ```powershell
     npm run build
     ```
4. **Test the Simulator Locally**:
   - Start the local dev server and navigate to the Practice Exam Simulator page to make sure the refreshed questions load and shuffle correctly:
     ```powershell
     npm run dev
     ```

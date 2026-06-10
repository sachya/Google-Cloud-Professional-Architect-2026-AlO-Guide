<div class="max-w-4xl mx-auto space-y-10">
  <div>
    <h1 class="text-3xl font-extrabold text-slate-900 dark:text-white mb-4">Google Cloud Well-Architected Framework</h1>
    <p class="text-lg text-slate-600 dark:text-slate-300">
      The Google Cloud Architecture Framework provides recommendations and best practices to help architects, developers, administrators, and other cloud practitioners design and operate a cloud topology that is secure, efficient, resilient, high-performing, and cost-effective.
    </p>
  </div>

  <div class="space-y-6">
    <!-- Operational Excellence -->
    <div class="bg-white dark:bg-slate-800 p-6 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm">
      <h2 class="text-xl font-bold text-blue-600 dark:text-blue-400 mb-3 flex items-center gap-2">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
        Operational Excellence
      </h2>
      <p class="text-slate-600 dark:text-slate-400 mb-4">Focuses on running, managing, and monitoring systems to deliver business value and continuously improving processes and procedures.</p>
      <ul class="list-disc list-inside text-sm text-slate-700 dark:text-slate-300 space-y-1">
        <li>Automate deployments and infrastructure provisioning (IaC, CI/CD).</li>
        <li>Implement comprehensive monitoring, logging, and alerting (Cloud Monitoring, Logging).</li>
        <li>Establish robust incident management and blameless post-mortem cultures.</li>
        <li>Perform capacity planning and scale systems dynamically.</li>
      </ul>
    </div>

    <!-- Security, Privacy, and Compliance -->
    <div class="bg-white dark:bg-slate-800 p-6 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm">
      <h2 class="text-xl font-bold text-blue-600 dark:text-blue-400 mb-3 flex items-center gap-2">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
        Security, Privacy, and Compliance
      </h2>
      <p class="text-slate-600 dark:text-slate-400 mb-4">Focuses on protecting information, systems, and assets while delivering business value through risk assessments and mitigation strategies.</p>
      <ul class="list-disc list-inside text-sm text-slate-700 dark:text-slate-300 space-y-1">
        <li>Apply defense-in-depth and principle of least privilege (IAM, VPC Service Controls).</li>
        <li>Protect data in transit and at rest using encryption (CMEK, Cloud KMS).</li>
        <li>Ensure compliance and manage vulnerabilities (Security Command Center).</li>
        <li>Adopt a zero-trust architecture (BeyondCorp Enterprise).</li>
      </ul>
    </div>

    <!-- Reliability -->
    <div class="bg-white dark:bg-slate-800 p-6 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm">
      <h2 class="text-xl font-bold text-blue-600 dark:text-blue-400 mb-3 flex items-center gap-2">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path></svg>
        Reliability
      </h2>
      <p class="text-slate-600 dark:text-slate-400 mb-4">Ensures a workload performs its intended function correctly and consistently when expected to.</p>
      <ul class="list-disc list-inside text-sm text-slate-700 dark:text-slate-300 space-y-1">
        <li>Design for high availability and fault tolerance (multi-region, multi-zone deployments).</li>
        <li>Implement automated disaster recovery and backup strategies (Cloud Storage, persistent disks).</li>
        <li>Establish Service Level Objectives (SLOs) and Error Budgets.</li>
        <li>Mitigate impact of localized failures using resilient architecture (load balancing, retries).</li>
      </ul>
    </div>

    <!-- Performance Optimization -->
    <div class="bg-white dark:bg-slate-800 p-6 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm">
      <h2 class="text-xl font-bold text-blue-600 dark:text-blue-400 mb-3 flex items-center gap-2">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
        Performance Optimization
      </h2>
      <p class="text-slate-600 dark:text-slate-400 mb-4">Focuses on using IT and computing resources efficiently to meet system requirements and to maintain efficiency as demand changes and technologies evolve.</p>
      <ul class="list-disc list-inside text-sm text-slate-700 dark:text-slate-300 space-y-1">
        <li>Select the right compute, storage, and database services based on workload profiles.</li>
        <li>Implement autoscaling to handle dynamic workloads (Managed Instance Groups, GKE Autoscaling).</li>
        <li>Optimize network latency and throughput (Cloud CDN, Premium Network Tier).</li>
        <li>Use caching and database indexing strategies (Memorystore).</li>
      </ul>
    </div>

    <!-- Cost Optimization -->
    <div class="bg-white dark:bg-slate-800 p-6 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm">
      <h2 class="text-xl font-bold text-blue-600 dark:text-blue-400 mb-3 flex items-center gap-2">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        Cost Optimization
      </h2>
      <p class="text-slate-600 dark:text-slate-400 mb-4">Focuses on avoiding unnecessary costs and maximizing business value through continuous monitoring and rightsizing.</p>
      <ul class="list-disc list-inside text-sm text-slate-700 dark:text-slate-300 space-y-1">
        <li>Leverage Committed Use Discounts (CUDs) and Sustained Use Discounts (SUDs).</li>
        <li>Implement billing alerts and export data to BigQuery for cost analysis.</li>
        <li>Rightsize resources and identify idle assets (Active Assist recommendations).</li>
        <li>Use cost-effective storage classes and lifecycle management.</li>
      </ul>
    </div>
  </div>
</div>

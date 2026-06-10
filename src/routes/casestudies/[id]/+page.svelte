<script lang="ts">
  let { data } = $props();
  let cs = $derived(data.casestudy);

  // Tab state: 'business' or 'technical'
  let activeTab = $state('business');

  // Service ID to Human-readable Name map for badges
  const serviceNameMap: Record<string, string> = {
    'compute-engine': 'Compute Engine',
    'google-kubernetes-engine--gke-': 'Google Kubernetes Engine (GKE)',
    'cloud-run': 'Cloud Run',
    'cloud-run-functions': 'Cloud Run functions',
    'cloud-storage': 'Cloud Storage',
    'cloud-sql': 'Cloud SQL',
    'spanner': 'Cloud Spanner',
    'alloydb-for-postgresql': 'AlloyDB',
    'bigtable': 'Cloud Bigtable',
    'memorystore-for-redis-cluster': 'Memorystore',
    'virtual-private-cloud--vpc-': 'VPC Network',
    'cloud-load-balancing': 'Cloud Load Balancing',
    'cloud-cdn': 'Cloud CDN',
    'cloud-interconnect': 'Cloud Interconnect',
    'cloud-vpn': 'Cloud VPN',
    'cloud-router': 'Cloud Router',
    'cloud-nat': 'Cloud NAT',
    'google-cloud-armor': 'Cloud Armor',
    'vpc-service-controls': 'VPC Service Controls',
    'identity-and-access-management': 'IAM',
    'cloud-key-management-service': 'Cloud KMS',
    'secret-manager': 'Secret Manager',
    'cloud-logging': 'Cloud Logging',
    'cloud-monitoring': 'Cloud Monitoring',
    'cloud-build': 'Cloud Build',
    'cloud-deploy': 'Cloud Deploy',
    'artifact-registry': 'Artifact Registry',
    'storage-transfer-service': 'Storage Transfer Service',
    'dialogflow-cx': 'Dialogflow CX',
    'vertex-ai': 'Vertex AI',
    'model-armor': 'Model Armor',
    'speech-to-text': 'Speech-to-Text',
    'cloud-vision-api': 'Cloud Vision API',
    'apigee-api-management': 'Apigee API Management',
    'api-gateway': 'API Gateway',
    'infrastructure-manager': 'Infrastructure Manager',
    'container-optimized-os': 'Container-Optimized OS',
    'bare-metal-solution': 'Bare Metal Solution',
    'colab-enterprise': 'Colab Enterprise',
    'data-pipelines-streaming': 'Dataflow / Pub/Sub'
  };

  const gradients: Record<string, string> = {
    'altostrat-media': 'from-blue-600 to-indigo-600',
    'cymbal-retail': 'from-purple-600 to-pink-600',
    'ehr-healthcare': 'from-emerald-600 to-teal-600',
    'knightmotives-automotive': 'from-amber-500 to-orange-600'
  };

  const borderColors: Record<string, string> = {
    'altostrat-media': 'border-blue-500',
    'cymbal-retail': 'border-purple-500',
    'ehr-healthcare': 'border-emerald-500',
    'knightmotives-automotive': 'border-amber-500'
  };
</script>

<svelte:head>
  <title>{cs.name} Case Study | GCP Architect Hub</title>
</svelte:head>

<div class="max-w-5xl mx-auto space-y-10 pb-16">
  <!-- Header Banner -->
  <div class="bg-white dark:bg-slate-800 rounded-3xl border border-slate-200 dark:border-slate-700 shadow-sm overflow-hidden relative">
    <div class="h-4 bg-gradient-to-r {gradients[cs.id]}"></div>
    <div class="p-8 md:p-10 space-y-4">
      <div class="flex flex-wrap items-center gap-2">
        <span class="px-3 py-1 bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-350 text-xs font-semibold rounded-full uppercase tracking-wider">
          {cs.industry}
        </span>
        <span class="px-3 py-1 bg-indigo-50 dark:bg-indigo-950/40 text-indigo-600 dark:text-indigo-400 text-xs font-semibold rounded-full uppercase tracking-wider border border-indigo-150 dark:border-indigo-900">
          Case Study
        </span>
      </div>
      <h1 class="text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">{cs.name}</h1>
      <p class="text-lg text-slate-700 dark:text-slate-300 leading-relaxed font-normal">
        {cs.overview}
      </p>
    </div>
  </div>

  <!-- Solution Concept & Environment -->
  <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
    <!-- Concept -->
    <div class="bg-white dark:bg-slate-800 p-6 md:p-8 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm space-y-4">
      <h2 class="text-xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
        <svg class="h-5 w-5 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
        </svg>
        Solution Concept
      </h2>
      <p class="text-sm text-slate-650 dark:text-slate-350 leading-relaxed">
        {cs.concept}
      </p>
    </div>

    <!-- Existing Environment -->
    <div class="bg-white dark:bg-slate-800 p-6 md:p-8 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm space-y-4">
      <h2 class="text-xl font-bold text-slate-900 dark:text-white flex items-center gap-2">
        <svg class="h-5 w-5 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
        </svg>
        Existing Technical Environment
      </h2>
      <ul class="space-y-2.5 text-sm text-slate-650 dark:text-slate-350">
        {#each cs.existingEnv as env}
          <li class="flex items-start gap-2">
            <span class="h-1.5 w-1.5 rounded-full bg-slate-400 dark:bg-slate-500 mt-2 flex-shrink-0"></span>
            <span>{env}</span>
          </li>
        {/each}
      </ul>
    </div>
  </div>

  <!-- Requirements-to-Solutions Mappings -->
  <div class="space-y-6">
    <div class="flex flex-col md:flex-row md:items-center justify-between border-b border-slate-200 dark:border-slate-700 pb-4 gap-4">
      <h2 class="text-2xl font-bold text-slate-900 dark:text-white">Requirements & Mappings</h2>
      
      <!-- Tabs -->
      <div class="flex p-1 bg-slate-100 dark:bg-slate-800 rounded-lg self-start">
        <button 
          onclick={() => activeTab = 'business'}
          class="px-4 py-1.5 rounded-md text-xs font-semibold transition-all {activeTab === 'business' ? 'bg-white dark:bg-slate-700 text-indigo-600 dark:text-indigo-400 shadow-sm' : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'}"
        >
          Business Requirements
        </button>
        <button 
          onclick={() => activeTab = 'technical'}
          class="px-4 py-1.5 rounded-md text-xs font-semibold transition-all {activeTab === 'technical' ? 'bg-white dark:bg-slate-700 text-indigo-600 dark:text-indigo-400 shadow-sm' : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-200'}"
        >
          Technical Requirements
        </button>
      </div>
    </div>

    <!-- Requirements Cards -->
    <div class="space-y-4">
      {#if activeTab === 'business'}
        {#each cs.businessRequirements as item}
          <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 p-6 hover:shadow-sm transition-shadow relative overflow-hidden flex flex-col md:flex-row gap-6">
            <div class="absolute top-0 left-0 w-1 h-full bg-indigo-500"></div>
            <!-- Requirement Column -->
            <div class="md:w-5/12 space-y-2">
              <span class="inline-block text-[11px] font-bold tracking-wider text-slate-400 uppercase">Requirement {item.id}</span>
              <p class="font-bold text-slate-850 dark:text-slate-100 text-base leading-snug">{item.req}</p>
            </div>
            <!-- Solution Column -->
            <div class="flex-1 space-y-3">
              <span class="inline-block text-[11px] font-bold tracking-wider text-indigo-500 uppercase">GCP Architecture Solution</span>
              <p class="text-sm text-slate-650 dark:text-slate-300 leading-relaxed">{item.solution}</p>
              
              <!-- Badges -->
              <div class="flex flex-wrap gap-1.5 pt-1">
                {#each item.gcpServices as svcId}
                  <a 
                    href={`/services/${svcId}`}
                    class="px-2 py-0.5 bg-slate-100 hover:bg-indigo-50 dark:bg-slate-700/60 dark:hover:bg-slate-700 text-slate-600 hover:text-indigo-600 dark:text-slate-300 rounded-md text-[11px] font-medium border border-slate-200 dark:border-slate-700 transition-colors"
                  >
                    {serviceNameMap[svcId] || svcId}
                  </a>
                {/each}
              </div>
            </div>
          </div>
        {/each}
      {:else}
        {#each cs.technicalRequirements as item}
          <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 p-6 hover:shadow-sm transition-shadow relative overflow-hidden flex flex-col md:flex-row gap-6">
            <div class="absolute top-0 left-0 w-1 h-full bg-teal-500"></div>
            <!-- Requirement Column -->
            <div class="md:w-5/12 space-y-2">
              <span class="inline-block text-[11px] font-bold tracking-wider text-slate-400 uppercase">Requirement {item.id}</span>
              <p class="font-bold text-slate-850 dark:text-slate-100 text-base leading-snug">{item.req}</p>
            </div>
            <!-- Solution Column -->
            <div class="flex-1 space-y-3">
              <span class="inline-block text-[11px] font-bold tracking-wider text-teal-500 dark:text-teal-400 uppercase">GCP Architecture Solution</span>
              <p class="text-sm text-slate-650 dark:text-slate-300 leading-relaxed">{item.solution}</p>
              
              <!-- Badges -->
              <div class="flex flex-wrap gap-1.5 pt-1">
                {#each item.gcpServices as svcId}
                  <a 
                    href={`/services/${svcId}`}
                    class="px-2 py-0.5 bg-slate-100 hover:bg-teal-50 dark:bg-slate-700/60 dark:hover:bg-slate-700 text-slate-600 hover:text-teal-600 dark:text-slate-300 rounded-md text-[11px] font-medium border border-slate-200 dark:border-slate-700 transition-colors"
                  >
                    {serviceNameMap[svcId] || svcId}
                  </a>
                {/each}
              </div>
            </div>
          </div>
        {/each}
      {/if}
    </div>
  </div>

  <!-- Proposed Target Architecture -->
  <div class="bg-white dark:bg-slate-800 p-8 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm relative overflow-hidden">
    <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500 to-teal-500"></div>
    <h2 class="text-2xl font-bold text-slate-900 dark:text-white mb-4 flex items-center gap-2">
      <svg class="h-6 w-6 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
      </svg>
      Target Cloud Architecture
    </h2>
    <p class="text-sm text-slate-650 dark:text-slate-300 leading-relaxed">
      {cs.proposedArchitecture}
    </p>
  </div>

  <!-- Exam Cheat Sheet -->
  <div class="bg-indigo-50/50 dark:bg-indigo-950/20 p-8 rounded-3xl border border-indigo-100 dark:border-indigo-900/60 space-y-4">
    <h2 class="text-xl font-bold text-indigo-900 dark:text-indigo-300 flex items-center gap-2">
      <svg class="h-5.5 w-5.5 text-indigo-600 dark:text-indigo-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
      </svg>
      Exam Cheat Sheet & Focus Areas
    </h2>
    <ul class="space-y-3 text-sm text-indigo-850 dark:text-slate-300">
      {#each cs.examTips as tip}
        <li class="flex items-start gap-2.5">
          <svg class="h-5 w-5 text-indigo-500 dark:text-indigo-400 mt-0.5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <span>{tip}</span>
        </li>
      {/each}
    </ul>
  </div>
</div>

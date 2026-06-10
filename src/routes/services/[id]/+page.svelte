<script lang="ts">
  let { data } = $props();
  let service = $derived(data.service);
  
  // Since we haven't generated the deep insights for every single service yet, 
  // we will display a placeholder block if features/cliExamples are empty.
  let hasDeepInsights = $derived(
    (service.keyPoints?.design?.length > 0) ||
    (service.features?.length > 0) || 
    (service.iamRoles?.length > 0) || 
    (service.cliExamples?.length > 0)
  );
</script>

<svelte:head>
  <title>{service.name} | GCP Architect Hub</title>
</svelte:head>

<div class="max-w-5xl mx-auto space-y-10 pb-16">
  <!-- Header -->
  <div class="bg-white dark:bg-slate-800 p-8 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm relative overflow-hidden">
    <div class="absolute top-0 left-0 w-2.5 h-full bg-gradient-to-b from-blue-600 to-indigo-500"></div>
    <div class="flex flex-col md:flex-row md:items-start justify-between gap-4">
      <div>
        <h1 class="text-3xl font-extrabold text-slate-900 dark:text-white mb-2 tracking-tight">{service.name}</h1>
        <div class="flex flex-wrap items-center gap-2 mb-4">
          <span class="px-3 py-1 bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 text-xs font-semibold rounded-full border border-blue-200 dark:border-blue-800">
            {service.category}
          </span>
          {#if service.architecturalCategory}
            <span class="px-3 py-1 bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 text-xs font-medium rounded-full border border-slate-200 dark:border-slate-600">
              {service.architecturalCategory}
            </span>
          {/if}
        </div>
        <p class="text-lg text-slate-700 dark:text-slate-305 leading-relaxed font-normal">
          {service.description}
        </p>
      </div>
    </div>
  </div>

  {#if hasDeepInsights}
    <!-- GCP Professional Architect Exam Guide Key Points -->
    {#if service.keyPoints && (service.keyPoints.design?.length > 0 || service.keyPoints.security?.length > 0 || service.keyPoints.reliability?.length > 0 || service.keyPoints.cost?.length > 0)}
      <div class="space-y-6">
        <div class="flex items-center gap-2">
          <svg class="w-6 h-6 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
          </svg>
          <h2 class="text-2xl font-bold text-slate-900 dark:text-white">GCP Architect Exam Guide (30-40 Key Points)</h2>
        </div>
        
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <!-- Pillar 1: Solution Design -->
          <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm relative overflow-hidden flex flex-col hover:shadow-md transition-shadow">
            <div class="absolute top-0 left-0 right-0 h-[3px] bg-gradient-to-r from-blue-500 to-indigo-500"></div>
            <h3 class="text-base font-bold text-slate-800 dark:text-slate-100 flex items-center gap-2 mb-4">
              <span class="p-1.5 bg-blue-50 dark:bg-blue-900/40 text-blue-600 dark:text-blue-400 rounded-lg">
                <svg class="h-4.5 w-4.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
                </svg>
              </span>
              Solution Design & Architecture
            </h3>
            <ul class="space-y-3 flex-1 text-sm text-slate-600 dark:text-slate-300">
              {#each service.keyPoints.design || [] as pt}
                <li class="flex items-start gap-2.5">
                  <span class="h-1.5 w-1.5 rounded-full bg-blue-500 mt-2 flex-shrink-0"></span>
                  <span>{pt}</span>
                </li>
              {/each}
            </ul>
          </div>

          <!-- Pillar 2: Security & Compliance -->
          <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm relative overflow-hidden flex flex-col hover:shadow-md transition-shadow">
            <div class="absolute top-0 left-0 right-0 h-[3px] bg-gradient-to-r from-purple-500 to-pink-500"></div>
            <h3 class="text-base font-bold text-slate-800 dark:text-slate-100 flex items-center gap-2 mb-4">
              <span class="p-1.5 bg-purple-50 dark:bg-purple-900/40 text-purple-600 dark:text-purple-400 rounded-lg">
                <svg class="h-4.5 w-4.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                </svg>
              </span>
              Security, IAM & Compliance
            </h3>
            <ul class="space-y-3 flex-1 text-sm text-slate-600 dark:text-slate-300">
              {#each service.keyPoints.security || [] as pt}
                <li class="flex items-start gap-2.5">
                  <span class="h-1.5 w-1.5 rounded-full bg-purple-500 mt-2 flex-shrink-0"></span>
                  <span>{pt}</span>
                </li>
              {/each}
            </ul>
          </div>

          <!-- Pillar 3: Reliability & High Availability -->
          <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm relative overflow-hidden flex flex-col hover:shadow-md transition-shadow">
            <div class="absolute top-0 left-0 right-0 h-[3px] bg-gradient-to-r from-emerald-500 to-green-500"></div>
            <h3 class="text-base font-bold text-slate-800 dark:text-slate-100 flex items-center gap-2 mb-4">
              <span class="p-1.5 bg-emerald-50 dark:bg-emerald-900/40 text-emerald-600 dark:text-emerald-400 rounded-lg">
                <svg class="h-4.5 w-4.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </span>
              Reliability & High Availability
            </h3>
            <ul class="space-y-3 flex-1 text-sm text-slate-600 dark:text-slate-300">
              {#each service.keyPoints.reliability || [] as pt}
                <li class="flex items-start gap-2.5">
                  <span class="h-1.5 w-1.5 rounded-full bg-emerald-500 mt-2 flex-shrink-0"></span>
                  <span>{pt}</span>
                </li>
              {/each}
            </ul>
          </div>

          <!-- Pillar 4: Cost & Performance -->
          <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm relative overflow-hidden flex flex-col hover:shadow-md transition-shadow">
            <div class="absolute top-0 left-0 right-0 h-[3px] bg-gradient-to-r from-amber-500 to-orange-500"></div>
            <h3 class="text-base font-bold text-slate-800 dark:text-slate-100 flex items-center gap-2 mb-4">
              <span class="p-1.5 bg-amber-50 dark:bg-amber-900/40 text-amber-600 dark:text-amber-400 rounded-lg">
                <svg class="h-4.5 w-4.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M12 16v1m-4-6h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </span>
              Cost & Performance Optimization
            </h3>
            <ul class="space-y-3 flex-1 text-sm text-slate-600 dark:text-slate-300">
              {#each service.keyPoints.cost || [] as pt}
                <li class="flex items-start gap-2.5">
                  <span class="h-1.5 w-1.5 rounded-full bg-amber-500 mt-2 flex-shrink-0"></span>
                  <span>{pt}</span>
                </li>
              {/each}
            </ul>
          </div>
        </div>
      </div>
    {/if}

    <!-- Features & Core Components -->
    {#if service.features?.length > 0}
      <div class="space-y-4">
        <h2 class="text-xl font-bold text-slate-900 dark:text-white border-b border-slate-200 dark:border-slate-700 pb-2">Key Features & Components</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          {#each service.features as feature}
            <div class="bg-white dark:bg-slate-800 p-5 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm">
              <h3 class="font-bold text-blue-600 dark:text-blue-400 mb-2">{feature.name}</h3>
              <p class="text-sm text-slate-600 dark:text-slate-400">{feature.description}</p>
            </div>
          {/each}
        </div>
      </div>
    {/if}

    <!-- IAM & Permissions -->
    {#if service.iamRoles?.length > 0}
      <div class="space-y-4">
        <h2 class="text-xl font-bold text-slate-900 dark:text-white border-b border-slate-200 dark:border-slate-700 pb-2">IAM & Security</h2>
        <div class="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 overflow-hidden shadow-sm">
          <table class="w-full text-left text-sm">
            <thead class="bg-slate-50 dark:bg-slate-900/50 border-b border-slate-200 dark:border-slate-700">
              <tr>
                <th class="px-6 py-3 font-semibold text-slate-700 dark:text-slate-300">Role</th>
                <th class="px-6 py-3 font-semibold text-slate-700 dark:text-slate-300">Description</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-200 dark:divide-slate-700">
              {#each service.iamRoles as role}
                <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50">
                  <td class="px-6 py-4 font-mono text-xs text-blue-600 dark:text-blue-400">{role.role}</td>
                  <td class="px-6 py-4 text-slate-600 dark:text-slate-400">{role.description}</td>
                </tr>
              {/each}
            </tbody>
          </table>
        </div>
      </div>
    {/if}

    <!-- CLI Examples -->
    {#if service.cliExamples?.length > 0}
      <div class="space-y-4">
        <h2 class="text-xl font-bold text-slate-900 dark:text-white border-b border-slate-200 dark:border-slate-700 pb-2">CLI & Operational Commands</h2>
        <div class="space-y-4">
          {#each service.cliExamples as cli}
            <div class="bg-slate-900 rounded-xl overflow-hidden shadow-sm">
              <div class="bg-slate-800 px-4 py-2 text-xs text-slate-400 font-medium border-b border-slate-700">
                {cli.description}
              </div>
              <div class="p-4 overflow-x-auto">
                <code class="text-sm font-mono text-green-400 whitespace-pre">{cli.command}</code>
              </div>
            </div>
          {/each}
        </div>
      </div>
    {/if}
  {:else}
    <!-- Placeholder for Missing Deep Insights -->
    <div class="bg-amber-50 dark:bg-amber-900/20 p-6 rounded-xl border border-amber-200 dark:border-amber-800/30 flex gap-4">
      <div class="text-amber-500 dark:text-amber-400">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
      </div>
      <div>
        <h3 class="font-bold text-amber-800 dark:text-amber-300 mb-1">Architectural Details Pending</h3>
        <p class="text-sm text-amber-700 dark:text-amber-400/80">
          The deep-dive insights (CUDs, IAM roles, architecture components, and gcloud commands) for this service are scheduled to be populated. The overarching structure accommodates vertical-specific data flexibly.
        </p>
      </div>
    </div>
  {/if}
</div>

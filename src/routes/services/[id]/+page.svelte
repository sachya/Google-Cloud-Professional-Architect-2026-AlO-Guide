<script lang="ts">
  let { data } = $props();
  let service = $derived(data.service);
  
  let hasDeepInsights = $derived(
    (service.keyPoints?.length > 0) ||
    (service.scenarios?.length > 0) || 
    (service.commands?.length > 0)
  );

  // Clipboard copy state tracking
  let copiedIndex = $state<number | null>(null);
  
  function copyCommand(text: string, index: number) {
    navigator.clipboard.writeText(text).then(() => {
      copiedIndex = index;
      setTimeout(() => {
        if (copiedIndex === index) {
          copiedIndex = null;
        }
      }, 2000);
    });
  }
</script>

<svelte:head>
  <title>{service.name} | GCP Architect Hub</title>
</svelte:head>

<div class="max-w-5xl mx-auto space-y-10 pb-16 px-4 md:px-0">
  <!-- Premium Service Header Card -->
  <div class="bg-white dark:bg-slate-800 p-6 md:p-8 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm relative overflow-hidden">
    <div class="absolute top-0 left-0 w-2.5 h-full bg-gradient-to-b from-blue-600 to-indigo-500"></div>
    <div class="flex flex-col gap-4">
      <div>
        <h1 class="text-3xl font-extrabold text-slate-900 dark:text-white mb-2 tracking-tight">{service.name}</h1>
        <div class="flex flex-wrap items-center gap-2 mb-4">
          <span class="px-3 py-1 bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 text-xs font-semibold rounded-full border border-blue-200 dark:border-blue-800">
            {service.category}
          </span>
          {#if service.architecturalCategory}
            <span class="px-3 py-1 bg-slate-100 dark:bg-slate-700/60 text-slate-600 dark:text-slate-300 text-xs font-medium rounded-full border border-slate-200 dark:border-slate-600">
              {service.architecturalCategory}
            </span>
          {/if}
        </div>
        <p class="text-base md:text-lg text-slate-700 dark:text-slate-300 leading-relaxed font-normal">
          {service.description}
        </p>
      </div>
    </div>
  </div>

  {#if hasDeepInsights}
    <!-- Section 1: Key Exam Points -->
    {#if service.keyPoints && service.keyPoints.length > 0}
      <div class="space-y-4">
        <div class="flex items-center gap-2.5">
          <span class="p-2 bg-indigo-50 dark:bg-indigo-900/30 text-indigo-600 dark:text-indigo-400 rounded-xl">
            <svg class="w-5.5 h-5.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
            </svg>
          </span>
          <h2 class="text-2xl font-bold text-slate-900 dark:text-white">GCP Architect Exam Key Points</h2>
        </div>
        
        <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 p-6 md:p-8 shadow-sm">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-4">
            {#each service.keyPoints as pt, i}
              <div class="flex items-start gap-3.5 group">
                <span class="mt-1 flex-shrink-0 flex items-center justify-center w-5 h-5 rounded-full bg-blue-50 dark:bg-blue-900/40 text-blue-600 dark:text-blue-400 font-bold text-xs">
                  {i + 1}
                </span>
                <p class="text-sm text-slate-600 dark:text-slate-300 leading-relaxed font-normal group-hover:text-slate-900 dark:group-hover:text-white transition-colors duration-150">
                  {pt}
                </p>
              </div>
            {/each}
          </div>
        </div>
      </div>
    {/if}

    <!-- Section 2: Use-Case Scenarios -->
    {#if service.scenarios && service.scenarios.length > 0}
      <div class="space-y-4">
        <div class="flex items-center gap-2.5">
          <span class="p-2 bg-emerald-50 dark:bg-emerald-900/30 text-emerald-600 dark:text-emerald-400 rounded-xl">
            <svg class="w-5.5 h-5.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
          </span>
          <h2 class="text-2xl font-bold text-slate-900 dark:text-white">Scenarios Where It Can Be Used</h2>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          {#each service.scenarios as item}
            <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm overflow-hidden flex flex-col hover:shadow-md transition-shadow duration-200">
              <!-- Scenario / Problem -->
              <div class="p-6 border-b border-slate-100 dark:border-slate-700/50 bg-slate-50/55 dark:bg-slate-900/30 flex-1">
                <div class="flex items-center gap-2 text-rose-600 dark:text-rose-450 font-bold text-xs uppercase tracking-wider mb-2">
                  <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                  </svg>
                  Business Scenario / Problem
                </div>
                <p class="text-sm text-slate-700 dark:text-slate-350 leading-relaxed font-normal">
                  {item.scenario}
                </p>
              </div>
              
              <!-- Architectural Solution -->
              <div class="p-6 bg-emerald-50/30 dark:bg-emerald-950/10">
                <div class="flex items-center gap-2 text-emerald-600 dark:text-emerald-400 font-bold text-xs uppercase tracking-wider mb-2">
                  <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                  </svg>
                  Recommended Architectural Solution
                </div>
                <p class="text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
                  {item.solution}
                </p>
              </div>
            </div>
          {/each}
        </div>
      </div>
    {/if}

    <!-- Section 3: Related Commands -->
    {#if service.commands && service.commands.length > 0}
      <div class="space-y-4">
        <div class="flex items-center gap-2.5">
          <span class="p-2 bg-amber-50 dark:bg-amber-900/30 text-amber-600 dark:text-amber-400 rounded-xl">
            <svg class="w-5.5 h-5.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
          </span>
          <h2 class="text-2xl font-bold text-slate-900 dark:text-white">Related CLI Commands</h2>
        </div>
        
        <div class="space-y-5">
          {#each service.commands as cmd, i}
            <div class="bg-slate-900 dark:bg-slate-950 rounded-2xl overflow-hidden shadow-md border border-slate-800">
              <div class="bg-slate-800/60 dark:bg-slate-900/80 px-5 py-3.5 text-xs text-slate-350 font-medium border-b border-slate-800 flex items-center justify-between gap-4">
                <span class="font-normal text-slate-300">{cmd.description}</span>
                <button
                  onclick={() => copyCommand(cmd.command, i)}
                  class="flex items-center gap-1.5 px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white rounded border border-slate-700 transition-colors text-[11px]"
                  title="Copy command to clipboard"
                >
                  {#if copiedIndex === i}
                    <svg class="w-3.5 h-3.5 text-emerald-450" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                    </svg>
                    <span>Copied!</span>
                  {:else}
                    <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m-5 4h6m-6 4h6m-6 4h6" />
                    </svg>
                    <span>Copy</span>
                  {/if}
                </button>
              </div>
              <div class="p-5 overflow-x-auto">
                <code class="text-xs md:text-sm font-mono text-emerald-400 whitespace-pre">{cmd.command}</code>
              </div>
            </div>
          {/each}
        </div>
      </div>
    {/if}
  {:else}
    <!-- Empty/Placeholder state -->
    <div class="bg-amber-50 dark:bg-amber-900/20 p-6 rounded-xl border border-amber-200 dark:border-amber-800/30 flex gap-4">
      <div class="text-amber-500 dark:text-amber-400">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
      </div>
      <div>
        <h3 class="font-bold text-amber-800 dark:text-amber-300 mb-1">Architectural Details Pending</h3>
        <p class="text-sm text-amber-700 dark:text-amber-400/85">
          Detailed guide information (key points, real-world scenarios, and administrative commands) for this service is currently compiling.
        </p>
      </div>
    </div>
  {/if}
</div>

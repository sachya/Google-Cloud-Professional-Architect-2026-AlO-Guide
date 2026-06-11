<script lang="ts">
  import { corePrinciples, pillars, crossPillars } from './wafData';
  
  // Navigation states using Svelte 5 Runes
  let activeTab = $state<'principles' | 'pillars' | 'perspectives'>('pillars');
  let activePillarId = $state<string>('operational-excellence');
  let activePerspectiveId = $state<string>('ai-ml');
  
  // Accordion state for recommendations (keys are category-index)
  let expandedRecs = $state<Record<string, boolean>>({});

  function toggleRec(key: string) {
    expandedRecs[key] = !expandedRecs[key];
  }

  // Derive active items
  let activePillar = $derived(pillars.find(p => p.id === activePillarId) || pillars[0]);
  let activePerspective = $derived(crossPillars.find(cp => cp.id === activePerspectiveId) || crossPillars[0]);

  // Color mapping utility for pillars
  const colorThemes: Record<string, {
    bg: string;
    border: string;
    text: string;
    accent: string;
    gradient: string;
    badge: string;
    hover: string;
  }> = {
    'operational-excellence': {
      bg: 'bg-blue-50 dark:bg-blue-950/20',
      border: 'border-blue-200 dark:border-blue-800',
      text: 'text-blue-700 dark:text-blue-300',
      accent: 'bg-blue-600 dark:bg-blue-500',
      gradient: 'from-blue-600 to-indigo-500',
      badge: 'bg-blue-100 dark:bg-blue-900/40 text-blue-800 dark:text-blue-300',
      hover: 'hover:bg-blue-50/50 dark:hover:bg-blue-950/10'
    },
    'security': {
      bg: 'bg-purple-50 dark:bg-purple-950/20',
      border: 'border-purple-200 dark:border-purple-800',
      text: 'text-purple-700 dark:text-purple-300',
      accent: 'bg-purple-600 dark:bg-purple-500',
      gradient: 'from-purple-600 to-pink-500',
      badge: 'bg-purple-100 dark:bg-purple-900/40 text-purple-800 dark:text-purple-300',
      hover: 'hover:bg-purple-50/50 dark:hover:bg-purple-950/10'
    },
    'reliability': {
      bg: 'bg-emerald-50 dark:bg-emerald-950/20',
      border: 'border-emerald-200 dark:border-emerald-800',
      text: 'text-emerald-700 dark:text-emerald-300',
      accent: 'bg-emerald-600 dark:bg-emerald-500',
      gradient: 'from-emerald-600 to-teal-500',
      badge: 'bg-emerald-100 dark:bg-emerald-900/40 text-emerald-800 dark:text-emerald-300',
      hover: 'hover:bg-emerald-50/50 dark:hover:bg-emerald-950/10'
    },
    'cost-optimization': {
      bg: 'bg-amber-50 dark:bg-amber-950/20',
      border: 'border-amber-200 dark:border-amber-800',
      text: 'text-amber-700 dark:text-amber-300',
      accent: 'bg-amber-600 dark:bg-amber-500',
      gradient: 'from-amber-600 to-orange-500',
      badge: 'bg-amber-100 dark:bg-amber-900/40 text-amber-800 dark:text-amber-300',
      hover: 'hover:bg-amber-50/50 dark:hover:bg-amber-950/10'
    },
    'performance-optimization': {
      bg: 'bg-indigo-50 dark:bg-indigo-950/20',
      border: 'border-indigo-200 dark:border-indigo-800',
      text: 'text-indigo-700 dark:text-indigo-300',
      accent: 'bg-indigo-600 dark:bg-indigo-500',
      gradient: 'from-indigo-600 to-violet-500',
      badge: 'bg-indigo-100 dark:bg-indigo-900/40 text-indigo-800 dark:text-indigo-300',
      hover: 'hover:bg-indigo-50/50 dark:hover:bg-indigo-950/10'
    },
    'sustainability': {
      bg: 'bg-green-50 dark:bg-green-950/20',
      border: 'border-green-200 dark:border-green-800',
      text: 'text-green-700 dark:text-green-300',
      accent: 'bg-green-600 dark:bg-green-500',
      gradient: 'from-green-600 to-emerald-500',
      badge: 'bg-green-100 dark:bg-green-900/40 text-green-800 dark:text-green-300',
      hover: 'hover:bg-green-50/50 dark:hover:bg-green-950/10'
    }
  };

  let activeTheme = $derived(colorThemes[activePillar.id] || colorThemes['operational-excellence']);
</script>

<svelte:head>
  <title>Well-Architected Framework | GCP Architect Hub</title>
</svelte:head>

<div class="max-w-6xl mx-auto space-y-10 pb-16">
  <!-- Hero Section -->
  <div class="bg-white dark:bg-slate-800 p-8 md:p-10 rounded-3xl border border-slate-200 dark:border-slate-700 shadow-sm relative overflow-hidden">
    <div class="absolute inset-0 bg-gradient-to-r from-blue-500/5 to-indigo-500/5 dark:from-blue-500/10 dark:to-indigo-500/10 pointer-events-none"></div>
    <div class="relative z-10">
      <h1 class="text-4xl font-extrabold text-slate-900 dark:text-white mb-4 tracking-tight">
        Google Cloud Well-Architected Framework
      </h1>
      <p class="text-lg text-slate-600 dark:text-slate-300 max-w-4xl leading-relaxed">
        A structured set of design principles, recommendations, and cross-pillar perspectives curated by Google experts. Master these pillars to construct highly secure, reliable, efficient, and cost-effective topologies tailored for modern enterprises.
      </p>
    </div>
  </div>

  <!-- Primary Navigation Tabs -->
  <div class="flex border-b border-slate-200 dark:border-slate-700">
    <button
      onclick={() => activeTab = 'pillars'}
      class="px-6 py-3.5 text-sm font-semibold border-b-2 transition-all flex items-center gap-2 focus:outline-none
      {activeTab === 'pillars' 
        ? 'border-blue-500 text-blue-600 dark:text-blue-400' 
        : 'border-transparent text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-white'}"
    >
      <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
      </svg>
      The 6 Pillars
    </button>
    <button
      onclick={() => activeTab = 'principles'}
      class="px-6 py-3.5 text-sm font-semibold border-b-2 transition-all flex items-center gap-2 focus:outline-none
      {activeTab === 'principles' 
        ? 'border-blue-500 text-blue-600 dark:text-blue-400' 
        : 'border-transparent text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-white'}"
    >
      <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
      </svg>
      Core Principles
    </button>
    <button
      onclick={() => activeTab = 'perspectives'}
      class="px-6 py-3.5 text-sm font-semibold border-b-2 transition-all flex items-center gap-2 focus:outline-none
      {activeTab === 'perspectives' 
        ? 'border-blue-500 text-blue-600 dark:text-blue-400' 
        : 'border-transparent text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-white'}"
    >
      <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" />
      </svg>
      Cross-Pillar Perspectives
    </button>
  </div>

  <!-- Content Switcher -->
  {#if activeTab === 'principles'}
    <!-- Core Principles Section -->
    <div class="space-y-6">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {#each corePrinciples as principle}
          <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm relative overflow-hidden flex flex-col hover:-translate-y-1 hover:shadow-md transition-all duration-200">
            <div class="absolute top-0 left-0 right-0 h-[3px] bg-gradient-to-r from-blue-500 to-indigo-500"></div>
            <h3 class="text-lg font-bold text-slate-800 dark:text-slate-100 flex items-center gap-2 mb-3">
              <span class="p-1.5 bg-blue-50 dark:bg-slate-900/40 text-blue-600 dark:text-blue-400 rounded-lg">
                {#if principle.id === 'design-for-change'}
                  <svg class="h-4.5 w-4.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 1121.21 7.89M9 11l3 3L22 4" /></svg>
                {:else if principle.id === 'document-architecture'}
                  <svg class="h-4.5 w-4.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
                {:else if principle.id === 'simplify-and-manage'}
                  <svg class="h-4.5 w-4.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" /></svg>
                {:else if principle.id === 'decouple-architecture'}
                  <svg class="h-4.5 w-4.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4" /></svg>
                {:else}
                  <svg class="h-4.5 w-4.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2" /></svg>
                {/if}
              </span>
              {principle.title}
            </h3>
            <p class="text-sm text-slate-600 dark:text-slate-400 mb-4 flex-1">
              {principle.summary}
            </p>
            <ul class="space-y-2.5 text-xs text-slate-700 dark:text-slate-300">
              {#each principle.points as pt}
                <li class="flex items-start gap-2">
                  <span class="h-1.5 w-1.5 rounded-full bg-indigo-500 mt-1.5 flex-shrink-0"></span>
                  <span>{pt}</span>
                </li>
              {/each}
            </ul>
          </div>
        {/each}
      </div>
    </div>

  {:else}
    <!-- Tab Switchers for Pillars or Perspectives -->
    <div class="grid grid-cols-1 lg:grid-cols-4 gap-8">
      
      <!-- Left sidebar buttons -->
      <div class="lg:col-span-1 space-y-2">
        {#if activeTab === 'pillars'}
          <h2 class="text-xs font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-3 px-3">Select Pillar</h2>
          {#each pillars as p}
            <button
              onclick={() => activePillarId = p.id}
              class="w-full text-left px-4 py-3 rounded-xl text-sm font-medium transition-all flex items-center justify-between border focus:outline-none
              {activePillarId === p.id 
                ? 'bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-300 border-blue-200 dark:border-blue-800 shadow-sm' 
                : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-350 border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-750'}"
            >
              <span>{p.title}</span>
              {#if p.id === 'sustainability'}
                <span class="px-2 py-0.5 text-[10px] rounded-full bg-green-100 dark:bg-green-900/40 text-green-700 dark:text-green-300 font-semibold border border-green-200 dark:border-green-800">Eco</span>
              {/if}
            </button>
          {/each}
        {:else}
          <h2 class="text-xs font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 mb-3 px-3">Select Perspective</h2>
          {#each crossPillars as cp}
            <button
              onclick={() => activePerspectiveId = cp.id}
              class="w-full text-left px-4 py-3 rounded-xl text-sm font-medium transition-all flex items-center justify-between border focus:outline-none
              {activePerspectiveId === cp.id 
                ? 'bg-indigo-50 dark:bg-indigo-900/20 text-indigo-700 dark:text-indigo-300 border-indigo-200 dark:border-indigo-800 shadow-sm' 
                : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-350 border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-750'}"
            >
              <span>{cp.title}</span>
            </button>
          {/each}
        {/if}
      </div>

      <!-- Right Main Content Panel -->
      <div class="lg:col-span-3 space-y-8">
        {#if activeTab === 'pillars'}
          <!-- Active Pillar Dashboard -->
          <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm relative overflow-hidden">
            <div class="absolute top-0 left-0 w-2 h-full bg-gradient-to-b {activeTheme.gradient}"></div>
            <div class="flex items-center gap-3 mb-4">
              <span class="px-3 py-1 text-xs font-semibold rounded-full {activeTheme.badge}">
                Pillar Guide
              </span>
            </div>
            <h2 class="text-2xl font-extrabold text-slate-900 dark:text-white mb-2">{activePillar.title}</h2>
            <p class="text-slate-600 dark:text-slate-300 leading-relaxed font-normal">{activePillar.description}</p>
          </div>

          <!-- Focus Areas & Recommendations -->
          <div class="space-y-4">
            <h3 class="text-lg font-bold text-slate-950 dark:text-white flex items-center gap-2">
              <svg class="h-5 w-5 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" /></svg>
              Core Recommendations & Focus Areas
            </h3>
            
            <div class="space-y-4">
              {#each activePillar.focusAreas as area, i}
                {@const recKey = `${activePillar.id}-${i}`}
                <div class="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl overflow-hidden shadow-sm">
                  <button 
                    onclick={() => toggleRec(recKey)}
                    class="w-full text-left p-5 flex items-center justify-between hover:bg-slate-50 dark:hover:bg-slate-750 transition-colors focus:outline-none"
                  >
                    <div>
                      <h4 class="font-bold text-slate-900 dark:text-white">{area.title}</h4>
                      <p class="text-xs text-slate-500 dark:text-slate-450 mt-1">{area.description}</p>
                    </div>
                    <svg class="h-5 w-5 text-slate-400 transform transition-transform duration-200 {expandedRecs[recKey] ? 'rotate-180' : ''}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                    </svg>
                  </button>

                  {#if expandedRecs[recKey]}
                    <div class="p-5 bg-slate-50/50 dark:bg-slate-850/30 border-t border-slate-100 dark:border-slate-750 space-y-3">
                      <ul class="space-y-2.5 text-sm text-slate-700 dark:text-slate-300">
                        {#each area.recommendations as rec}
                          <li class="flex items-start gap-3">
                            <span class="h-1.5 w-1.5 rounded-full bg-blue-500 dark:bg-blue-450 mt-2 flex-shrink-0"></span>
                            <span>{rec}</span>
                          </li>
                        {/each}
                      </ul>
                    </div>
                  {/if}
                </div>
              {/each}
            </div>
          </div>

          <!-- Exam Takeaways (High-Yield Alerts) -->
          <div class="p-6 rounded-2xl bg-amber-500/5 dark:bg-amber-500/10 border border-amber-500/20 space-y-3">
            <h3 class="text-sm font-bold uppercase tracking-wider text-amber-800 dark:text-amber-400 flex items-center gap-2">
              <svg class="h-5 w-5 text-amber-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" /></svg>
              GCP Architect Certification High-Yield Insights
            </h3>
            <ul class="space-y-3 text-sm text-slate-700 dark:text-slate-300">
              {#each activePillar.examInsights as insight}
                <li class="flex items-start gap-2.5">
                  <span class="h-1.5 w-1.5 rounded-full bg-amber-500 mt-2 flex-shrink-0"></span>
                  <span>{insight}</span>
                </li>
              {/each}
            </ul>
          </div>

          <!-- Shared Responsibility Matrix -->
          <div class="space-y-4">
            <h3 class="text-lg font-bold text-slate-950 dark:text-white flex items-center gap-2">
              <svg class="h-5 w-5 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4" /></svg>
              Shared Responsibility / Shared Fate Matrix
            </h3>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <!-- Google Manages -->
              <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm flex flex-col">
                <h4 class="font-bold text-slate-900 dark:text-white flex items-center gap-2 mb-4">
                  <span class="p-1.5 bg-green-50 dark:bg-green-900/40 text-green-600 dark:text-green-400 rounded-lg">
                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
                  </span>
                  Google Cloud Responsibility
                </h4>
                <ul class="space-y-3 text-sm text-slate-600 dark:text-slate-350 flex-1">
                  {#each activePillar.sharedFate.google as item}
                    <li class="flex items-start gap-2.5">
                      <span class="h-1.5 w-1.5 rounded-full bg-green-500 mt-2 flex-shrink-0"></span>
                      <span>{item}</span>
                    </li>
                  {/each}
                </ul>
              </div>

              <!-- Customer Manages -->
              <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm flex flex-col">
                <h4 class="font-bold text-slate-900 dark:text-white flex items-center gap-2 mb-4">
                  <span class="p-1.5 bg-blue-50 dark:bg-blue-900/40 text-blue-600 dark:text-blue-400 rounded-lg">
                    <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" /></svg>
                  </span>
                  Your (Customer) Responsibility
                </h4>
                <ul class="space-y-3 text-sm text-slate-600 dark:text-slate-350 flex-1">
                  {#each activePillar.sharedFate.customer as item}
                    <li class="flex items-start gap-2.5">
                      <span class="h-1.5 w-1.5 rounded-full bg-blue-500 mt-2 flex-shrink-0"></span>
                      <span>{item}</span>
                    </li>
                  {/each}
                </ul>
              </div>
            </div>
          </div>

        {:else}
          <!-- Cross-Pillar Perspectives -->
          <div class="bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm relative overflow-hidden">
            <div class="absolute top-0 left-0 w-2 h-full bg-gradient-to-b from-indigo-500 to-purple-500"></div>
            <div class="flex items-center gap-3 mb-4">
              <span class="px-3 py-1 text-xs font-semibold rounded-full bg-indigo-100 dark:bg-indigo-900/40 text-indigo-800 dark:text-indigo-300 border border-indigo-200 dark:border-indigo-800">
                Architectural Perspective
              </span>
            </div>
            <h2 class="text-2xl font-extrabold text-slate-900 dark:text-white mb-2">{activePerspective.title}</h2>
            <p class="text-slate-600 dark:text-slate-300 leading-relaxed font-normal">{activePerspective.description}</p>
          </div>

          <div class="space-y-4">
            <h3 class="text-lg font-bold text-slate-950 dark:text-white flex items-center gap-2">
              <svg class="h-5 w-5 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" /></svg>
              High-Yield Architectural Guidelines
            </h3>
            
            <div class="grid grid-cols-1 gap-4">
              {#each activePerspective.insights as insight}
                {@const splitInsight = insight.split(': ')}
                <div class="bg-white dark:bg-slate-800 p-6 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm space-y-2">
                  {#if splitInsight.length > 1}
                    <h4 class="font-bold text-slate-800 dark:text-slate-100 flex items-center gap-2">
                      <span class="h-2 w-2 rounded-full bg-indigo-500"></span>
                      {@html splitInsight[0].replace(/\*\*/g, '')}
                    </h4>
                    <p class="text-sm text-slate-650 dark:text-slate-350 leading-relaxed pl-4">
                      {splitInsight.slice(1).join(': ')}
                    </p>
                  {:else}
                    <p class="text-sm text-slate-650 dark:text-slate-350 leading-relaxed flex items-start gap-2">
                      <span class="h-2 w-2 rounded-full bg-indigo-500 mt-2 flex-shrink-0"></span>
                      <span>{insight}</span>
                    </p>
                  {/if}
                </div>
              {/each}
            </div>
          </div>
        {/if}
      </div>

    </div>
  {/if}
</div>

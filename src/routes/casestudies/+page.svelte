<script lang="ts">
  import casestudies from '$lib/data/casestudies.json';

  const gradients: Record<string, string> = {
    'altostrat-media': 'from-blue-600 to-indigo-600',
    'cymbal-retail': 'from-purple-600 to-pink-600',
    'ehr-healthcare': 'from-emerald-600 to-teal-600',
    'knightmotives-automotive': 'from-amber-500 to-orange-600'
  };

  const icons: Record<string, string> = {
    'altostrat-media': 'M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3',
    'cymbal-retail': 'M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z',
    'ehr-healthcare': 'M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4',
    'knightmotives-automotive': 'M12 19l9 2-9-18-9 18 9-2zm0 0v-8'
  };
</script>

<svelte:head>
  <title>Case Studies | GCP Architect Hub</title>
</svelte:head>

<div class="max-w-6xl mx-auto space-y-10 pb-16">
  <!-- Hero Section -->
  <div class="bg-white dark:bg-slate-800 p-8 md:p-12 rounded-3xl border border-slate-200 dark:border-slate-700 shadow-sm relative overflow-hidden">
    <div class="absolute inset-0 bg-gradient-to-r from-blue-500/5 to-indigo-500/5 dark:from-blue-500/10 dark:to-indigo-500/10 pointer-events-none"></div>
    <div class="relative z-10 max-w-3xl">
      <h1 class="text-4xl font-extrabold text-slate-900 dark:text-white mb-4 tracking-tight">
        Google Cloud Case Studies
      </h1>
      <p class="text-lg text-slate-600 dark:text-slate-350 leading-relaxed mb-6">
        The Professional Cloud Architect exam tests your ability to map business and technical requirements to Google Cloud infrastructure across 4 core case studies. Select a case below to study their full requirements-to-solutions mappings, proposed architectures, and exam tips.
      </p>
    </div>
  </div>

  <!-- Grid -->
  <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
    {#each casestudies as cs}
      <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm hover:shadow-md hover:-translate-y-0.5 transition-all duration-200 overflow-hidden flex flex-col group">
        <!-- Card Header with custom gradient -->
        <div class="p-6 bg-gradient-to-r {gradients[cs.id]} text-white relative">
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs px-2 py-1 bg-white/20 rounded-full font-medium tracking-wide uppercase">
              {cs.industry}
            </span>
            <span class="text-white/80">
              <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d={icons[cs.id]} />
              </svg>
            </span>
          </div>
          <h2 class="text-2xl font-bold tracking-tight">{cs.name}</h2>
        </div>

        <!-- Card Body -->
        <div class="p-6 flex-1 flex flex-col justify-between space-y-6">
          <div class="space-y-4">
            <p class="text-sm text-slate-600 dark:text-slate-350 leading-relaxed line-clamp-3">
              {cs.overview}
            </p>
            
            <div class="grid grid-cols-2 gap-3 text-xs">
              <div class="bg-slate-50 dark:bg-slate-900/60 p-3 rounded-lg border border-slate-100 dark:border-slate-800">
                <span class="block text-slate-400 dark:text-slate-500 font-medium mb-1">Business Mappings</span>
                <span class="font-bold text-slate-800 dark:text-slate-200 text-sm">{cs.businessRequirements.length} Mapped</span>
              </div>
              <div class="bg-slate-50 dark:bg-slate-900/60 p-3 rounded-lg border border-slate-100 dark:border-slate-800">
                <span class="block text-slate-400 dark:text-slate-500 font-medium mb-1">Technical Mappings</span>
                <span class="font-bold text-slate-800 dark:text-slate-200 text-sm">{cs.technicalRequirements.length} Mapped</span>
              </div>
            </div>
          </div>

          <a 
            href={`/casestudies/${cs.id}`}
            class="w-full text-center py-2.5 px-4 rounded-xl bg-slate-50 dark:bg-slate-900 text-slate-700 dark:text-slate-300 font-semibold hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors flex items-center justify-center gap-2 group"
          >
            <span>Analyze Case Map</span>
            <svg class="h-4 w-4 transform group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </a>
        </div>
      </div>
    {/each}
  </div>
</div>

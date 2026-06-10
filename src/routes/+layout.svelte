<script lang="ts">
  import '../app.css';
  import { page } from '$app/stores';
  import casestudies from '$lib/data/casestudies.json';
  let { data, children } = $props();

  // Search filter state
  let searchQuery = $state("");
  // Sidebar state
  let isSidebarCollapsed = $state(false);
  let isMobileSidebarOpen = $state(false);

  // Group filtered services by category
  let filteredServices = $derived(
    data.services.filter((service: any) => {
      if (!searchQuery.trim()) return true;
      const query = searchQuery.toLowerCase();
      return (
        service.name.toLowerCase().includes(query) ||
        (service.description && service.description.toLowerCase().includes(query)) ||
        (service.architecturalCategory && service.architecturalCategory.toLowerCase().includes(query))
      );
    })
  );

  // Filter case studies by query
  let filteredCaseStudies = $derived(
    casestudies.filter((cs: any) => {
      if (!searchQuery.trim()) return true;
      const query = searchQuery.toLowerCase();
      return (
        cs.name.toLowerCase().includes(query) ||
        cs.industry.toLowerCase().includes(query) ||
        cs.overview.toLowerCase().includes(query) ||
        cs.businessRequirements.some((b: any) => b.req.toLowerCase().includes(query) || b.solution.toLowerCase().includes(query)) ||
        cs.technicalRequirements.some((t: any) => t.req.toLowerCase().includes(query) || t.solution.toLowerCase().includes(query))
      );
    })
  );

  let categories = $derived(filteredServices.reduce((acc: any, service: any) => {
    if (!acc[service.category]) acc[service.category] = [];
    acc[service.category].push(service);
    return acc;
  }, {}));

  let categoryKeys = $derived(Object.keys(categories).sort());

  // Active route tracking
  let activeServiceId = $derived($page.params.id);
  let isCaseStudyRoute = $derived($page.url.pathname.startsWith('/casestudies'));
  let activeCaseStudyId = $derived(isCaseStudyRoute ? $page.params.id : null);
  let isWafRoute = $derived($page.url.pathname.startsWith('/waf'));
  let isLinksRoute = $derived($page.url.pathname.startsWith('/links'));
  
  let activeService = $derived(data.services.find((s: any) => s.id === activeServiceId));
  let activeCategory = $derived(isCaseStudyRoute ? 'GCP Case Studies' : (activeService?.category || ''));

  // Manual category toggle overrides
  let manualToggles = $state<Record<string, boolean>>({});

  function isCategoryExpanded(category: string): boolean {
    if (searchQuery.trim() !== "") return true; // Expand everything on search
    if (manualToggles[category] !== undefined) return manualToggles[category];
    if (category === "GCP Case Studies") return true; // Default Case Studies to expanded on load
    return category === activeCategory;
  }

  function toggleCategory(category: string) {
    if (manualToggles[category] === undefined) {
      // For GCP Case Studies, default is true, so toggle is false
      const defaultVal = category === "GCP Case Studies" ? true : (category === activeCategory);
      manualToggles[category] = !defaultVal;
    } else {
      manualToggles[category] = !manualToggles[category];
    }
  }

  // Helper to close mobile menu
  function closeMobileSidebar() {
    isMobileSidebarOpen = false;
  }
</script>

<div class="min-h-screen bg-slate-50 dark:bg-slate-900 text-slate-900 dark:text-slate-100 flex flex-col font-sans transition-colors duration-200">
  <!-- Top Navigation Header -->
  <header class="bg-white dark:bg-slate-800 border-b border-slate-200 dark:border-slate-700 p-4 sticky top-0 z-30 shadow-sm">
    <div class="container mx-auto flex items-center justify-between">
      <div class="flex items-center gap-3">
        <!-- Hamburger Menu Mobile Toggle -->
        <button 
          onclick={() => isMobileSidebarOpen = !isMobileSidebarOpen}
          class="md:hidden p-2 rounded-md text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 focus:outline-none"
          aria-label="Toggle mobile menu"
        >
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>

        <!-- Desktop Sidebar Toggle -->
        <button 
          onclick={() => isSidebarCollapsed = !isSidebarCollapsed}
          class="hidden md:block p-2 rounded-md text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-700 focus:outline-none"
          title={isSidebarCollapsed ? "Expand sidebar" : "Collapse sidebar"}
        >
          <svg class="h-5 w-5 transform transition-transform duration-200 {isSidebarCollapsed ? 'rotate-180' : ''}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 19l-7-7 7-7m8 14l-7-7 7-7" />
          </svg>
        </button>

        <a href="/" class="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-600 to-indigo-500 hover:opacity-90 transition-opacity flex items-center gap-2">
          <span>GCP Architect Hub</span>
          <span class="text-xs px-2 py-0.5 bg-blue-100 dark:bg-blue-900/40 text-blue-700 dark:text-blue-300 rounded-full font-normal">PCA Study Guide</span>
        </a>
      </div>

      <nav class="flex gap-2">
        <a href="/" class="text-sm font-medium px-3 py-2 rounded-md hover:bg-slate-100 dark:hover:bg-slate-700 transition-colors {$page.url.pathname === '/' || $page.url.pathname.startsWith('/services') ? 'text-blue-600 dark:text-blue-400 font-semibold bg-slate-100 dark:bg-slate-800' : 'text-slate-700 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400'}">Services</a>
        <a href="/casestudies" class="text-sm font-medium px-3 py-2 rounded-md hover:bg-slate-100 dark:hover:bg-slate-700 transition-colors {isCaseStudyRoute ? 'text-blue-600 dark:text-blue-400 font-semibold bg-slate-100 dark:bg-slate-800' : 'text-slate-700 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400'}">Case Studies</a>
        <a href="/waf" class="text-sm font-medium px-3 py-2 rounded-md hover:bg-slate-100 dark:hover:bg-slate-700 transition-colors {isWafRoute ? 'text-blue-600 dark:text-blue-400 font-semibold bg-slate-100 dark:bg-slate-800' : 'text-slate-700 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400'}">Well-Architected</a>
        <a href="/links" class="text-sm font-medium px-3 py-2 rounded-md hover:bg-slate-100 dark:hover:bg-slate-700 transition-colors {isLinksRoute ? 'text-blue-600 dark:text-blue-400 font-semibold bg-slate-100 dark:bg-slate-800' : 'text-slate-700 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400'}">Links</a>
      </nav>
    </div>
  </header>

  <!-- Main Workspace -->
  <div class="flex-1 flex overflow-hidden relative">
    
    <!-- Mobile Sidebar Drawer (Overlay & Panel) -->
    {#if isMobileSidebarOpen}
      <div 
        onclick={closeMobileSidebar} 
        class="fixed inset-0 bg-slate-900/60 z-40 md:hidden transition-opacity duration-200"
        aria-hidden="true"
      ></div>
    {/if}

    <aside class="fixed inset-y-0 left-0 w-80 bg-white dark:bg-slate-800 z-50 transform transition-transform duration-300 md:hidden flex flex-col border-r border-slate-200 dark:border-slate-700 pt-16 {isMobileSidebarOpen ? 'translate-x-0' : '-translate-x-full'}">
      <!-- Search inside Mobile Menu -->
      <div class="p-4 border-b border-slate-200 dark:border-slate-700">
        <div class="relative">
          <input 
            type="text" 
            placeholder="Search offerings & cases..." 
            bind:value={searchQuery}
            class="w-full pl-9 pr-4 py-2 text-sm bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-slate-900 dark:text-slate-100"
          />
          <svg class="absolute left-3 top-2.5 h-4 w-4 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>
      </div>
      <!-- Scrollable Categories for Mobile -->
      <div class="flex-1 overflow-y-auto p-4 space-y-4">
        
        <!-- Study Links & Resources (Mobile) -->
        <div class="space-y-1 pb-2 border-b border-slate-100 dark:border-slate-800/60">
          <a 
            href="/links" 
            onclick={closeMobileSidebar}
            class="w-full flex items-center gap-2.5 py-2 px-3 rounded-lg font-semibold text-xs uppercase tracking-wider transition-colors {isLinksRoute ? 'bg-blue-50 dark:bg-slate-800 text-blue-600 dark:text-blue-400 font-semibold border-l-2 border-blue-500 shadow-sm' : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/40'}"
          >
            <svg class="h-4 w-4 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" />
            </svg>
            <span>Study Links & Resources</span>
          </a>
        </div>

        <!-- Case Studies (Mobile) -->
        <div class="space-y-1">
          <button 
            onclick={() => toggleCategory("GCP Case Studies")}
            class="w-full flex items-center justify-between text-left py-2 px-2 rounded-lg font-semibold text-xs text-slate-500 dark:text-slate-400 uppercase tracking-wider hover:bg-slate-100 dark:hover:bg-slate-750 transition-colors"
          >
            <span>GCP Case Studies ({filteredCaseStudies.length})</span>
            <svg class="h-4 w-4 transform transition-transform duration-200 {isCategoryExpanded('GCP Case Studies') ? 'rotate-90' : ''}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </button>
          
          {#if isCategoryExpanded("GCP Case Studies")}
            <ul class="space-y-0.5 pl-2">
              {#each filteredCaseStudies as cs}
                <li>
                  <a 
                    href={`/casestudies/${cs.id}`} 
                    onclick={closeMobileSidebar}
                    class="block px-3 py-2 text-sm rounded-md transition-colors truncate {activeCaseStudyId === cs.id ? 'bg-blue-50 dark:bg-slate-700/60 text-blue-600 dark:text-blue-400 font-medium border-l-2 border-blue-500' : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-50 dark:hover:bg-slate-700/30'}"
                    title={cs.name}
                  >
                    {cs.name}
                  </a>
                </li>
              {/each}
            </ul>
          {/if}
        </div>

        {#each categoryKeys as category}
          <div class="space-y-1">
            <button 
              onclick={() => toggleCategory(category)}
              class="w-full flex items-center justify-between text-left py-2 px-2 rounded-lg font-semibold text-xs text-slate-500 dark:text-slate-400 uppercase tracking-wider hover:bg-slate-100 dark:hover:bg-slate-750 transition-colors"
            >
              <span>{category} ({categories[category].length})</span>
              <svg class="h-4 w-4 transform transition-transform duration-200 {isCategoryExpanded(category) ? 'rotate-90' : ''}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </button>
            
            {#if isCategoryExpanded(category)}
              <ul class="space-y-0.5 pl-2 transition-all duration-300">
                {#each categories[category] as service}
                  <li>
                    <a 
                      href={`/services/${service.id}`} 
                      onclick={closeMobileSidebar}
                      class="block px-3 py-2 text-sm rounded-md transition-colors truncate {activeServiceId === service.id ? 'bg-blue-50 dark:bg-slate-700/60 text-blue-600 dark:text-blue-400 font-medium border-l-2 border-blue-500' : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-50 dark:hover:bg-slate-700/30'}"
                      title={service.name}
                    >
                      {service.name}
                    </a>
                  </li>
                {/each}
              </ul>
            {/if}
          </div>
        {/each}
      </div>
    </aside>

    <!-- Desktop Sidebar -->
    <aside 
      class="border-r border-slate-200 dark:border-slate-700 bg-slate-50/50 dark:bg-slate-900/50 flex flex-col flex-shrink-0 transition-all duration-300 overflow-hidden {isSidebarCollapsed ? 'w-0' : 'w-72'} hidden md:flex"
    >
      <!-- Search Filter -->
      <div class="p-4 border-b border-slate-200 dark:border-slate-700">
        <div class="relative">
          <input 
            type="text" 
            placeholder="Search offerings & cases..." 
            bind:value={searchQuery}
            class="w-full pl-9 pr-4 py-2 text-sm bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-slate-900 dark:text-slate-100 shadow-sm"
          />
          <svg class="absolute left-3 top-2.5 h-4 w-4 text-slate-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>
      </div>

      <!-- Categories List -->
      <div class="flex-1 overflow-y-auto p-4 space-y-4">
        
        <!-- Study Links & Resources (Desktop) -->
        <div class="border-b border-slate-100 dark:border-slate-800/60 pb-3">
          <a 
            href="/links" 
            class="w-full flex items-center gap-2.5 py-2 px-3 rounded-lg font-bold text-[11px] uppercase tracking-wider transition-colors {isLinksRoute ? 'bg-blue-50 dark:bg-slate-800 text-blue-600 dark:text-blue-400 font-semibold border-l-2 border-blue-500 shadow-sm' : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/40'}"
          >
            <svg class="h-3.5 w-3.5 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" />
            </svg>
            <span>Study Links & Resources</span>
          </a>
        </div>

        <!-- Case Studies (Desktop) -->
        <div class="border-b border-slate-100 dark:border-slate-800/60 pb-3 last:border-b-0">
          <button 
            onclick={() => toggleCategory("GCP Case Studies")}
            class="w-full flex items-center justify-between text-left py-2 px-2 rounded-lg font-bold text-[11px] text-slate-500 dark:text-slate-400 uppercase tracking-wider hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors focus:outline-none"
          >
            <span class="truncate pr-2">GCP Case Studies ({filteredCaseStudies.length})</span>
            <svg class="h-3.5 w-3.5 transform transition-transform duration-200 flex-shrink-0 {isCategoryExpanded('GCP Case Studies') ? 'rotate-90' : ''}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </button>
          
          {#if isCategoryExpanded("GCP Case Studies")}
            <ul class="space-y-0.5 mt-1 pl-1">
              {#each filteredCaseStudies as cs}
                <li>
                  <a 
                    href={`/casestudies/${cs.id}`} 
                    class="block px-3 py-1.5 text-sm rounded-md transition-colors truncate {activeCaseStudyId === cs.id ? 'bg-blue-50 dark:bg-slate-800 text-blue-600 dark:text-blue-400 font-semibold border-l-2 border-blue-500 shadow-sm' : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100/60 dark:hover:bg-slate-800/40'}"
                    title={cs.name}
                  >
                    {cs.name}
                  </a>
                </li>
              {/each}
            </ul>
          {/if}
        </div>

        {#each categoryKeys as category}
          <div class="border-b border-slate-100 dark:border-slate-800/60 pb-3 last:border-b-0">
            <button 
              onclick={() => toggleCategory(category)}
              class="w-full flex items-center justify-between text-left py-2 px-2 rounded-lg font-bold text-[11px] text-slate-500 dark:text-slate-400 uppercase tracking-wider hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors focus:outline-none"
            >
              <span class="truncate pr-2">{category} ({categories[category].length})</span>
              <svg class="h-3.5 w-3.5 transform transition-transform duration-200 flex-shrink-0 {isCategoryExpanded(category) ? 'rotate-90' : ''}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </button>
            
            {#if isCategoryExpanded(category)}
              <ul class="space-y-0.5 mt-1 pl-1">
                {#each categories[category] as service}
                  <li>
                    <a 
                      href={`/services/${service.id}`} 
                      class="block px-3 py-1.5 text-sm rounded-md transition-colors truncate {activeServiceId === service.id ? 'bg-blue-50 dark:bg-slate-800 text-blue-600 dark:text-blue-400 font-semibold border-l-2 border-blue-500 shadow-sm' : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100/60 dark:hover:bg-slate-800/40'}"
                      title={service.name}
                    >
                      {service.name}
                    </a>
                  </li>
                {/each}
              </ul>
            {/if}
          </div>
        {/each}
        {#if categoryKeys.length === 0}
          <div class="text-center py-8 text-sm text-slate-400 dark:text-slate-500">
            No offerings match search.
          </div>
        {/if}
      </div>
    </aside>

    <!-- Main Content Area -->
    <main class="flex-1 overflow-y-auto p-6 md:p-8 bg-white dark:bg-slate-900 transition-colors duration-200">
      {@render children()}
    </main>
  </div>
</div>


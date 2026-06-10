<script lang="ts">
  let { data } = $props();
  
  let totalServices = $derived(data.services.length);
  let categories = $derived(data.services.reduce((acc: any, service: any) => {
    if (!acc[service.category]) acc[service.category] = 0;
    acc[service.category]++;
    return acc;
  }, {}));
  
  let categoryEntries = $derived(Object.entries(categories).sort((a: any, b: any) => b[1] - a[1]));
</script>

<div class="max-w-4xl mx-auto space-y-8">
  <div class="text-center py-10 bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-slate-800 dark:to-slate-900 rounded-2xl border border-blue-100 dark:border-slate-700 shadow-sm">
    <h1 class="text-4xl font-extrabold text-slate-900 dark:text-white mb-4">GCP Architect Study Hub</h1>
    <p class="text-lg text-slate-600 dark:text-slate-300 max-w-2xl mx-auto">
      Your comprehensive reference guide for mastering Google Cloud Platform. Navigate through the detailed features, IAM policies, and architecture principles for {totalServices} services.
    </p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    {#each categoryEntries as [category, count]}
      <div class="bg-white dark:bg-slate-800 p-6 rounded-xl border border-slate-200 dark:border-slate-700 shadow-sm hover:shadow-md transition-shadow">
        <h2 class="text-lg font-bold text-slate-800 dark:text-slate-100 mb-2">{category}</h2>
        <div class="flex items-center justify-between mt-4">
          <span class="text-3xl font-light text-blue-600 dark:text-blue-400">{count}</span>
          <span class="text-sm font-medium text-slate-500 uppercase tracking-wide">Services</span>
        </div>
      </div>
    {/each}
  </div>
</div>

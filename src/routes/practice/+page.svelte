<script lang="ts">
  import { onMount } from 'svelte';

  interface Attempt {
    setId: number;
    score: number;
    total: number;
    percent: number;
    timeSpent: string;
    date: string;
    passed: boolean;
  }

  let attempts = $state<Attempt[]>([]);

  onMount(() => {
    loadAttempts();
  });

  function loadAttempts() {
    try {
      const stored = localStorage.getItem('gcp_practice_attempts');
      if (stored) {
        attempts = JSON.parse(stored);
      }
    } catch (e) {
      console.error('Error loading history:', e);
    }
  }

  function clearHistory() {
    if (confirm('Are you sure you want to clear your practice exam attempt history?')) {
      localStorage.removeItem('gcp_practice_attempts');
      attempts = [];
    }
  }
</script>

<div class="max-w-5xl mx-auto space-y-8 pb-12">
  <!-- Hero Section -->
  <div class="p-8 md:p-10 bg-gradient-to-br from-blue-600 to-indigo-700 dark:from-slate-800 dark:to-slate-900 rounded-2xl border border-blue-500/20 dark:border-slate-700 shadow-lg text-white">
    <div class="max-w-3xl">
      <h1 class="text-3xl md:text-4xl font-extrabold mb-4 flex items-center gap-3">
        <svg class="h-10 w-10 text-blue-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        Practice Exam Simulator
      </h1>
      <p class="text-blue-100 text-base md:text-lg mb-6">
        Test your readiness for the official Google Cloud Professional Cloud Architect (PCA) exam. Take 5 realistic, advanced practice sets of 90 questions. The engine randomizes question and option order to simulate real-world testing conditions.
      </p>
      
      <!-- Exam Stats Overview -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4 bg-white/10 dark:bg-black/20 p-4 rounded-xl backdrop-blur-sm text-sm">
        <div>
          <span class="block text-blue-200 text-xs uppercase font-semibold">Total Questions</span>
          <span class="text-xl font-bold">90 per Set</span>
        </div>
        <div>
          <span class="block text-blue-200 text-xs uppercase font-semibold">Time Allowed</span>
          <span class="text-xl font-bold">120 Minutes</span>
        </div>
        <div>
          <span class="block text-blue-200 text-xs uppercase font-semibold">Passing Score</span>
          <span class="text-xl font-bold">70%</span>
        </div>
        <div>
          <span class="block text-blue-200 text-xs uppercase font-semibold">Structure</span>
          <span class="text-xl font-bold">65% Single / 35% Multi</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Exam Sets Grid -->
  <div>
    <h2 class="text-2xl font-bold text-slate-800 dark:text-slate-100 mb-6">Available Practice Sets</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {#each Array(5) as _, i}
        {@const setId = i + 1}
        {@const setAttempts = attempts.filter(a => a.setId === setId)}
        {@const bestScore = setAttempts.length > 0 ? Math.max(...setAttempts.map(a => a.percent)) : null}
        
        <div class="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700/80 rounded-xl p-6 shadow-sm hover:shadow-md transition-all flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="text-xs font-semibold px-2.5 py-1 bg-blue-50 dark:bg-blue-900/30 text-blue-600 dark:text-blue-400 rounded-md">
                GCP PCA Simulator
              </span>
              {#if bestScore !== null}
                <span class="text-xs font-medium px-2 py-0.5 rounded-full {bestScore >= 70 ? 'bg-green-100 dark:bg-green-900/30 text-green-700 dark:text-green-300' : 'bg-amber-100 dark:bg-amber-900/30 text-amber-700 dark:text-amber-300'}">
                  Best: {bestScore}%
                </span>
              {/if}
            </div>
            
            <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-2">Practice Set {setId}</h3>
            <p class="text-sm text-slate-500 dark:text-slate-400 mb-6 leading-relaxed">
              90 tricky, advanced-level questions mapping to the GCP Well-Architected Framework and case studies (Altostrat, Cymbal, EHR, KnightMotives).
            </p>
          </div>
          
          <div class="space-y-3">
            <a 
              href={`/practice/${setId}`}
              class="w-full inline-flex items-center justify-center px-4 py-2.5 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition-colors text-sm shadow-sm"
            >
              Start Exam Set
              <svg class="ml-2 h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
              </svg>
            </a>
            
            {#if setAttempts.length > 0}
              <div class="text-xs text-slate-400 text-center">
                Attempts: {setAttempts.length} | Last: {setAttempts[setAttempts.length - 1].percent}%
              </div>
            {/if}
          </div>
        </div>
      {/each}
    </div>
  </div>

  <!-- Attempt History Dashboard -->
  <div class="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl p-6 shadow-sm">
    <div class="flex items-center justify-between mb-6">
      <div class="flex items-center gap-2">
        <svg class="h-6 w-6 text-slate-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <h2 class="text-xl font-bold text-slate-900 dark:text-white">Your Performance History</h2>
      </div>
      {#if attempts.length > 0}
        <button 
          onclick={clearHistory}
          class="text-xs font-semibold text-rose-600 hover:text-rose-700 hover:underline bg-none border-none cursor-pointer"
        >
          Clear History
        </button>
      {/if}
    </div>

    {#if attempts.length === 0}
      <div class="text-center py-12 border-2 border-dashed border-slate-200 dark:border-slate-700 rounded-xl text-slate-500 dark:text-slate-400">
        <p class="text-base mb-2">No exam attempts recorded yet.</p>
        <p class="text-xs text-slate-400">Select any practice set above to begin testing your skills.</p>
      </div>
    {:else}
      <div class="overflow-x-auto">
        <table class="w-full text-left text-sm border-collapse">
          <thead>
            <tr class="border-b border-slate-200 dark:border-slate-700 text-slate-400 font-semibold">
              <th class="pb-3 pr-4">Date Taken</th>
              <th class="pb-3 px-4">Exam Set</th>
              <th class="pb-3 px-4">Score</th>
              <th class="pb-3 px-4">Time Spent</th>
              <th class="pb-3 pl-4 text-right">Result</th>
            </tr>
          </thead>
          <tbody>
            {#each [...attempts].reverse() as attempt}
              <tr class="border-b border-slate-100 dark:border-slate-800/60 hover:bg-slate-50/50 dark:hover:bg-slate-800/30 transition-colors text-slate-700 dark:text-slate-300">
                <td class="py-3.5 pr-4 text-slate-500 dark:text-slate-400">{attempt.date}</td>
                <td class="py-3.5 px-4 font-semibold">Set {attempt.setId}</td>
                <td class="py-3.5 px-4 font-mono font-medium">
                  {attempt.score}/{attempt.total} ({attempt.percent}%)
                </td>
                <td class="py-3.5 px-4 font-mono text-slate-500 dark:text-slate-400">{attempt.timeSpent}</td>
                <td class="py-3.5 pl-4 text-right">
                  <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold {attempt.passed ? 'bg-green-100 dark:bg-green-900/30 text-green-800 dark:text-green-400' : 'bg-rose-100 dark:bg-rose-900/30 text-rose-800 dark:text-rose-400'}">
                    {attempt.passed ? 'PASS' : 'FAIL'}
                  </span>
                </td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
    {/if}
  </div>
</div>

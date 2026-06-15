<script lang="ts">
  import { onMount } from 'svelte';
  import { page } from '$app/state';
  import { goto } from '$app/navigation';

  const setId = parseInt(page.params.setId, 10);

  interface QuestionReview {
    id: string;
    question: string;
    options: string[];
    correctAnswer: number[];
    userAnswer: number[];
    isCorrect: boolean;
    category: string;
    explanation: string;
  }

  interface ResultsData {
    setId: number;
    score: number;
    total: number;
    percent: number;
    timeSpent: string;
    date: string;
    passed: boolean;
    categoryStats: Record<string, { total: number; correct: number }>;
    questionsReview: QuestionReview[];
  }

  let results = $state<ResultsData | null>(null);
  let reviewFilter = $state<'all' | 'correct' | 'incorrect' | 'skipped'>('all');
  let expandedQuestionId = $state<string | null>(null);

  onMount(() => {
    try {
      const stored = sessionStorage.getItem(`gcp_exam_results_${setId}`);
      if (stored) {
        results = JSON.parse(stored);
      } else {
        // Redirect if no results found
        goto('/practice');
      }
    } catch (e) {
      console.error('Error loading exam results:', e);
      goto('/practice');
    }
  });

  // Filtered reviews
  let filteredReviews = $derived(() => {
    if (!results) return [];
    return results.questionsReview.filter(q => {
      if (reviewFilter === 'all') return true;
      if (reviewFilter === 'correct') return q.isCorrect;
      if (reviewFilter === 'incorrect') return !q.isCorrect && q.userAnswer.length > 0;
      if (reviewFilter === 'skipped') return q.userAnswer.length === 0;
      return true;
    });
  });

  function getCategoryScoreClass(percent: number): string {
    if (percent >= 70) return 'bg-green-500 text-green-700 dark:text-green-400';
    if (percent >= 50) return 'bg-amber-500 text-amber-700 dark:text-amber-400';
    return 'bg-rose-500 text-rose-750 dark:text-rose-450';
  }

  function getCategoryBgClass(percent: number): string {
    if (percent >= 70) return 'bg-green-50 dark:bg-green-950/10 border-green-100 dark:border-green-900/30';
    if (percent >= 50) return 'bg-amber-50 dark:bg-amber-950/10 border-amber-105 dark:border-amber-900/30';
    return 'bg-rose-50 dark:bg-rose-950/10 border-rose-105 dark:border-rose-900/30';
  }
</script>

{#if !results}
  <div class="h-96 flex items-center justify-center">
    <div class="flex flex-col items-center gap-3">
      <div class="animate-spin rounded-full h-10 w-10 border-4 border-blue-600 border-t-transparent"></div>
      <p class="text-slate-500 dark:text-slate-400 text-sm">Compiling exam analytics...</p>
    </div>
  </div>
{:else}
  <div class="max-w-4xl mx-auto space-y-8 pb-16">
    <!-- Header Back Button -->
    <div class="flex items-center justify-between">
      <a 
        href="/practice" 
        class="inline-flex items-center gap-2 text-sm font-semibold text-slate-500 hover:text-slate-800 dark:hover:text-white transition-colors"
      >
        <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7" />
        </svg>
        Back to Dashboard
      </a>
      <span class="text-xs text-slate-450 font-mono">Exam taken on {results.date}</span>
    </div>

    <!-- Score Card Overview -->
    <div class="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700/80 rounded-2xl p-6 md:p-8 shadow-sm flex flex-col md:flex-row items-center gap-8 justify-between">
      <div class="space-y-4 text-center md:text-left">
        <h1 class="text-3xl font-extrabold text-slate-900 dark:text-white">Exam Results Compiled</h1>
        <p class="text-slate-500 dark:text-slate-450 max-w-md text-sm md:text-base leading-relaxed">
          You have completed GCP Professional Cloud Architect Practice Set {results.setId}. Check your score, time taken, and domain-wise performance analytics below.
        </p>
        
        <div class="flex flex-wrap gap-4 justify-center md:justify-start">
          <div class="px-4 py-2 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-100 dark:border-slate-700/50">
            <span class="block text-slate-400 text-[10px] uppercase font-bold tracking-wider">Correct Answers</span>
            <span class="text-base font-bold text-slate-800 dark:text-slate-200">{results.score} / {results.total}</span>
          </div>
          <div class="px-4 py-2 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-100 dark:border-slate-700/50">
            <span class="block text-slate-400 text-[10px] uppercase font-bold tracking-wider">Time Elapsed</span>
            <span class="text-base font-bold text-slate-800 dark:text-slate-200">{results.timeSpent}</span>
          </div>
        </div>
      </div>

      <!-- Score Ring Indicator -->
      <div class="flex flex-col items-center gap-2">
        <div class="relative flex items-center justify-center">
          <!-- SVG Circular Progress Bar -->
          <svg class="h-36 w-36 transform -rotate-90">
            <circle 
              cx="72" cy="72" r="62" 
              class="stroke-slate-100 dark:stroke-slate-700 fill-none" 
              stroke-width="10" 
            />
            <circle 
              cx="72" cy="72" r="62" 
              class="fill-none transition-all duration-1000 ease-out {results.passed ? 'stroke-green-500' : 'stroke-rose-500'}" 
              stroke-width="10" 
              stroke-dasharray="390"
              stroke-dashoffset={390 - (390 * results.percent) / 100}
              stroke-linecap="round"
            />
          </svg>
          <div class="absolute text-center">
            <span class="block text-3xl font-extrabold text-slate-800 dark:text-white">{results.percent}%</span>
            <span class="text-[10px] font-bold tracking-widest text-slate-400 uppercase">Score</span>
          </div>
        </div>
        
        <span class="inline-flex items-center px-4 py-1.5 rounded-full text-sm font-extrabold shadow-sm {results.passed ? 'bg-green-100 dark:bg-green-950/30 text-green-700 dark:text-green-400' : 'bg-rose-100 dark:bg-rose-950/30 text-rose-700 dark:text-rose-450'}">
          {results.passed ? 'PASSING SCORE' : 'FAILING SCORE'}
        </span>
      </div>
    </div>

    <!-- Category-Wise / Domain Performance Breakdown -->
    <div class="space-y-4">
      <h2 class="text-xl font-bold text-slate-800 dark:text-white flex items-center gap-2">
        <svg class="h-5 w-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
        </svg>
        Domain Performance Analytics
      </h2>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        {#each Object.entries(results.categoryStats) as [category, stats]}
          {@const catPercent = Math.round((stats.correct / stats.total) * 100)}
          {@const scoreClass = getCategoryScoreClass(catPercent)}
          {@const bgClass = getCategoryBgClass(catPercent)}
          
          <div class="p-5 rounded-xl border flex flex-col justify-between shadow-sm bg-white dark:bg-slate-800/80 {bgClass}">
            <div class="space-y-2">
              <div class="flex items-start justify-between gap-4">
                <span class="text-sm font-bold text-slate-800 dark:text-slate-100 leading-snug line-clamp-2">
                  {category}
                </span>
                <span class="text-sm font-mono font-bold shrink-0 {scoreClass.split(' ')[1]}">
                  {catPercent}%
                </span>
              </div>
              <p class="text-xs text-slate-400">
                Correct answers: {stats.correct} of {stats.total} questions
              </p>
            </div>
            
            <!-- Custom Progress Bar -->
            <div class="w-full bg-slate-200 dark:bg-slate-700/80 h-2 rounded-full mt-4 overflow-hidden">
              <div 
                class="h-2 rounded-full transition-all duration-1000 {scoreClass.split(' ')[0]}" 
                style="width: {catPercent}%"
              ></div>
            </div>
          </div>
        {/each}
      </div>
    </div>

    <!-- Review Questions Section -->
    <div class="space-y-6">
      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <h2 class="text-xl font-bold text-slate-800 dark:text-white flex items-center gap-2">
          <svg class="h-5 w-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
          </svg>
          Detailed Questions Review
        </h2>
        
        <!-- Filter Tabs -->
        <div class="flex bg-slate-100 dark:bg-slate-800 rounded-lg p-1 text-xs border border-slate-200 dark:border-slate-700 shrink-0 font-medium">
          <button 
            onclick={() => reviewFilter = 'all'}
            class="px-3 py-1.5 rounded-md transition-colors {reviewFilter === 'all' ? 'bg-white dark:bg-slate-750 text-blue-600 dark:text-blue-400 font-bold shadow-sm' : 'text-slate-500 hover:text-slate-800 dark:hover:text-white'}"
          >
            All ({results.questionsReview.length})
          </button>
          <button 
            onclick={() => reviewFilter = 'correct'}
            class="px-3 py-1.5 rounded-md transition-colors {reviewFilter === 'correct' ? 'bg-white dark:bg-slate-750 text-green-600 dark:text-green-400 font-bold shadow-sm' : 'text-slate-500 hover:text-slate-800 dark:hover:text-white'}"
          >
            Correct ({results.questionsReview.filter(q => q.isCorrect).length})
          </button>
          <button 
            onclick={() => reviewFilter = 'incorrect'}
            class="px-3 py-1.5 rounded-md transition-colors {reviewFilter === 'incorrect' ? 'bg-white dark:bg-slate-750 text-rose-600 dark:text-rose-450 font-bold shadow-sm' : 'text-slate-500 hover:text-slate-800 dark:hover:text-white'}"
          >
            Incorrect ({results.questionsReview.filter(q => !q.isCorrect && q.userAnswer.length > 0).length})
          </button>
          <button 
            onclick={() => reviewFilter = 'skipped'}
            class="px-3 py-1.5 rounded-md transition-colors {reviewFilter === 'skipped' ? 'bg-white dark:bg-slate-750 text-slate-600 dark:text-slate-400 font-bold shadow-sm' : 'text-slate-500 hover:text-slate-800 dark:hover:text-white'}"
          >
            Skipped ({results.questionsReview.filter(q => q.userAnswer.length === 0).length})
          </button>
        </div>
      </div>

      <!-- Questions Review Grid -->
      <div class="space-y-4">
        {#each filteredReviews() as rev, index}
          <div class="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700/80 rounded-xl overflow-hidden shadow-sm hover:border-slate-300 transition-colors">
            <!-- Question Toggle Header -->
            <button 
              onclick={() => expandedQuestionId = expandedQuestionId === rev.id ? null : rev.id}
              class="w-full text-left p-5 flex items-start justify-between gap-4 hover:bg-slate-50/50 dark:hover:bg-slate-800/40 transition-colors"
            >
              <div class="space-y-1.5">
                <div class="flex items-center gap-2 flex-wrap">
                  <span class="text-[10px] font-mono font-semibold px-2 py-0.5 rounded {rev.isCorrect ? 'bg-green-150 text-green-700 dark:bg-green-900/20 dark:text-green-400' : 'bg-rose-150 text-rose-700 dark:bg-rose-900/20 dark:text-rose-400'}">
                    {rev.isCorrect ? 'CORRECT' : rev.userAnswer.length === 0 ? 'SKIPPED' : 'INCORRECT'}
                  </span>
                  <span class="text-[10px] font-mono text-slate-400">{rev.category}</span>
                </div>
                <h3 class="text-sm md:text-base font-medium text-slate-900 dark:text-white leading-relaxed">
                  Q{index + 1}: {rev.question}
                </h3>
              </div>
              
              <svg class="h-5 w-5 text-slate-400 shrink-0 transform transition-transform duration-200 {expandedQuestionId === rev.id ? 'rotate-180' : ''}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>

            <!-- Question Review Body (Collapsible) -->
            {#if expandedQuestionId === rev.id}
              <div class="p-5 border-t border-slate-100 dark:border-slate-750 bg-slate-50/40 dark:bg-slate-900/20 space-y-5 text-sm">
                <!-- Options list review -->
                <div class="space-y-2">
                  {#each rev.options as option, idx}
                    {@const isUserSelected = rev.userAnswer.includes(idx)}
                    {@const isCorrect = rev.correctAnswer.includes(idx)}
                    
                    <div class="p-3.5 rounded-lg border flex items-start gap-3.5 leading-relaxed {isCorrect ? 'bg-green-50/60 dark:bg-green-950/10 border-green-200 dark:border-green-900/50 text-green-900 dark:text-green-300' : isUserSelected ? 'bg-rose-50/60 dark:bg-rose-950/10 border-rose-200 dark:border-rose-900/50 text-rose-900 dark:text-rose-450' : 'bg-white dark:bg-slate-900 border-slate-150 dark:border-slate-800 text-slate-650 dark:text-slate-350'}">
                      <span class="mt-0.5 shrink-0">
                        {#if isCorrect}
                          <!-- Correct Icon -->
                          <svg class="h-4.5 w-4.5 text-green-600 dark:text-green-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                          </svg>
                        {:else if isUserSelected}
                          <!-- Incorrect Icon -->
                          <svg class="h-4.5 w-4.5 text-rose-600 dark:text-rose-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M6 18L18 6M6 6l12 12" />
                          </svg>
                        {:else}
                          <!-- Neutral Bullet -->
                          <span class="h-2 w-2 rounded-full bg-slate-300 dark:bg-slate-700 inline-block mx-1"></span>
                        {/if}
                      </span>
                      
                      <div class="flex-1 font-medium">
                        {option}
                        {#if isUserSelected && isCorrect}
                          <span class="ml-2 text-xs font-mono font-bold text-green-600 dark:text-green-500">(Your correct choice)</span>
                        {:else if isUserSelected && !isCorrect}
                          <span class="ml-2 text-xs font-mono font-bold text-rose-600 dark:text-rose-500">(Your incorrect choice)</span>
                        {:else if !isUserSelected && isCorrect}
                          <span class="ml-2 text-xs font-mono font-bold text-green-600 dark:text-green-500">(Correct answer)</span>
                        {/if}
                      </div>
                    </div>
                  {/each}
                </div>

                <!-- Explanation Area -->
                <div class="p-4 bg-blue-50/50 dark:bg-slate-800/60 border border-blue-100 dark:border-slate-700/60 rounded-xl space-y-2 text-slate-750 dark:text-slate-300">
                  <h4 class="text-xs font-bold text-blue-700 dark:text-blue-450 uppercase tracking-wider">Architectural Explanation</h4>
                  <p class="leading-relaxed font-medium">
                    {rev.explanation}
                  </p>
                </div>
              </div>
            {/if}
          </div>
        {/each}
        
        {#if filteredReviews().length === 0}
          <div class="text-center py-12 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl text-slate-500 dark:text-slate-400">
            No questions match the current filter.
          </div>
        {/if}
      </div>
    </div>
  </div>
{/if}

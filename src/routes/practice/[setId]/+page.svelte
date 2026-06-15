<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  import { goto } from '$app/navigation';
  import { page } from '$app/state';

  let { data } = $props();
  const { setId, questions } = data;

  // Active state
  let currentIndex = $state(0);
  let selectedAnswers = $state<Record<string, number[]>>({}); // questionId -> list of selected indices
  let flaggedQuestions = $state<Record<string, boolean>>({}); // questionId -> boolean

  // Timer states (120 minutes = 7200 seconds)
  let timeRemaining = $state(120 * 60);
  let timerInterval: any = null;
  let startTime = Date.now();

  // Dialog State
  let showConfirmSubmit = $state(false);
  let isSidebarOpen = $state(true);

  // Derived calculations
  let currentQuestion = $derived(questions[currentIndex]);
  let answeredCount = $derived(
    Object.keys(selectedAnswers).filter(id => selectedAnswers[id] && selectedAnswers[id].length > 0).length
  );
  
  // Format seconds to HH:MM:SS
  let formattedTime = $derived(() => {
    const hours = Math.floor(timeRemaining / 3600);
    const minutes = Math.floor((timeRemaining % 3600) / 60);
    const seconds = timeRemaining % 60;
    return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
  });

  onMount(() => {
    // Start countdown
    timerInterval = setInterval(() => {
      if (timeRemaining > 0) {
        timeRemaining--;
      } else {
        // Time expired, auto-submit
        clearInterval(timerInterval);
        submitExam(true);
      }
    }, 1000);

    // Prompt user on refresh/close
    window.onbeforeunload = () => {
      return "Are you sure you want to leave? Your exam progress will be lost.";
    };
  });

  onDestroy(() => {
    if (timerInterval) clearInterval(timerInterval);
    if (typeof window !== 'undefined') {
      window.onbeforeunload = null;
    }
  });

  function selectOption(optionIdx: number) {
    const qId = currentQuestion.id;
    const isMulti = currentQuestion.type === 'multi';

    if (!selectedAnswers[qId]) {
      selectedAnswers[qId] = [];
    }

    if (isMulti) {
      // For multi-select: toggle selection
      if (selectedAnswers[qId].includes(optionIdx)) {
        selectedAnswers[qId] = selectedAnswers[qId].filter(idx => idx !== optionIdx);
      } else {
        selectedAnswers[qId] = [...selectedAnswers[qId], optionIdx];
      }
    } else {
      // For single-select: overwrite selection
      selectedAnswers[qId] = [optionIdx];
    }
  }

  function toggleFlag() {
    const qId = currentQuestion.id;
    flaggedQuestions[qId] = !flaggedQuestions[qId];
  }

  function goNext() {
    if (currentIndex < questions.length - 1) {
      currentIndex++;
    }
  }

  function goPrev() {
    if (currentIndex > 0) {
      currentIndex--;
    }
  }

  function submitExam(auto = false) {
    if (timerInterval) clearInterval(timerInterval);
    if (typeof window !== 'undefined') {
      window.onbeforeunload = null;
    }

    // Calculate score, category stats, and generate payload
    const totalQuestions = questions.length;
    let correctCount = 0;
    
    // Group categories for analytics
    const categoryStats: Record<string, { total: number; correct: number }> = {};

    const questionsReview = questions.map((q: any) => {
      const uAnswers = selectedAnswers[q.id] || [];
      
      // Determine correctness (all correct indices must be selected and no incorrect ones)
      const isCorrect = q.answer.length === uAnswers.length && 
                        q.answer.every((ans: number) => uAnswers.includes(ans));
      
      if (isCorrect) {
        correctCount++;
      }

      // Track domain category stats
      if (!categoryStats[q.category]) {
        categoryStats[q.category] = { total: 0, correct: 0 };
      }
      categoryStats[q.category].total++;
      if (isCorrect) {
        categoryStats[q.category].correct++;
      }

      return {
        id: q.id,
        question: q.question,
        options: q.options,
        correctAnswer: q.answer,
        userAnswer: uAnswers,
        isCorrect,
        category: q.category,
        explanation: q.explanation
      };
    });

    const finalPercent = Math.round((correctCount / totalQuestions) * 100);
    const timeSpentSecs = (120 * 60) - timeRemaining;
    const timeSpentMin = Math.floor(timeSpentSecs / 60);
    const timeSpentSec = timeSpentSecs % 60;
    const formattedTimeSpent = `${timeSpentMin}m ${timeSpentSec}s`;
    
    const dateStr = new Date().toLocaleDateString(undefined, { 
      year: 'numeric', month: 'short', day: 'numeric',
      hour: '2-digit', minute: '2-digit'
    });

    const isPassed = finalPercent >= 70;

    // 1. Save to sessionStorage for Results display page
    const resultsData = {
      setId,
      score: correctCount,
      total: totalQuestions,
      percent: finalPercent,
      timeSpent: formattedTimeSpent,
      date: dateStr,
      passed: isPassed,
      categoryStats,
      questionsReview
    };
    sessionStorage.setItem(`gcp_exam_results_${setId}`, JSON.stringify(resultsData));

    // 2. Save summary to localStorage attempts history
    try {
      const historyStr = localStorage.getItem('gcp_practice_attempts');
      const historyList = historyStr ? JSON.parse(historyStr) : [];
      historyList.push({
        setId,
        score: correctCount,
        total: totalQuestions,
        percent: finalPercent,
        timeSpent: formattedTimeSpent,
        date: dateStr,
        passed: isPassed
      });
      localStorage.setItem('gcp_practice_attempts', JSON.stringify(historyList));
    } catch (e) {
      console.error('Error saving attempt history:', e);
    }

    // Redirect to results page
    goto(`/practice/${setId}/results`);
  }
</script>

<div class="h-[calc(100vh-80px)] flex flex-col -m-6 md:-m-8 bg-slate-50 dark:bg-slate-950 overflow-hidden font-sans">
  <!-- Exam Session Topbar -->
  <header class="bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 px-6 py-4 flex items-center justify-between flex-shrink-0 z-10 shadow-sm">
    <div class="flex items-center gap-4">
      <a href="/practice" class="text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 transition-colors" title="Exit Exam">
        <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l-7-7m7-7" />
        </svg>
      </a>
      <div>
        <h1 class="text-lg font-bold text-slate-800 dark:text-white">GCP PCA Practice Set {setId}</h1>
        <div class="text-xs text-slate-400">
          Answered {answeredCount} of {questions.length} questions ({Math.round((answeredCount/questions.length)*100)}%)
        </div>
      </div>
    </div>

    <!-- Timer and Submission -->
    <div class="flex items-center gap-4">
      <div class="flex items-center gap-2 px-3 py-1.5 bg-slate-100 dark:bg-slate-800 rounded-lg font-mono font-bold text-sm text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 {timeRemaining < 600 ? 'text-rose-600 bg-rose-50 dark:bg-rose-950/20 border-rose-200 animate-pulse' : ''}">
        <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        {formattedTime()}
      </div>
      <button 
        onclick={() => showConfirmSubmit = true}
        class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-lg text-sm transition-colors shadow-sm"
      >
        Submit Exam
      </button>
    </div>
  </header>

  <!-- Progress Bar -->
  <div class="w-full bg-slate-200 dark:bg-slate-800 h-1 flex-shrink-0">
    <div class="bg-blue-600 h-1 transition-all duration-300" style="width: {(answeredCount / questions.length) * 100}%"></div>
  </div>

  <!-- Primary Workspace -->
  <div class="flex-1 flex overflow-hidden">
    <!-- Main Question Board -->
    <main class="flex-1 overflow-y-auto p-6 md:p-8 flex flex-col justify-between">
      <div class="max-w-3xl mx-auto w-full space-y-6">
        <!-- Question Meta -->
        <div class="flex items-center justify-between">
          <span class="text-xs font-semibold px-2.5 py-1 bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 rounded-md">
            Question {currentIndex + 1} of {questions.length}
          </span>
          <span class="text-xs font-bold text-blue-600 dark:text-blue-400 uppercase tracking-wide">
            {currentQuestion.type === 'multi' ? 'Multiple Choice (Select 2)' : 'Single Choice'}
          </span>
        </div>

        <!-- Question Category -->
        <div class="text-xs text-slate-400 italic font-medium">
          {currentQuestion.category}
        </div>

        <!-- Question Text -->
        <div class="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-xl p-6 shadow-sm">
          <p class="text-slate-800 dark:text-slate-100 text-base md:text-lg leading-relaxed font-medium">
            {currentQuestion.question}
          </p>
        </div>

        <!-- Options List -->
        <div class="space-y-3">
          {#each currentQuestion.options as option, idx}
            {@const isSelected = (selectedAnswers[currentQuestion.id] || []).includes(idx)}
            <button 
              onclick={() => selectOption(idx)}
              class="w-full text-left p-4 rounded-xl border transition-all text-sm md:text-base flex items-start gap-4 shadow-sm bg-white dark:bg-slate-900 hover:bg-slate-50 dark:hover:bg-slate-850/60 {isSelected ? 'border-blue-500 dark:border-blue-400 ring-2 ring-blue-500/20 dark:ring-blue-400/20 bg-blue-50/20 dark:bg-blue-900/10' : 'border-slate-200 dark:border-slate-850'}"
            >
              <!-- Input Decorator -->
              <span class="mt-0.5 shrink-0">
                {#if currentQuestion.type === 'multi'}
                  <!-- Checkbox -->
                  <span class="h-5.5 w-5.5 rounded border flex items-center justify-center {isSelected ? 'bg-blue-600 border-blue-600 text-white' : 'border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800'}">
                    {#if isSelected}
                      <svg class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                      </svg>
                    {/if}
                  </span>
                {:else}
                  <!-- Radio -->
                  <span class="h-5.5 w-5.5 rounded-full border flex items-center justify-center {isSelected ? 'bg-blue-600 border-blue-600 text-white' : 'border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800'}">
                    {#if isSelected}
                      <span class="h-2 w-2 bg-white rounded-full"></span>
                    {/if}
                  </span>
                {/if}
              </span>
              <span class="text-slate-700 dark:text-slate-200 leading-relaxed font-medium">{option}</span>
            </button>
          {/each}
        </div>
      </div>

      <!-- Action Panel Footer -->
      <footer class="max-w-3xl mx-auto w-full mt-8 pt-4 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between">
        <button 
          onclick={goPrev}
          disabled={currentIndex === 0}
          class="px-4 py-2 bg-white dark:bg-slate-900 hover:bg-slate-100 dark:hover:bg-slate-800 border border-slate-200 dark:border-slate-850 text-slate-700 dark:text-slate-300 text-sm font-semibold rounded-lg transition-colors flex items-center gap-2 disabled:opacity-40 disabled:hover:bg-white dark:disabled:hover:bg-slate-900"
        >
          <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
          Previous
        </button>

        <button 
          onclick={toggleFlag}
          class="px-4 py-2 border rounded-lg text-sm font-semibold transition-colors flex items-center gap-2 {flaggedQuestions[currentQuestion.id] ? 'bg-amber-50 dark:bg-amber-950/20 text-amber-700 dark:text-amber-400 border-amber-300' : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-850 text-slate-500 hover:bg-slate-100 dark:hover:bg-slate-800'}"
        >
          <svg class="h-4 w-4 fill-current {flaggedQuestions[currentQuestion.id] ? 'text-amber-500' : 'text-slate-450'}" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
          </svg>
          {flaggedQuestions[currentQuestion.id] ? 'Flagged for Review' : 'Flag Question'}
        </button>

        <button 
          onclick={goNext}
          disabled={currentIndex === questions.length - 1}
          class="px-4 py-2 bg-white dark:bg-slate-900 hover:bg-slate-100 dark:hover:bg-slate-800 border border-slate-200 dark:border-slate-850 text-slate-700 dark:text-slate-300 text-sm font-semibold rounded-lg transition-colors flex items-center gap-2 disabled:opacity-40 disabled:hover:bg-white dark:disabled:hover:bg-slate-900"
        >
          Next
          <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </button>
      </footer>
    </main>

    <!-- Right Grid Navigation Sidebar -->
    {#if isSidebarOpen}
      <aside class="w-80 border-l border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 flex flex-col flex-shrink-0 relative shadow-sm">
        <div class="p-4 border-b border-slate-200 dark:border-slate-800 flex items-center justify-between">
          <span class="text-sm font-bold text-slate-700 dark:text-slate-300">Question Board Map</span>
          <button 
            onclick={() => isSidebarOpen = false}
            class="p-1 rounded hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-400"
            title="Collapse panel"
          >
            <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
          </button>
        </div>

        <!-- Grid Container -->
        <div class="flex-1 overflow-y-auto p-4">
          <div class="grid grid-cols-5 gap-2.5">
            {#each questions as q, idx}
              {@const qId = q.id}
              {@const isAnswered = selectedAnswers[qId] && selectedAnswers[qId].length > 0}
              {@const isFlagged = flaggedQuestions[qId]}
              {@const isActive = idx === currentIndex}
              
              <button 
                onclick={() => currentIndex = idx}
                class="aspect-square flex flex-col items-center justify-center rounded-lg border text-xs font-mono font-semibold transition-all relative {isActive ? 'border-blue-600 dark:border-blue-400 ring-2 ring-blue-500/20 scale-105' : 'border-slate-200 dark:border-slate-800'} {isAnswered ? 'bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-400' : 'bg-slate-50 dark:bg-slate-900/30 text-slate-500 dark:text-slate-450'}"
              >
                {idx + 1}
                {#if isFlagged}
                  <span class="absolute top-0.5 right-0.5 h-1.5 w-1.5 rounded-full bg-amber-500"></span>
                {/if}
              </button>
            {/each}
          </div>
        </div>

        <!-- Color Legend Info -->
        <div class="p-4 border-t border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-900/60 text-[11px] text-slate-500 dark:text-slate-400 space-y-2">
          <div class="flex items-center gap-2">
            <span class="h-3 w-3 rounded bg-blue-50 dark:bg-blue-900/20 border border-blue-200 dark:border-blue-800 inline-block"></span>
            <span>Answered Question</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="h-3 w-3 rounded bg-slate-50 dark:bg-slate-900/30 border border-slate-200 dark:border-slate-800 inline-block relative">
              <span class="absolute top-0.5 right-0.5 h-1.5 w-1.5 rounded-full bg-amber-500"></span>
            </span>
            <span>Flagged for Review</span>
          </div>
        </div>
      </aside>
    {:else}
      <!-- Floating Sidebar Opener -->
      <button 
        onclick={() => isSidebarOpen = true}
        class="absolute right-4 top-20 p-2.5 bg-blue-600 hover:bg-blue-700 text-white rounded-full shadow-lg z-20 flex items-center justify-center transition-transform hover:scale-105"
        title="Open Question Board Map"
      >
        <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
      </button>
    {/if}
  </div>

  <!-- Confirm Submit Modal Overlay -->
  {#if showConfirmSubmit}
    <div class="fixed inset-0 z-50 flex items-center justify-center bg-black/55 backdrop-blur-sm p-4 animate-fade-in">
      <div class="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 max-w-md w-full rounded-xl p-6 shadow-xl space-y-4">
        <h3 class="text-xl font-bold text-slate-900 dark:text-white">Confirm Submission</h3>
        <p class="text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
          Are you sure you want to finish and submit your practice exam? You will not be able to change your answers after submission.
        </p>

        {#if answeredCount < questions.length}
          <div class="p-3 bg-rose-50 dark:bg-rose-950/20 border border-rose-200 dark:border-rose-900/50 rounded-lg text-rose-700 dark:text-rose-450 text-xs font-semibold">
            Warning: You have {questions.length - answeredCount} unanswered questions out of {questions.length}.
          </div>
        {/if}

        <div class="flex items-center justify-end gap-3 pt-2">
          <button 
            onclick={() => showConfirmSubmit = false}
            class="px-4 py-2 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-350 hover:bg-slate-100 dark:hover:bg-slate-800 text-sm font-semibold rounded-lg transition-colors"
          >
            Cancel
          </button>
          <button 
            onclick={() => { showConfirmSubmit = false; submitExam(); }}
            class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white text-sm font-semibold rounded-lg transition-colors shadow-sm"
          >
            Yes, Submit Exam
          </button>
        </div>
      </div>
    </div>
  {/if}
</div>

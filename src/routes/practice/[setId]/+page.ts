import { error } from '@sveltejs/kit';
import questionsData from '$lib/data/practice_questions.json';

interface Question {
  id: string;
  type: string;
  category: string;
  question: string;
  options: string[];
  answer: number[];
  explanation: string;
}

export function load({ params }: { params: { setId: string } }) {
  const setId = parseInt(params.setId, 10);
  if (isNaN(setId) || setId < 1 || setId > 5) {
    throw error(404, 'Practice set not found');
  }

  // Filter questions for this set
  const setQuestions = (questionsData as Question[]).filter(q => 
    q.id.startsWith(`q-${setId}-`)
  );

  if (setQuestions.length === 0) {
    throw error(404, 'No questions found for this set');
  }

  // Helper to shuffle an array (Fisher-Yates)
  function shuffleArray<T>(array: T[]): T[] {
    const arr = [...array];
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  // Process and shuffle each question's options, re-mapping correct answers
  const processedQuestions = setQuestions.map(q => {
    // Pack options with their original correctness metadata
    const optionsMetadata = q.options.map((text, index) => ({
      text,
      isCorrect: q.answer.includes(index)
    }));

    // Shuffle the options
    const shuffledMetadata = shuffleArray(optionsMetadata);

    // Reconstruct shuffled options list and retrieve new indices of correct answers
    const shuffledOptions = shuffledMetadata.map(o => o.text);
    const newAnswerIndices = shuffledMetadata.reduce((acc: number[], o, idx) => {
      if (o.isCorrect) acc.push(idx);
      return acc;
    }, []);

    return {
      ...q,
      options: shuffledOptions,
      answer: newAnswerIndices
    };
  });

  // Shuffle the entire questions pool so order is fully random
  const shuffledQuestions = shuffleArray(processedQuestions);

  return {
    setId,
    questions: shuffledQuestions
  };
}

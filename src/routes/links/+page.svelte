<script lang="ts">
  const categories = [
    {
      title: "Official Case Study PDFs",
      description: "Direct links to the 4 official fictitious business cases tested on the PCA exam.",
      color: "from-blue-500/10 to-indigo-500/10 dark:from-blue-500/20 dark:to-indigo-500/20",
      icon: `<svg class="h-6 w-6 text-blue-600 dark:text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
               <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
             </svg>`,
      links: [
        {
          name: "Altostrat Media Case Study",
          description: "Media & content delivery company focused on scaling transcoding, multi-region database replication, and hybrid-cloud media delivery pipelines.",
          url: "https://services.google.com/fh/files/misc/v6.1_pca_altostrat_media_case_study_english.pdf",
          label: "altostrat-media",
          badge: "PDF"
        },
        {
          name: "Cymbal Retail Case Study",
          description: "Global brick-and-mortar retail business transitioning to cloud-native e-commerce, real-time inventory management, and personalized AI shopping assistants.",
          url: "https://services.google.com/fh/files/misc/v6.1_pca_cymbal_retail_case_study_english.pdf",
          label: "cymbal-retail",
          badge: "PDF"
        },
        {
          name: "EHR Healthcare Case Study",
          description: "Healthcare insurer modernizing legacy applications to microservices on GKE, requiring strict HIPAA compliance, KMS encryption, and secure disaster recovery.",
          url: "https://services.google.com/fh/files/misc/v6.1_pca_ehr_healthcare_case_study_english.pdf",
          label: "ehr-healthcare",
          badge: "PDF"
        },
        {
          name: "KnightMotives Automotive Case Study",
          description: "Automotive manufacturer launching connected vehicle APIs, processing high-volume telematics streaming data via Pub/Sub and Bigtable in rural locations.",
          url: "https://services.google.com/fh/files/misc/v6.1_pca_knightmotives_automotive_case_study_english.pdf",
          label: "knightmotives-automotive",
          badge: "PDF"
        }
      ]
    },
    {
      title: "Architecture Guides & Frameworks",
      description: "Official Google Cloud design patterns, architectural principles, and exam blueprints.",
      color: "from-emerald-500/10 to-teal-500/10 dark:from-emerald-500/20 dark:to-teal-500/20",
      icon: `<svg class="h-6 w-6 text-emerald-600 dark:text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
               <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
             </svg>`,
      links: [
        {
          name: "Google Cloud Well-Architected Framework",
          description: "Comprehensive guidance covering the 6 pillars: Operational Excellence, Security, Reliability, Performance, Cost, and Sustainability.",
          url: "https://cloud.google.com/architecture",
          badge: "Official Docs"
        },
        {
          name: "Professional Cloud Architect Exam Guide",
          description: "Official exam objectives outline and description of knowledge areas tested in the certification exam.",
          url: "https://cloud.google.com/learn/certification/guides/professional-cloud-architect",
          badge: "Official Guide"
        }
      ]
    },
    {
      title: "Exam Practice & Training Platforms",
      description: "Official interactive learning paths and high-yield video practice explanations.",
      color: "from-purple-500/10 to-pink-500/10 dark:from-purple-500/20 dark:to-pink-500/20",
      icon: `<svg class="h-6 w-6 text-purple-600 dark:text-purple-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
               <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
             </svg>`,
      links: [
        {
          name: "Google Cloud Skills Boost",
          description: "Hands-on labs, structured quest courses, and practice learning paths for cloud engineering and architecture.",
          url: "https://www.cloudskillsboost.google",
          aliasUrl: "skills.google.com",
          badge: "Practice Labs"
        },
        {
          name: "GCP Practice Exam Video Walkthrough",
          description: "High-yield video breakdown analyzing official practice exam questions, solution design steps, and exam strategies.",
          url: "https://www.youtube.com/watch?v=BMr-po8LpM0",
          badge: "Video Tutorial"
        }
      ]
    }
  ];
</script>

<svelte:head>
  <title>Links & Resources | GCP Architect Hub</title>
</svelte:head>

<div class="max-w-6xl mx-auto space-y-10 pb-16">
  <!-- Hero Section -->
  <div class="bg-white dark:bg-slate-800 p-8 md:p-12 rounded-3xl border border-slate-200 dark:border-slate-700 shadow-sm relative overflow-hidden">
    <div class="absolute inset-0 bg-gradient-to-r from-blue-500/5 to-indigo-500/5 dark:from-blue-500/10 dark:to-indigo-500/10 pointer-events-none"></div>
    <div class="relative z-10 max-w-3xl">
      <h1 class="text-4xl font-extrabold text-slate-900 dark:text-white mb-4 tracking-tight">
        Study Links & Resources
      </h1>
      <p class="text-lg text-slate-600 dark:text-slate-350 leading-relaxed">
        Access official guides, case study PDFs, hands-on learning resources, and exam prep walk-throughs. Use these resources in tandem with our architecture hub mappings to prepare for the Google Cloud Professional Cloud Architect exam.
      </p>
    </div>
  </div>

  <!-- Category List -->
  <div class="space-y-10">
    {#each categories as cat}
      <div class="space-y-4">
        <!-- Category Title -->
        <div class="flex items-center gap-3">
          <div class="p-2.5 rounded-xl bg-gradient-to-br {cat.color}">
            {@html cat.icon}
          </div>
          <div>
            <h2 class="text-2xl font-bold text-slate-900 dark:text-white tracking-tight">{cat.title}</h2>
            <p class="text-sm text-slate-500 dark:text-slate-400">{cat.description}</p>
          </div>
        </div>

        <!-- Links Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          {#each cat.links as link}
            <a 
              href={link.url}
              target="_blank"
              rel="noopener noreferrer"
              class="group block bg-white dark:bg-slate-800 p-6 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm hover:shadow-md hover:border-blue-500 dark:hover:border-blue-500/60 transition-all duration-200"
            >
              <div class="flex flex-col h-full justify-between space-y-4">
                <div class="space-y-2">
                  <div class="flex justify-between items-start gap-4">
                    <h3 class="font-bold text-slate-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-blue-450 transition-colors leading-tight">
                      {link.name}
                    </h3>
                    <span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-semibold bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 group-hover:bg-blue-50 dark:group-hover:bg-blue-900/30 group-hover:text-blue-700 dark:group-hover:text-blue-300 transition-colors whitespace-nowrap">
                      {link.badge}
                    </span>
                  </div>
                  <p class="text-sm text-slate-600 dark:text-slate-355 leading-relaxed line-clamp-3">
                    {link.description}
                  </p>
                </div>

                <div class="flex items-center justify-between pt-2 text-xs font-semibold text-slate-500 dark:text-slate-400 group-hover:text-blue-600 dark:group-hover:text-blue-450 transition-colors">
                  <span class="truncate pr-4 max-w-[280px]">
                    {(link as any).aliasUrl || link.url}
                  </span>
                  <span class="flex items-center gap-1 shrink-0">
                    <span>Visit resource</span>
                    <svg class="h-3.5 w-3.5 transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                    </svg>
                  </span>
                </div>
              </div>
            </a>
          {/each}
        </div>
      </div>
    {/each}
  </div>
</div>

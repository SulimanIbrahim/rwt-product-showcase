# RWT Product Showcase — Part 2: Screenshot Capture Prompts for Claude

**Repo:** `SulimanIbrahim/rwt-product-showcase`
**Approach:** After the animated HTML pages are built (Part 1), Claude generates capture instructions for specific frames at key moments. The browser renders the HTML page, pauses at the specified scene, and takes a high-resolution screenshot. These screenshots go on redwhite.tech with Microsoft Dynamics 365-style captions.

---

## How Screenshots Are Captured

1. Open the HTML demo page in browser at 1920x1080
2. Using the scene manager's pause functionality (each scene should have a data attribute `data-scene="N"`), pause at specific scenes
3. Take screenshot at 2x resolution (3840x2160) for retina displays
4. Compress to WebP for web delivery
5. Overlay RWT watermark bottom-right

## Brand Guidelines (Captions)
- Font: Inter, 14px, color #666666
- Caption style: Bold headline (what this shows) + 1 sentence explanation
- Example: **Smart Inventory Dashboard** — AI predicts stock levels and auto-generates restock alerts in real time.

---

## NexArena — Screenshot Capture Points (6 screenshots)

### NA-SCREEN-01: Hero Banner
**Scene:** 2 seconds in (right after title animation completes)
**What to capture:** Full hero section with "NexArena" title, tagline, 3D rotating model, and pulsing CTA
**Caption:** **NexArena Hero** — The AI-Native Game Commerce Engine. Powered by RedWhiteTech.

### NA-SCREEN-02: Smart Inventory Dashboard
**Scene:** 12 seconds in (inventory fully loaded)
**What to capture:** Dashboard with live inventory numbers, AI restock alert, sparkline charts
**Caption:** **AI-Powered Inventory Management** — Predict demand, optimize stock levels, and automate restocking across 45+ countries.

### NA-SCREEN-03: AI Game Recommendations
**Scene:** 19 seconds in (all recommendation cards visible)
**What to capture:** Gamer profile + recommendation cards with match percentages
**Caption:** **Personalized Game Recommendations** — AI analyzes player behavior to surface the right games. 34% higher engagement.

### NA-SCREEN-04: Dynamic Pricing Engine
**Scene:** 27 seconds in (optimal price highlighted)
**What to capture:** Pricing dashboard with live prices, competitor comparison, revenue projection
**Caption:** **AI Dynamic Pricing** — Adjust prices in real-time based on demand, competition, and market trends. 15-minute update cycles.

### NA-SCREEN-05: Anti-Fraud AI Shield
**Scene:** 49 seconds in (fraud detection rules fully displayed)
**What to capture:** Split view showing fraud prevention in action, blocked transactions, shield animation
**Caption:** **Enterprise-Grade Fraud Prevention** — AI detects and blocks fraudulent transactions. AED 2.4M saved for clients.

### NA-SCREEN-06: Global Scale
**Scene:** 64 seconds in (world map fully loaded)
**What to capture:** Global deployment map, stats, server health indicators
**Caption:** **Operating at Global Scale** — 12M+ games delivered, 2,800+ stores powered, 99.99% uptime. Built for enterprise.

---

## PeoplePulse — Screenshot Capture Points (6 screenshots)

### PP-SCREEN-01: Hero
**Scene:** 3 seconds in
**What to capture:** PeoplePulse title with pulse animation, tagline, 3D human figure
**Caption:** **PeoplePulse — HR That Thinks Ahead** — AI-powered talent management from hiring to retention.

### PP-SCREEN-02: AI Resume Screening
**Scene:** 12 seconds in (top matches displayed)
**What to capture:** Resume stack with AI filtering, match percentages, bias-filtered badge
**Caption:** **AI Resume Screening** — Process 847 resumes in 4.2 seconds. Bias-filtered, skills-matched, ready for review.

### PP-SCREEN-03: Talent Analytics Dashboard
**Scene:** 19 seconds in (heatmap and retention alerts visible)
**What to capture:** Org chart, skill gap heatmap, retention risk alerts
**Caption:** **Workforce Intelligence** — Visualize skill gaps, predict retention risks, and plan headcount with AI-powered analytics.

### PP-SCREEN-04: Employee Sentiment
**Scene:** 32 seconds in (sentiment word cloud formed)
**What to capture:** Sentiment dashboard, pulse survey results, word cloud
**Caption:** **Real-Time Employee Sentiment** — Anonymous AI-analyzed feedback. Detect trends before they become problems.

### PP-SCREEN-05: Automated Onboarding
**Scene:** 25 seconds in (onboarding checklist mid-completion)
**What to capture:** Onboarding timeline, document signing, welcome message
**Caption:** **AI-Automated Onboarding** — Reduce onboarding from 14 days to 3 days. Every step tracked and automated.

### PP-SCREEN-06: Compliance Dashboard
**Scene:** 53 seconds in (all compliance checks green)
**What to capture:** Compliance dashboard, document expiry alerts, audit trail
**Caption:** **100% Audit-Ready Compliance** — UAE Labor Law, GDPR, ISO-aligned. Every action logged and reportable.

---

## FlowForge — Screenshot Capture Points (6 screenshots)

### FF-SCREEN-01: Hero
**Scene:** 4 seconds in
**What to capture:** FlowForge title assembled, tagline, 3D project network
**Caption:** **FlowForge — Projects That Manage Themselves** — AI-native project orchestration for teams that ship.

### FF-SCREEN-02: AI Task Prioritization
**Scene:** 12 seconds in (kanban fully auto-sorted)
**What to capture:** Auto-populated Kanban board with AI priority indicators
**Caption:** **AI Task Prioritization** — 23 tasks auto-scheduled in 0.8 seconds. Blockers flagged before they delay.

### FF-SCREEN-03: Predictive Deadlines
**Scene:** 19 seconds in (Gantt chart with predictions)
**What to capture:** Gantt chart, deadline predictions with confidence %, risk indicator
**Caption:** **Predictive Deadlines** — 94% prediction accuracy. Know which deadlines are at risk weeks in advance.

### FF-SCREEN-04: Resource Optimization
**Scene:** 27 seconds in (workload balanced)
**What to capture:** Team workload cards, reassignment arrows, cost savings counter
**Caption:** **AI Resource Optimization** — Balance workloads in 3 moves. AED 147K average savings per project.

### FF-SCREEN-05: Risk Detection Radar
**Scene:** 43 seconds in (risk radar with active alerts)
**What to capture:** 360-degree risk radar, mitigation cards, early warning notification
**Caption:** **Proactive Risk Detection** — 87% of risks flagged before they become issues. Sleep better at night.

### FF-SCREEN-06: Integration Ecosystem
**Scene:** 64 seconds in (all integrations displayed)
**What to capture:** Integration icons circling FlowForge, data sync animation
**Caption:** **150+ Integrations** — GitHub, Jira, Slack, Figma, Teams. Connected in under 3 minutes.

---

## ServClaw — Screenshot Capture Points (6 screenshots)

### SC-SCREEN-01: Hero
**Scene:** 3 seconds in
**What to capture:** ServClaw title with claw animation, tagline, 3D robotic arm
**Caption:** **ServClaw — Deploy AI Agents Into Your Business. Instantly.** — Harness-powered agent management.

### SC-SCREEN-02: One-Click Deployment
**Scene:** 12 seconds in (deployment complete)
**What to capture:** Terminal interface, progress bar at 100%, "Agent deployed in 4.7 seconds"
**Caption:** **One-Click Agent Deployment** — Deploy production AI agents in under 5 seconds. Zero infrastructure setup.

### SC-SCREEN-03: Agent Fleet Management
**Scene:** 20 seconds in (fleet dashboard fully loaded)
**What to capture:** Agent cards grid, auto-scaling visualization, resource usage bars
**Caption:** **Agent Fleet Dashboard** — Manage, scale, and monitor all your AI agents from a single pane of glass.

### SC-SCREEN-04: CI/CD Pipeline Integration
**Scene:** 28 seconds in (canary deployment progressing)
**What to capture:** Pipeline visualization, canary deployment traffic shifting, Harness logo
**Caption:** **CI/CD Native** — Agents deploy automatically after every successful build. Integrated with your pipeline.

### SC-SCREEN-05: Automated Governance
**Scene:** 36 seconds in (approval flow complete)
**What to capture:** Policy cards, approval chain, compliance score, audit trail
**Caption:** **Automated Governance** — Every agent action is logged, reviewed, and auditable. ISO 27001 compliant.

### SC-SCREEN-06: Security & Compliance
**Scene:** 55 seconds in (security layers displayed)
**What to capture:** Security layers around agent, encryption badges, data residency map
**Caption:** **Enterprise-Grade Security** — AES-256, TLS 1.3, UAE sovereign cloud. Built for regulated industries.

---

## CogniVerse — Screenshot Capture Points (6 screenshots)

### CV-SCREEN-01: Hero
**Scene:** 3 seconds in
**What to capture:** CogniVerse title with universe animation, tagline, 3D neural network
**Caption:** **CogniVerse — Where Learning Meets Intelligence** — AI-powered learning experience platform.

### CV-SCREEN-02: AI-Personalized Learning Paths
**Scene:** 12 seconds in (path fully generated)
**What to capture:** Learner profile, AI-generated learning path, skill spider chart
**Caption:** **Personalized Learning Paths** — AI crafts unique learning journeys based on role, goals, and current skills.

### CV-SCREEN-03: Adaptive Assessments
**Scene:** 20 seconds in (knowledge map updating)
**What to capture:** Quiz interface, knowledge map with green nodes, mastery percentage
**Caption:** **Adaptive Assessments** — Questions adapt to each learner. 200% more effective than fixed testing.

### CV-SCREEN-04: Intelligent Content Generation
**Scene:** 28 seconds in (content generated)
**What to capture:** AI content studio with generated lesson, format tabs, language option
**Caption:** **AI Content Studio** — Generate lessons, quizzes, and flashcards in 12 seconds. Arabic and English.

### CV-SCREEN-05: Virtual AI Tutor
**Scene:** 43 seconds in (tutor explaining concept)
**What to capture:** Chat interface, code example, AI explanation, code playground
**Caption:** **24/7 AI Tutor** — Students get instant help in Arabic or English. Every question answered, anytime.

### CV-SCREEN-06: Gamification & Engagement
**Scene:** 50 seconds in (achievement celebration)
**What to capture:** Badge unlock animation, leaderboard, skill tree, streak fire
**Caption:** **Engagement That Lasts** — Gamification increases course completion by 47%. Learning that feels like progress.

---

## Screenshot Capture Technical Notes

### Browser Screenshot Method
```javascript
// In browser console after pausing at desired scene:
// Method 1: Using html2canvas library
html2canvas(document.body, { scale: 2 }).then(canvas => {
  canvas.toBlob(blob => {
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'screenshot.png';
    a.click();
  });
});

// Method 2: Using Puppeteer (from Node.js)
// await page.screenshot({ path: 'screenshot.png', fullPage: false, type: 'png' });
```

### File Naming Convention
- `nexarena-hero.webp`
- `nexarena-inventory.webp`
- `nexarena-recommendations.webp`
- etc.

### Dimensions & Format
- Captured: 3840x2160 (retina 2x)
- Delivered: 1920x1080 WebP (quality 85)
- Max file size: 300KB per screenshot
- Use for website: `<img src="..." loading="lazy" width="1920" height="1080">`

---

## Total: 30 Screenshots (6 per product × 5 products)

| Product | Code | Screenshots |
|---------|------|-------------|
| NexArena | NA | Hero, Inventory, Recommendations, Pricing, Fraud, Scale |
| PeoplePulse | PP | Hero, Resume Screening, Analytics, Sentiment, Onboarding, Compliance |
| FlowForge | FF | Hero, Task Prioritization, Deadlines, Resources, Risk, Integrations |
| ServClaw | SC | Hero, Deployment, Fleet, CI/CD, Governance, Security |
| CogniVerse | CV | Hero, Learning Paths, Assessments, Content Gen, AI Tutor, Gamification |

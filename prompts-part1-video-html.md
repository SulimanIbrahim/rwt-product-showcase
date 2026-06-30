# RWT Product Showcase — Part 1: Animated HTML Demo Prompts for Claude

**Repo:** `SulimanIbrahim/rwt-product-showcase`
**Approach:** Claude generates animated HTML/CSS/Three.js pages → browser screen recording → MP4 video
Reference: Suliman's HTML animation style (layered CSS + Three.js 3D elements)

---

## Brand Guidelines (all products)
- Red: `#C21A0C` | Dark: `#1A1A1A` | Gray: `#666666` | BG: `#FFFFFF` / `#F5F5F5`
- Font: Inter (Google Fonts CDN)
- RWT logo in header/footer
- "Contact Sales" CTA buttons throughout
- Style: Microsoft Dynamics 365 enterprise SaaS aesthetic
- Animation: CSS @keyframes + Three.js CDN 3D + JS auto-advance scene timer
- Resolution: 1920x1080 | Dark theme preferred | 75-85 seconds auto-play

---

## Prompt 1: NexArena — AI-Powered Game Commerce Platform

**Tagline:** "The AI-Native Game Commerce Engine"

### Claude Prompt:

```
Create a single self-contained HTML file for NexArena — an AI-powered game commerce platform product demo by RedWhiteTech. This page will be screen-recorded into a product video. Must be highly animated and interactive.

Technical: No dependencies except Three.js CDN and Inter font from Google Fonts. All CSS and JS inline. Resolution 1920x1080. Dark theme.

REQUIRED AUTO-PLAY SCENE SEQUENCE (75-85 seconds total):

SCENE 1 (0-8s): Hero
- "NexArena" fades in letter-by-letter with staggered animation
- Tagline "The AI-Native Game Commerce Engine" slides up from below
- Three.js 3D rotating geometric shape (gold/red tones, gamepad-like)
- "Contact Sales" CTA button pulses with red glow (#C21A0C)
- Background: dark gradient with subtle floating particle icons (game controllers, keys, cart)
- Red accent line animates across the bottom

SCENE 2 (8-15s): Smart Inventory Dashboard
- Dashboard panel slides in from right with CSS transform
- Inventory numbers count up: "12,847 games in stock"
- AI prediction badge appears with red pulse: "Restock Alert: FIFA 26 — 48 hours"
- Mini sparkline charts draw themselves (JS canvas or CSS)
- Auto-cursor moves to highlight the AI recommendation section
- "92% stock accuracy" badge with green check

SCENE 3 (15-22s): AI Game Recommendations
- Left panel: gamer profile card (avatar placeholder, genres, history)
- Right panel: recommendation cards slide in with stagger (each 0.3s delay)
- Each card shows: game cover placeholder, "98% Match" circle animation, price
- "Why recommended?" tooltip appears on auto-hover
- Conversion stat pulses: "+34% engagement from AI recommendations"

SCENE 4 (22-30s): Dynamic Pricing Engine
- Pricing table with live-updating numbers (JS intervals)
- Prices animate up/down based on simulated demand
- Competitor price bars: NexArena vs Market — ours highlighted green at lower price
- "Optimal Price: AED 239" badge with animated border
- Revenue projection line draws across months with upward trend
- "AI adjusts prices every 15 minutes" info card

SCENE 5 (30-38s): Digital Key Delivery System
- Digital key card animates in with glow effect
- Delivery speed counter: races from 0 to 2.3 seconds
- World map (simplified CSS/JS) with delivery nodes lighting up globally
- Security badges slide in: Encrypted, Verified, Instant
- "99.97% delivery success rate" stat
- Customer rating: 4.8/5 stars animate in one by one

SCENE 6 (38-45s): Gamer Analytics Dashboard
- Full-width analytics with animated charts
- Player retention curve draws smoothly over 90 days
- "87% repeat purchase rate" highlighted
- AI insight box: "Players who buy RPGs are 3x more likely to purchase within 7 days"
- Realtime activity feed scrolls on the side
- Revenue per user bar chart animates height

SCENE 7 (45-52s): Anti-Fraud AI Shield
- Split screen: left = fraud attempts (red glow), right = clean transactions (green)
- Fraud detection rules appear as cards that light up when triggered
- Metrics: "AED 2.4M fraud prevented" counter
- Shield icon with pulsing protection ring animation
- Blocked transaction log auto-scrolls
- "47,000+ attacks blocked this month"

SCENE 8 (52-60s): Developer Integration
- Code editor style view: REST API endpoint code types itself (JS typing effect)
- Integration logos scroll horizontally: Steam, Epic, PlayStation, Xbox Store
- "Go live in under 48 hours" with countdown-style animation
- API response: JSON auto-formats and colorizes
- SDK language options flash: Python, Node.js, PHP, Java

SCENE 9 (60-68s): Global Scale
- World map with connected nodes (Three.js particles on a globe shape)
- Stats cascade: "12M+ Games Delivered" → "45+ Countries" → "10,000+ Developers"
- Server health dashboard: all green indicators
- 99.99% uptime displayed with animated bars
- Client ecosystem: number counts up "2,800+ stores powered by NexArena"

SCENE 10 (68-75s): CTA Finale
- All features collapse into elegant grid summary
- NexArena logo center with 3D rotation (Three.js)
- Main CTA: "Power Your Game Store With AI" large button
- Secondary: "Request Demo" button below
- Contact info: phone, email, website
- Red White Tech branding: logo, "RAKEZ, Ras Al Khaimah, UAE"

TECHNICAL SPECS:
- Use Three.js CDN: <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
- CSS animations: @keyframes for all movements, opacity transitions
- JS scene manager: auto-advance timer, scene counter, smooth crossfade transitions
- Particles: Three.js particle system in background (floating dots, ~200 particles, slow drift)
- Font: <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap">
- All colors use CSS variables at :root level
- Include hidden "REPLAY" button appearing at sequence end
- Ensure no scrollbars — everything fits 1920x1080 viewport
- Use requestAnimationFrame for smooth animations
```

---

## Prompt 2: PeoplePulse — Intelligent HR & Talent Management

**Tagline:** "HR That Thinks Ahead"

### Claude Prompt:

```
Create a single self-contained HTML file for PeoplePulse — an AI-powered HR and talent management platform by RedWhiteTech. This page will be screen-recorded into a product video.

Same technical requirements as NexArena: self-contained HTML, Three.js CDN, Inter font, 1920x1080, dark theme, 75-85 second auto-play sequence.

SCENE SEQUENCE:

SCENE 1 (0-7s): Hero
- "PeoplePulse" title with pulse animation (scale up/down slightly)
- "HR That Thinks Ahead" tagline fades in
- 3D rotating abstract human figure (Three.js geometric shapes)
- Red CTA: "Contact Sales"
- Background: dark with subtle heartbeat-like pulse rings

SCENE 2 (7-14s): AI Resume Screening
- Resume stack on left, AI processing animation on right
- Resumes flip through rapidly like cards
- AI highlights matching skills in green on each pass
- Counter: "847 resumes → 23 top matches in 4.2 seconds"
- Match percentages appear next to filtered candidates
- "Bias-filtered" badge with shield icon

SCENE 3 (14-21s): Talent Analytics Dashboard
- Org chart with animated connections
- Skill gap heatmap: departments color-coded (red = critical gap, green = strong)
- "Retention risk" alerts: 3 employees flagged with risk scores
- Headcount trends chart draws upward
- "Time-to-hire reduced by 62%" stat highlight
- Demographic distribution pie chart animates

SCENE 4 (21-28s): Automated Onboarding Flow
- Onboarding checklist: items auto-check one by one
- New hire profile card appears with animation
- "Day 1" through "Day 90" journey timeline animates
- Document signing simulation: signature appears on form
- Welcome message auto-types in company chat preview
- "Onboarding time: 14 days → 3 days" comparison

SCENE 5 (28-35s): Employee Sentiment Analysis
- Sentiment dashboard: emoji gauges across departments
- Pulse survey responses animate in real-time
- Word cloud forms from employee feedback keywords
- Alert: "Engineering team sentiment trending down — suggested action"
- Historical sentiment line chart draws
- "Anonymous, AI-analyzed, bias-free" trust badge

SCENE 6 (35-42s): Workforce Planning
- Future headcount projection: bars grow month by month
- Department budget allocation: animated donut chart
- "AI recommends: 3 senior engineers, 2 PMs for Q3 projects"
- Skills inventory: employees mapped to required skills (auto-connecting lines)
- Cost projection: numbers scroll as scenario switches

SCENE 7 (42-49s): Performance Management
- Employee performance dashboard
- 360-review completion rate: "94% participation"
- Goal tracking: progress bars fill with color coding
- Peer recognition feed scrolls: "Ahmed recognized by Sarah for..."
- Promotion readiness indicator: "12 employees flagged for advancement"
- Performance bell curve normalizes with animation

SCENE 8 (49-56s): Compliance & Reporting
- Compliance dashboard with green checkmarks
- Document expiry alerts: "3 contracts expiring in 30 days"
- Audit trail log auto-scrolls with timestamps
- Region-specific compliance: UAE labor law, GDPR, ISO badges
- Report auto-generates: PDF icon animates creation
- "100% audit-ready" badge

SCENE 9 (56-63s): Employee Self-Service Portal
- Mobile-responsive view (phone frame in center)
- Employee tapping through: leave request → instant approval animation
- Payslip view: numbers animate with breakdown
- "Request time off" flow: calendar → submit → "Approved in 2 minutes"
- Learning module recommendations appear
- "90% employee satisfaction with self-service"

SCENE 10 (63-72s): Enterprise Scale + CTA
- Global deployment: "Operating in 15 countries, 50,000+ employees managed"
- Security certifications animate in: ISO 27001, SOC 2, GDPR, UAE PDPL
- Integration logos: SAP, Oracle, Microsoft 365, Slack
- "HR That Thinks Ahead" tagline re-appears
- CTA: "Transform Your HR With AI — Contact Sales"
- RWT branding footer

TECHNICAL: Same as NexArena — Three.js CDN, Inter font, CSS @keyframes, JS scene timer, particles, crossfade transitions.
```

---

## Prompt 3: FlowForge — AI-Native Project Orchestration

**Tagline:** "Projects That Manage Themselves"

### Claude Prompt:

```
Create a self-contained HTML file for FlowForge — an AI-native project management and orchestration platform by RedWhiteTech. Screen-recordable product demo page.

Same specs: self-contained HTML, Three.js CDN, Inter font, 1920x1080, dark theme, 75-85 seconds.

SCENE SEQUENCE:

SCENE 1 (0-8s): Hero
- "FlowForge" title assembles from floating geometric pieces
- "Projects That Manage Themselves" types out
- 3D rotating project structure (Three.js: interconnected nodes forming a pyramid/network)
- Red CTA pulse: "Contact Sales"
- Background: dark with subtle grid lines and data flow particles

SCENE 2 (8-15s): AI Task Prioritization
- Kanban board auto-populates: tasks fly into columns
- AI reorders tasks with glowing priority indicators
- "AI detected: Task B blocks 4 dependencies — prioritizing"
- Effort estimates appear next to tasks
- "23 tasks auto-scheduled in 0.8 seconds"
- Team member avatars assigned automatically

SCENE 3 (15-22s): Predictive Deadlines
- Gantt chart draws across timeline
- Deadline predictions appear with confidence percentages
- Risk indicator: one task flags yellow — "78% probability of delay"
- "AI suggests: Add 1 developer to reduce risk to 12%"
- Historical accuracy: "94% prediction accuracy across 1,200+ projects"
- Auto-reschedule animation when resource added

SCENE 4 (22-30s): Resource Optimization
- Team member cards with workload bars
- Overloaded members glow red, underutilized glow blue
- AI suggestion: reassignment arrows animate between members
- "Balanced workload in 3 moves" — three transfers animate
- Productivity projection: line chart shows optimization impact
- Cost savings counter: "AED 147K saved in resource optimization"

SCENE 5 (30-38s): Smart Reporting
- Report dashboard assembles from widgets
- Real-time project health: all green except one amber
- Burndown chart draws: actual vs planned lines
- "AI executive summary" text generates word by word
- Stakeholder view: simplified dashboard with top-level metrics
- Export options: PDF, PowerPoint, Notion — icons animate

SCENE 6 (38-45s): Risk Detection
- Risk radar: 360-degree view with risk spikes
- "AI detected: Scope creep on Feature X — 34% over original estimate"
- Mitigation cards slide in with recommended actions
- Risk history timeline: risks appearing and being resolved
- "87% of risks flagged before they become issues"
- Early warning system: notification bell rings with alert

SCENE 7 (45-52s): Automated Workflows
- Workflow builder: blocks connect with animated lines
- Approval chain: "Submitted → Reviewed → Approved" with checkmarks
- Trigger example: "When PR merged → Auto-update task → Notify QA"
- Workflow runs in real-time: blocks light up green as they execute
- "1,200+ automated workflows running"
- Time saved counter: "2,847 hours saved this quarter"

SCENE 8 (52-60s): Team Collaboration
- Real-time activity feed scrolls
- Comment thread: messages appear with typing indicators
- Document collaboration: two cursors moving on shared doc
- Meeting summary: AI generates action items from virtual meeting
- "Reduced meetings by 40% with async AI updates"
- Team happiness: NPS score animates up

SCENE 9 (60-68s): Integration Ecosystem
- Integration icons circle around FlowForge logo
- Connections light up: GitHub, Jira, Slack, Figma, Notion, Microsoft Teams
- Data sync animation: content flows between platforms
- "150+ integrations, 1-click setup"
- API webhook demo: endpoint fires, JSON response appears
- "Connected in under 3 minutes" badge

SCENE 10 (68-75s): CTA Finale
- Summary metrics grid: all key numbers animated
- FlowForge logo with 3D rotation
- Main CTA: "Let AI Run Your Projects — Contact Sales"
- Secondary: "See It In Action — Request Demo"
- RWT branding footer

TECHNICAL: Same as others — Three.js CDN, Inter font, inline CSS/JS, 1920x1080, dark theme, scene timer, particles, crossfade transitions, hidden replay button.
```

---

## Prompt 4: ServClaw — Harness Agent Deployment & Management

**Tagline:** "Deploy AI Agents Into Your Business. Instantly."

### Claude Prompt:

```
Create a single self-contained HTML file for ServClaw — an AI agent deployment and management platform by RedWhiteTech, powered by Harness. Screen-recordable demo page.

Same specs: self-contained HTML, Three.js CDN, Inter font, 1920x1080, dark theme, 75-85 seconds.

SCENE SEQUENCE:

SCENE 1 (0-8s): Hero
- "ServClaw" title with claw-like animation (letters snap together)
- "Deploy AI Agents Into Your Business. Instantly." — text reveals from center
- 3D robotic claw/arm rotating (Three.js geometric shapes)
- Red CTA: "Contact Sales"
- Background: dark blue/black with circuit-like particle lines

SCENE 2 (8-15s): One-Click Agent Deployment
- Terminal-style interface appears
- Command types itself: "$ servclaw deploy agent=customer-support"
- Progress bar fills rapidly: "Deploying → Configuring → Live"
- "Agent deployed in 4.7 seconds" badge
- Agent status card appears: green "ACTIVE" indicator
- Deployment log scrolls with green checkmarks

SCENE 3 (15-22s): Agent Fleet Management Dashboard
- Dashboard with agent cards in a grid
- Each card: agent name, status (green/yellow/red), tasks completed, uptime
- Auto-scaling animation: agents multiply as demand spikes
- "12 agents active | 3 idle | 0 errors"
- Resource usage bars: CPU, memory per agent
- Quick actions: Start, Stop, Restart buttons with hover effects

SCENE 4 (22-30s): CI/CD Pipeline Integration
- Pipeline visualization: code → build → test → deploy → monitor
- Harness logo integration: CD pipeline triggers
- Agent deployed automatically after successful build
- Canary deployment: 10% → 50% → 100% with traffic shifting animation
- Rollback simulation: one click reverts deployment
- "Integrated with your existing CI/CD in minutes"

SCENE 5 (30-38s): Automated Governance
- Policy cards appear in a grid: Security, Compliance, Access Control, Audit
- Agent action approval flow: "Agent requested: access customer DB"
- Approval chain: "Pending → Reviewed → Approved — action logged"
- Compliance score: "98/100" with green gauge
- Audit trail scrolls: timestamped agent actions
- "Every agent action is logged, reviewed, and auditable"

SCENE 6 (38-45s): Monitoring & Observability
- Real-time agent monitoring dashboard
- Request per second counter: live updating
- Response time graph: stays under 200ms
- Error rate: 0.03% shown with green indicator
- Agent conversation preview: messages stream in real-time
- Anomaly detection: spike alert flashes yellow briefly

SCENE 7 (45-52s): Agent Intelligence Dashboard
- Agent performance metrics: task completion rate, accuracy, learning rate
- Training data pipeline visualization
- "AI accuracy: 96.7% and improving" with upward trend
- Feedback loop: human feedback flows back to agent
- Agent specialization: different agents for support, sales, operations
- "Each agent learns from every interaction"

SCENE 8 (52-60s): Security & Compliance Guardrails
- Security layers animate around an agent
- Encryption badge: "AES-256, TLS 1.3"
- Data residency: "UAE sovereign cloud, on-prem option"
- Access control matrix: role-based permissions grid
- Penetration test: simulation runs, all checks pass green
- "ISO 27001, SOC 2, UAE PDPL compliant"

SCENE 9 (60-68s): Enterprise Scale
- Global deployment map with agent nodes worldwide
- "50,000+ agents deployed across 30 countries"
- "99.99% agent uptime" metric
- Enterprise logos rotate: "Trusted by banks, telcos, governments"
- Scaling animation: 1 agent → 100 agents → 10,000 agents
- "From pilot to enterprise — managed deployment"

SCENE 10 (68-75s): CTA Finale
- Summary: all metrics in a grid
- ServClaw logo with 3D claw rotation
- Main CTA: "Deploy AI Agents Today — Contact Sales"
- Secondary: "Schedule a Demo"
- RWT branding footer
- "Powered by Harness" badge

TECHNICAL: Same as all others.
```

---

## Prompt 5: CogniVerse — AI-Powered Learning Experience Platform

**Tagline:** "Where Learning Meets Intelligence"

### Claude Prompt:

```
Create a single self-contained HTML file for CogniVerse — an AI-powered learning experience platform (LXP) by RedWhiteTech. Screen-recordable demo page.

Same specs: self-contained HTML, Three.js CDN, Inter font, 1920x1080, dark theme, 75-85 seconds.

SCENE SEQUENCE:

SCENE 1 (0-8s): Hero
- "CogniVerse" title with expanding universe-like animation (letters spread and snap)
- "Where Learning Meets Intelligence" fades in with glow
- 3D rotating brain/network (Three.js: interconnected glowing nodes)
- Red CTA: "Contact Sales"
- Background: deep space-like with floating knowledge particles

SCENE 2 (8-15s): AI-Personalized Learning Paths
- Learner profile card on left
- AI generates learning path on right: modules connect with animated paths
- "Based on your role (Software Engineer) and goals (Lead Developer)"
- Skill assessment spider chart draws with current vs target levels
- "Recommended path: 8 modules, estimated 6 weeks"
- Each module previews content: video, quiz, project, peer review

SCENE 3 (15-22s): Adaptive Assessments
- Quiz interface: question appears, answer options slide in
- Difficulty adapts: student answers correctly → next question harder
- Real-time knowledge map updates: nodes turn from gray to green
- "Mastery level: 78% → 92%" after assessment
- Wrong answer triggers: AI explanation slides in
- "Adaptive testing: 200% more effective than fixed tests"

SCENE 4 (22-30s): Intelligent Content Generation
- AI content studio: prompt box types "Create a lesson on Docker containerization for beginners"
- Content generates in real-time: text, diagrams, code examples appear
- "Generated in 12 seconds" badge
- Content formats: text, video script, quiz questions, flashcards — tabs switch
- Quality score: "4.8/5 — reviewed by senior instructor"
- Languages: content translates to Arabic with one click

SCENE 5 (30-38s): Student Analytics Dashboard
- Instructor view: class performance overview
- Individual student cards with progress bars
- At-risk detection: "3 students behind schedule — AI suggests intervention"
- Engagement metrics: time spent, completion rates, quiz scores
- Learning velocity: how fast students progress through material
- "AI identifies struggling students 3 weeks before exams"

SCENE 6 (38-45s): Virtual AI Tutor
- Chat interface on right
- Student asks: "Can you explain polymorphism in Java with an example?"
- AI tutor responds with explanation, code example, and follow-up question
- Code playground: code executes and shows output
- "24/7 AI tutoring in Arabic and English"
- Tutor analytics: "Common question: OOP concepts — 143 students asked this week"

SCENE 7 (45-52s): Gamification Engine
- Achievement system: badges unlock with animations
- Leaderboard: top learners with points and streaks
- "7-day learning streak!" fire animation
- Skill tree: RPG-style progression with unlockable nodes
- Course completion celebration: confetti animation
- "Gamification increases course completion by 47%"

SCENE 8 (52-60s): Collaborative Learning
- Virtual classroom: participant avatars in a circle
- Live whiteboard: students and instructor draw together
- Breakout rooms: small groups form with animation
- Peer review: student submits work → peer feedback appears
- Discussion forum: threads populate with AI-suggested responses
- "Community-driven learning boosts retention by 65%"

SCENE 9 (60-68s): Enterprise Training Scale
- Corporate dashboard: departments, compliance training tracking
- "15,000+ employees trained across 12 departments"
- Compliance completion: "100% GDPR, 98% Safety" with progress bars
- ROI calculator: "AED 2.3M saved vs traditional training"
- Custom branding: client logo appears on platform
- Integration: LMS, HRIS, SSO logos animate

SCENE 10 (68-75s): CTA Finale
- All features summarized in grid
- CogniVerse logo with 3D neural network rotation
- Main CTA: "Transform Learning With AI — Contact Sales"
- Secondary: "Request a Demo for Your Organization"
- RWT branding footer

TECHNICAL: Same as all others.
```

---

## File Structure Expected in Repo

```
rwt-product-showcase/
├── nexarena.html         # NexArena product demo
├── peoplepulse.html      # PeoplePulse product demo
├── flowforge.html        # FlowForge product demo
├── servclaw.html         # ServClaw product demo
├── cogniverse.html       # CogniVerse product demo
├── shared/
│   ├── rwt-brand.css     # Shared RWT brand styles
│   └── scene-manager.js  # Shared scene timer/transition logic
├── prompts-part1-video-html.md   # This file
├── prompts-part2-screenshots.md  # Screenshot capture prompts
└── README.md
```

## Post-Generation Pipeline

1. Claude generates each HTML file
2. Open each in browser at 1920x1080
3. Run auto-play sequence
4. **Screen recording:** Use `navigator.mediaDevices.getDisplayMedia()` or Puppeteer `page.screencast()` to capture MP4
5. **Screenshots:** Capture specific frames at key scenes (see Part 2)
6. Result: 5 product demo videos + 30-40 screenshots for website

# RWT Product Showcase — Video Descriptions

Three product demo videos built and rendered by **Red White Tech**, each showcasing a distinct enterprise platform. All videos are screen-recorded from self-contained animated HTML demos at 1920x1080, 30fps, H.264.

---

## 1. ORBIS — Digital Commerce Platform

**File:** `render/nexarena.mp4`
**Thumbnail:** `thumbnail-nexarena.jpg`
**Duration:** 64.5 seconds
**Resolution:** 1920x1080

### Overview

ORBIS is a full-stack digital commerce platform built for the gaming, collectibles, and entertainment market. It enables merchants to sell digital games, books, comics, and trading cards through a single unified storefront with instant digital delivery and AI-powered recommendations.

### What the Video Shows

The demo walks through the complete customer journey and platform capability across 10 scenes:

**Scene 1 — Platform Introduction**
The ORBIS brand identity is introduced with an indigo and cyan color palette. The hero scene establishes the platform as a specialist digital commerce solution for games, books, comics, and trading cards, contrasting it against generic e-commerce platforms.

**Scene 2 — Storefront & Product Detail**
The live storefront is shown with a product detail page for a featured game title. The UI demonstrates a genre-tagged product listing with a price, ratings, and instant delivery options. The Add to Cart flow is shown along with trust signals (Instant Delivery, Verified Key badges).

**Scene 3 — Animated Product Grid**
A 12-card product grid demonstrates the category-browsing experience across games, comics, and cards. Cards include cover art, price tags, and delivery type indicators. Hover states and grid responsiveness are implied through the animated reveal sequence.

**Scene 4 — Shopping Cart & Checkout**
The multi-item cart is shown with price breakdown, discount code field, and a secure checkout flow. The platform's instant fulfillment model is demonstrated: after payment, digital delivery keys and download links appear in the customer's library without any shipping wait.

**Scene 5 — Digital Library & Delivery**
The customer's personal library view displays owned titles across categories. The instant delivery confirmation screen shows the fulfillment pipeline: purchase confirmed, license key generated, item added to library — all within seconds of transaction.

**Scene 6 — Merchant Analytics Dashboard**
A revenue analytics view shows transaction volume across categories, top-selling products, and conversion funnel metrics. The dashboard is the platform operator's control center for understanding catalogue performance.

**Scene 7 — AI Recommendation Engine**
The platform's AI recommendation module surfaces contextual upsell suggestions based on purchase history and browsing behavior. The "Customers Also Bought" and "New in Your Genres" components are demonstrated updating in real time.

**Scene 8 — Admin Control Panel**
The back-office panel shows inventory management, product publishing, and pricing controls. A product upload flow demonstrates how merchants onboard new digital titles with metadata tagging, pricing tiers, and release scheduling.

**Scene 9 — Platform Capability Marketing**
A mid-video marketing slide explains what ORBIS does as a platform: multi-category digital commerce, instant key delivery, AI curation, and real-time analytics. This segment is positioned as a capability statement aimed at prospective platform operators.

**Scene 10 — Red White Tech Attribution**
The final scene transitions to a clean dark outro crediting Red White Tech as the builder of the ORBIS platform. The RWT logo and brand identity close the video with a "We built this" statement, inviting viewers to inquire about similar builds.

### Design Notes
- **Color palette:** Indigo `#6366F1` primary, Cyan `#22D3EE` accent, deep navy background `#0B1120`
- **Transition style:** IRIS opacity fade — scenes dissolve through a shared timeline
- **Icons:** Font Awesome 6 throughout (no emojis)
- **Typography:** Display-weight headings with tightly tracked uppercase labels
- No fake platform statistics or fabricated user counts are shown anywhere in the video

---

## 2. Rotation14 — Enterprise AI HR Platform

**File:** `render/rotation14.mp4`
**Thumbnail:** `thumbnail-rotation14.jpg`
**Duration:** 76 seconds
**Resolution:** 1920x1080

### Overview

Rotation14 is an enterprise AI platform for human resources, built around the Microsoft 365 design language in dark mode. It handles the full employee lifecycle — from AI-powered resume screening and bias-free hiring through onboarding, sentiment monitoring, performance management, compliance automation, and a unified mobile employee portal.

### What the Video Shows

**Scene 1 — System Initialization**
A Three.js wireframe network renders in real time, representing the AI backbone connecting all HR modules. The Rotation14 brand and tagline are introduced against the deep navy background. The camera zooms into the central network node with the header "SYSTEM INITIALIZATION."

**Scene 2 — Deep Parse Screening Engine**
The AI resume parsing module is shown processing incoming job applications. A candidate matrix lists parsed applicants with competency tags, skills matched, seniority level, bias status, and hiring decision. The camera zooms into the candidate grid with the header "AUTOMATED BIAS FILTERING," highlighting that the platform removes demographic signals before scoring.

**Scene 3 — Organisational Risk Intelligence**
An organisation chart maps team structure and reports an attrition risk score for each team node. A highlighted risk card at the bottom flags a specific team with an elevated flight-risk indicator and root-cause reasoning. The zoom targets this card with "PREDICTIVE ATTRITION ALERT."

**Scene 4 — Automated Onboarding Tracks**
A day-by-day onboarding task grid is shown for new hires, broken into 30/60/90-day milestones. Each track shows assigned tasks, stakeholder contacts, completion status, and learning path modules. The camera zooms into a specific task block with "AI-CURATED LEARNING PATHS."

**Scene 5 — Real-Time Sentiment Analysis**
An employee sentiment dashboard shows mood trend lines broken down by team and time period. A resolution panel at the bottom surface lists open HR cases alongside AI-drafted response suggestions. The feature header reads "REAL-TIME SENTIMENT ANALYSIS."

**Scene 6 — Predictive Resource Planning**
Scenario-based headcount forecasting is shown with a demand forecast chart and a quarterly simulation results table. The table flags a Q4 high-risk headcount gap and recommends a specific hiring action with budget impact and break-even timeline. Camera header: "SCENARIO SIMULATION ALGORITHM."

**Scene 7 — Performance Review & Compensation**
A performance review dashboard displays individual contributor scores across KPI dimensions, peer feedback summaries, and a compensation recommendation panel. The zoom targets the promotion recommendation section with "UNBIASED PERFORMANCE METRICS."

**Scene 8 — Automated Compliance Oversight**
A compliance tracking table lists statutory obligations with status indicators — completed, pending, or flagged. A red-highlighted row calls out an expiring contract requiring legal review. The zoom targets this row with "AUTOMATED COMPLIANCE OVERSIGHT," emphasising the platform's role in reducing legal risk.

**Scene 9 — Unified Employee Mobile Portal**
A mobile-first employee portal view is shown inside a device frame, displaying an employee's personal dashboard: upcoming tasks, payslip access, leave balance, and a chat interface for HR queries. Camera header: "UNIFIED EMPLOYEE PORTAL."

**Scene 10 — Red White Tech Attribution**
The video closes with a slow camera push into the Red White Tech logo and brand attribution. The screen fades to black with the header "PROUDLY DEVELOPED BY RED WHITE TECH."

### Design Notes
- **Color palette:** Background `#111724`, borders `#29354A`, cobalt blue `#0078D4`, success green `#107C41`
- **Strict no-border-radius:** All UI elements use hard 90-degree corners enforced globally
- **Transition style:** Horizontal slide (CSS `translateX`) — scenes push in from the right
- **Camera system:** Per-scene zoom into specific data zones, with blur overlay and feature header drop from top
- **3D element:** Three.js icosahedron wireframe network in Scene 1 (WebGL, renders in headless Chromium)

---

## 3. ServClaw — Enterprise AI Agent Platform

**File:** `render/servclaw.mp4`
**Thumbnail:** `thumbnail-servclaw.jpg`
**Duration:** 72 seconds
**Resolution:** 1920x1080

### Overview

ServClaw is an enterprise AI agent deployment and management platform built by Red White Tech and powered by Harness CI/CD infrastructure. It enables organisations to deploy, govern, and monitor large fleets of specialised AI agents — from a single command to 50,000 agents across 30 global regions. The platform is built around a premium enterprise light mode aesthetic.

### What the Video Shows

**Scene 1 — System Initialization**
The ServClaw hero introduces the platform with a split layout: branding on the left with key value propositions (sub-5s deployment, 99.99% uptime, ISO 27001 certified), and a Three.js wireframe robotic claw on the right. The claw rotates slowly on its Y-axis, representing the orchestration engine. The camera zooms into the claw's central joint with the header "ENTERPRISE AGENT ORCHESTRATION."

**Scene 2 — Instant Agent Provisioning**
A dark-themed terminal window shows the `servclaw deploy` command being entered with agent name and environment flags. Four sequential deployment steps are confirmed with green checkmarks: provisioning compute, injecting agent logic, connecting enterprise data streams, and health check passing. An agent status card on the right confirms the agent is live, showing the agent ID, region, data stream connections, and memory usage. A large "4.7s" badge highlights the deployment time. Camera header: "SUB-5-SECOND DEPLOYMENT."

**Scene 3 — Agent Fleet Dashboard**
A full-width grid of 8 agent cards displays the live fleet. Each card shows the agent ID, role, operations executed today, uptime percentage, and CPU/RAM usage bars. Active agents have a green top border; standby agents show amber. Fleet-wide statistics at the top show 12 active, 3 standby, 0 errors, 15 total. The camera zooms into a resource-heavy card with "DYNAMIC FLEET SCALING."

**Scene 4 — CI/CD Pipeline Integration**
A five-node horizontal pipeline is shown: Commit, Build, Test, Deploy, Monitor. Each node illuminates in sequence. The Deploy node is rendered in Harness Blue with a "HARNESS" badge, showing the integration point. Below the pipeline, a canary routing bar shows traffic split — 90% to v1.0 and 10% to v2.0 — with real-time error rate and latency delta readings. Camera header: "HARNESS-POWERED CANARY RELEASES."

**Scene 5 — Automated Governance**
Four policy cards display scores for Security Policy (98/100), Compliance (100/100), Access Control (97/100), and Audit Trail (100/100). On the right, a live access request from Agent #409 is processed in real time: the policy engine reviews and approves the request in three automated steps, logging a cryptographic hash to the immutable audit trail. Below, the four most recent audit entries are shown with timestamps and hash previews. Camera header: "IMMUTABLE AUDIT TRAIL."

**Scene 6 — Real-Time Observability**
Five stat cards at the top show live telemetry: 2,847 requests per second, 148ms average response time, 0.03% error rate, 15 active agents, and 1 anomaly detected. A 30-bar request throughput chart shows load patterns. An anomaly detection feed on the right shows the spike event, the automatic failover action (completed in 1.8s with zero downtime), root cause identification, and system restoration — all within a 17-second window. Camera header: "PREDICTIVE ANOMALY DETECTION."

**Scene 7 — Agent Intelligence**
An accuracy trend chart shows resolution accuracy climbing from 60% to 98.5% over time, represented as green bars. A feedback loop diagram explains how human reviewer validation feeds back into the agent model. A specialisation registry lists five agent types with their individual accuracy scores: Customer Support (98.5%), Sales Intelligence (96.2%), Operations Monitor (99.1%), Contract Analysis (97.8%), Fraud Detection (99.7%). Camera header: "CONTINUOUS LEARNING LOOP."

**Scene 8 — Enterprise Security Architecture**
Three concentric security rings surround a central robot icon, labelled with AES-256, TLS 1.3, RBAC, and WAF. Eight compliance badges form a grid: ISO 27001, SOC 2 Type II, UAE PDPL, AES-256, On-Premise, UAE Sovereign, Zero Trust, and Key Rotation. A penetration test result banner confirms 27 vectors tested with zero critical findings. Camera header: "SOVEREIGN DATA COMPLIANCE."

**Scene 9 — Global Infrastructure Scale**
A dot-grid world map overlaid with SVG shows active deployment nodes across New York, London, Paris, Dubai, Mumbai, Singapore, Tokyo, Seoul, São Paulo, Lagos, and Sydney. Connection lines link all nodes. Dubai and Singapore pulse as primary regional hubs. Overlay metrics show 50,000+ agents deployed, 30 regions active, and 99.99% uptime SLA maintained. Camera header: "GLOBAL EDGE DEPLOYMENT."

**Scene 10 — Attribution**
The closing scene uses a centered light-mode layout with the large "ServClaw" logotype (with Harness Blue accent on "Claw"), the subtitle "Enterprise Agent Orchestration," and a lockup combining the Red White Tech logo alongside a "POWERED BY HARNESS" badge. A contact prompt fades in: "Initiate Deployment — Contact Enterprise Sales." Camera header: "PROUDLY DEVELOPED BY RED WHITE TECH."

### Design Notes
- **Color palette:** Background `#FFFFFF`, panels `#F8F9FA`, borders `#E2E8F0`, text `#0F172A`, Harness Blue `#2563EB`, Success Green `#16A34A`, Alert Amber `#D97706`
- **Border radius:** Maximum 2px (micro-bevel) — SaaS enterprise aesthetic
- **Transition style:** Horizontal slide (CSS `translateX`) — same engine as Rotation14
- **Camera system:** Per-scene zoom with interpolated transform, dark `#0F172A` feature header drops from top
- **3D element:** Three.js geometric robotic claw arm (wireframe) in Scene 1
- **Powered by Harness:** Harness CI/CD integration is a named feature throughout

---

## Technical Specifications

| Property | Value |
|---|---|
| Resolution | 1920 x 1080 px |
| Frame rate | 30 fps |
| Codec | H.264 (libx264) |
| Quality | CRF 16, `slow` preset |
| Pixel format | yuv420p |
| Audio | None (silent demo) |
| Render method | Playwright headless Chromium — frame-by-frame CSS animation seek |
| Scene transitions | ORBIS: opacity fade / Rotation14 + ServClaw: horizontal slide |

## Render Commands

```bash
npm run render:nexarena      # ORBIS → render/nexarena.mp4
npm run render:rotation14    # Rotation14 → render/rotation14.mp4
npm run render:rotation14    # ServClaw → render/servclaw.mp4

# Or all at once:
npm run render:all

# 4K variants:
npm run render:nexarena:4k
npm run render:rotation14:4k
```

---

*Built by Red White Tech — [redwhitetech.ae](https://redwhitetech.ae)*

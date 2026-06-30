#!/usr/bin/env python3
import base64, pathlib

LOGO_PATH = pathlib.Path('Red White Tech png-01.png')
with open(LOGO_PATH, 'rb') as f:
    LOGO_B64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode()

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ServClaw — Enterprise AI Agent Platform</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;}
:root{
  --bg:#FFFFFF;--panel:#F8F9FA;--panel2:#EEF2FF;--bdr:#E2E8F0;
  --text:#0F172A;--text2:#334155;--muted:#64748B;
  --blue:#2563EB;--blue-lt:#DBEAFE;--blue-dk:#1D4ED8;
  --green:#16A34A;--green-lt:#DCFCE7;
  --amber:#D97706;--amber-lt:#FEF3C7;
  --red:#DC2626;--red-lt:#FEE2E2;
  --sh:0 1px 3px rgba(15,23,42,.08),0 1px 2px rgba(15,23,42,.04);
  --sh2:0 4px 12px rgba(15,23,42,.10),0 2px 4px rgba(15,23,42,.06);
}
body{width:1920px;height:1080px;overflow:hidden;background:var(--bg);
  font-family:'Inter',system-ui,sans-serif;color:var(--text);font-size:14px;line-height:1.5;
  -webkit-font-smoothing:antialiased;}
#stage{position:relative;width:1920px;height:1080px;overflow:hidden;}
#camera-group{position:absolute;inset:0;transform-origin:0 0;will-change:transform;
  transition:transform 800ms cubic-bezier(0.25,0.46,0.45,0.94);}
.scene{position:absolute;inset:0;background:var(--bg);transform:translateX(100%);overflow:hidden;}
.scene.is-active{transform:translateX(0);}
.scene.entering{animation:slideIn 0.6s cubic-bezier(0.25,0.46,0.45,0.94) forwards;z-index:3;}
.scene.exiting{animation:slideOut 0.6s cubic-bezier(0.25,0.46,0.45,0.94) forwards;z-index:2;}
@keyframes slideIn{from{transform:translateX(100%)}to{transform:translateX(0)}}
@keyframes slideOut{from{transform:translateX(0)}to{transform:translateX(-100%)}}

html.capture-mode .scene{animation:none!important;}
html.capture-mode .scene:not(.is-active){transform:translateX(100%)!important;}
html.capture-mode .scene.is-active{transform:translateX(0)!important;}
html.capture-mode #camera-group{transition:none!important;}
html.capture-mode #blur-overlay{display:none!important;}
html.capture-mode #feature-hdr{transition:none!important;}

#blur-overlay{position:absolute;inset:0;z-index:50;background:rgba(255,255,255,.35);
  backdrop-filter:blur(8px);opacity:0;pointer-events:none;transition:opacity 500ms;}
#blur-overlay.visible{opacity:1;}

#feature-hdr{position:absolute;top:0;left:0;right:0;height:64px;z-index:100;
  background:#0F172A;display:flex;align-items:center;justify-content:center;gap:16px;
  transform:translateY(-100%);transition:transform 380ms cubic-bezier(0.22,1,0.36,1);
  border-bottom:2px solid var(--blue);}
#feature-hdr.visible{transform:translateY(0);}
.fh-icon{color:var(--blue);font-size:20px;}
.fh-text{color:#FFF;font-size:14px;font-weight:800;letter-spacing:.26em;text-transform:uppercase;}

#tl{position:absolute;bottom:22px;left:50%;transform:translateX(-50%);
  display:flex;gap:10px;z-index:200;align-items:center;}
.tl-dot{width:8px;height:8px;background:rgba(15,23,42,.15);border-radius:4px;cursor:pointer;transition:all 200ms;}
.tl-dot.active{background:var(--blue);width:28px;}
.tl-dot.done{background:rgba(37,99,235,.35);}

/* ---- Utilities ---- */
.panel{background:var(--panel);border:1px solid var(--bdr);box-shadow:var(--sh);border-radius:2px;}
.panel-hdr{padding:11px 16px;border-bottom:1px solid var(--bdr);font-size:11px;font-weight:700;
  letter-spacing:.12em;text-transform:uppercase;color:var(--muted);display:flex;align-items:center;gap:8px;}
.badge{display:inline-flex;align-items:center;gap:5px;padding:3px 9px;font-size:11px;font-weight:700;
  border-radius:2px;letter-spacing:.06em;text-transform:uppercase;}
.b-blue{background:var(--blue-lt);color:var(--blue);}
.b-green{background:var(--green-lt);color:var(--green);}
.b-amber{background:var(--amber-lt);color:var(--amber);}
.b-red{background:var(--red-lt);color:var(--red);}
.b-dark{background:var(--text);color:#FFF;}
.b-harness{background:var(--blue);color:#FFF;}
.dot-live{width:7px;height:7px;border-radius:50%;background:var(--green);
  box-shadow:0 0 0 0 rgba(22,163,74,.4);animation:pulse 2s infinite;}
.dot-amber{width:7px;height:7px;border-radius:50%;background:var(--amber);}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(22,163,74,.4)}
  70%{box-shadow:0 0 0 8px rgba(22,163,74,0)}100%{box-shadow:0 0 0 0 rgba(22,163,74,0)}}
.bar-track{background:var(--bdr);height:6px;border-radius:1px;overflow:hidden;width:100%;}
.bar-fill{height:100%;border-radius:1px;transition:width 1.4s cubic-bezier(.4,0,.2,1);}
.bf-blue{background:var(--blue);}
.bf-green{background:var(--green);}
.bf-amber{background:var(--amber);}
.bf-red{background:var(--red);}
.mono{font-family:'Fira Code','Courier New',monospace;}

/* ---- Entry animations ---- */
.scene.is-active .au{animation:fadeUp .6s ease both;}
.scene.is-active .aur{animation:fadeUp .8s ease both;}
.scene.is-active .asr{animation:slideR .6s ease both;}
.scene.is-active .apt{animation:popIn .5s cubic-bezier(.34,1.56,.64,1) both;}
@keyframes fadeUp{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
@keyframes slideR{from{opacity:0;transform:translateX(-16px)}to{opacity:1;transform:translateX(0)}}
@keyframes popIn{from{opacity:0;transform:scale(.85)}to{opacity:1;transform:scale(1)}}
.d1{animation-delay:.1s}.d2{animation-delay:.25s}.d3{animation-delay:.4s}.d4{animation-delay:.55s}
.d5{animation-delay:.7s}.d6{animation-delay:.85s}.d7{animation-delay:1.0s}.d8{animation-delay:1.15s}

/* ---- S0 Hero ---- */
.s0{display:flex;align-items:center;justify-content:center;
  background:linear-gradient(135deg,#F0F6FF 0%,#FFFFFF 50%,#F5F3FF 100%);}
.s0-inner{display:flex;align-items:center;gap:0;width:1920px;height:1080px;}
.s0-left{flex:0 0 840px;padding:0 80px 0 100px;display:flex;flex-direction:column;justify-content:center;}
.s0-right{flex:1;height:1080px;position:relative;display:flex;align-items:center;justify-content:center;
  background:linear-gradient(135deg,#EEF2FF 0%,#F0F9FF 100%);border-left:1px solid var(--bdr);}
.s0-eyebrow{font-size:12px;font-weight:700;color:var(--blue);letter-spacing:.2em;text-transform:uppercase;margin-bottom:20px;}
.s0-title{font-size:88px;font-weight:900;color:var(--text);line-height:1;margin-bottom:16px;letter-spacing:-3px;}
.s0-title span{color:var(--blue);}
.s0-sub{font-size:24px;font-weight:400;color:var(--text2);margin-bottom:36px;line-height:1.4;}
.s0-pills{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:48px;}
.s0-pill{padding:6px 14px;font-size:12px;font-weight:600;border-radius:2px;
  border:1px solid var(--bdr);color:var(--text2);background:var(--bg);}
.s0-pill.blue{background:var(--blue-lt);color:var(--blue);border-color:var(--blue-lt);}
.s0-harness{display:flex;align-items:center;gap:10px;color:var(--muted);font-size:13px;font-weight:500;}
.s0-harness i{color:var(--blue);}
#s0-canvas{width:700px;height:700px;}
.s0-claw-label{position:absolute;bottom:60px;left:50%;transform:translateX(-50%);
  font-size:11px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);}

/* ---- S1 Provisioning ---- */
.s1{display:flex;}
.s1-left{flex:1;background:#0F172A;padding:60px 56px;display:flex;flex-direction:column;justify-content:center;}
.s1-right{flex:0 0 560px;background:var(--panel);padding:60px 48px;display:flex;flex-direction:column;justify-content:center;border-left:1px solid var(--bdr);}
.term-bar{display:flex;align-items:center;gap:7px;margin-bottom:28px;}
.td{width:12px;height:12px;border-radius:50%;}
.td-r{background:#EF4444;}.td-y{background:#F59E0B;}.td-g{background:#22C55E;}
.term-title{color:#475569;font-size:12px;font-weight:500;margin-left:10px;font-family:'Fira Code',monospace;}
.t-prompt{color:#22C55E;}.t-cmd{color:#E2E8F0;font-size:15px;line-height:1.6;}
.t-flag{color:#93C5FD;}.t-val{color:#FCD34D;}
.t-line{color:#94A3B8;font-size:13px;margin-top:8px;}
.t-step{display:flex;align-items:center;gap:12px;margin:16px 0;font-size:14px;}
.t-ok{color:#22C55E;width:18px;}.t-spin{color:#60A5FA;width:18px;animation:spin 1s linear infinite;}
@keyframes spin{to{transform:rotate(360deg)}}
.t-step-txt{color:#CBD5E1;}.t-step-sub{color:#475569;font-size:12px;font-family:'Fira Code',monospace;}
.t-success-box{margin-top:28px;background:#052E16;border:1px solid #166534;padding:16px 20px;}
.t-success-lbl{color:#22C55E;font-size:13px;font-weight:700;letter-spacing:.08em;}
.t-success-val{color:#4ADE80;font-size:20px;font-weight:800;margin-top:4px;font-family:'Fira Code',monospace;}
.ac-title{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:20px;}
.ac-main{background:var(--bg);border:1px solid var(--bdr);border-radius:2px;padding:24px;margin-bottom:16px;box-shadow:var(--sh2);}
.ac-name{font-size:22px;font-weight:800;color:var(--text);margin:10px 0 4px;}
.ac-ver{font-size:12px;color:var(--muted);margin-bottom:18px;font-family:'Fira Code',monospace;}
.ac-row{display:flex;justify-content:space-between;align-items:center;padding:9px 0;border-bottom:1px solid var(--bdr);font-size:13px;}
.ac-row:last-child{border-bottom:none;}
.ac-lbl{color:var(--muted);}.ac-val{font-weight:600;}.ac-val.blue{color:var(--blue);}
.ac-time{background:var(--blue-lt);padding:18px;text-align:center;border-radius:2px;}
.ac-time-n{font-size:36px;font-weight:900;color:var(--blue);}
.ac-time-l{font-size:11px;color:var(--blue);letter-spacing:.12em;text-transform:uppercase;margin-top:2px;}

/* ---- S2 Fleet ---- */
.s2{display:flex;flex-direction:column;padding:50px 60px;}
.s2-hdr{display:flex;align-items:center;justify-content:space-between;margin-bottom:36px;}
.s2-title{font-size:28px;font-weight:800;color:var(--text);}
.s2-stats{display:flex;gap:20px;}
.stat-chip{background:var(--panel);border:1px solid var(--bdr);padding:12px 20px;text-align:center;border-radius:2px;}
.stat-n{font-size:28px;font-weight:900;color:var(--text);}
.stat-n.blue{color:var(--blue);}.stat-n.green{color:var(--green);}.stat-n.amber{color:var(--amber);}
.stat-l{font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-top:2px;}
.agent-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;flex:1;}
.agent-card{background:var(--bg);border:1px solid var(--bdr);border-radius:2px;padding:20px;box-shadow:var(--sh);
  display:flex;flex-direction:column;gap:12px;position:relative;overflow:hidden;}
.agent-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--green);}
.agent-card.standby::before{background:var(--amber);}
.ag-top{display:flex;align-items:center;justify-content:space-between;}
.ag-id{font-size:13px;font-weight:700;color:var(--text);font-family:'Fira Code',monospace;}
.ag-row{display:flex;justify-content:space-between;align-items:center;font-size:12px;}
.ag-lbl{color:var(--muted);}.ag-val{font-weight:600;color:var(--text);}
.ag-bars{display:flex;flex-direction:column;gap:6px;}
.ag-bar-row{display:flex;align-items:center;gap:8px;font-size:11px;}
.ag-bar-lbl{color:var(--muted);width:32px;}.ag-bar-val{color:var(--muted);width:28px;text-align:right;}
.ag-bar-track{flex:1;height:4px;background:var(--bdr);border-radius:1px;overflow:hidden;}
.ag-bar-fill{height:100%;border-radius:1px;background:var(--blue);}
.ag-bar-fill.amber{background:var(--amber);}

/* ---- S3 CI/CD ---- */
.s3{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:60px;}
.s3-title{font-size:13px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:60px;}
.pipeline{display:flex;align-items:center;gap:0;margin-bottom:60px;}
.pipe-node{display:flex;flex-direction:column;align-items:center;gap:12px;position:relative;}
.pipe-circle{width:88px;height:88px;border-radius:50%;border:2px solid var(--bdr);background:var(--bg);
  display:flex;align-items:center;justify-content:center;font-size:28px;box-shadow:var(--sh2);position:relative;}
.pipe-circle.done{border-color:var(--green);background:var(--green-lt);color:var(--green);}
.pipe-circle.active{border-color:var(--blue);background:var(--blue-lt);color:var(--blue);}
.pipe-circle.harness{border-color:var(--blue);background:var(--blue);color:#FFF;}
.pipe-lbl{font-size:13px;font-weight:700;color:var(--text);text-align:center;}
.pipe-sub{font-size:11px;color:var(--muted);text-align:center;}
.pipe-arrow{width:80px;display:flex;align-items:center;justify-content:center;color:var(--bdr);font-size:20px;padding-bottom:30px;}
.pipe-arrow.lit{color:var(--green);}
.harness-badge{position:absolute;top:-12px;right:-16px;padding:3px 8px;background:var(--blue);color:#FFF;
  font-size:10px;font-weight:700;letter-spacing:.08em;border-radius:2px;}
.canary-box{width:900px;background:var(--bg);border:1px solid var(--bdr);border-radius:2px;padding:28px 36px;box-shadow:var(--sh2);}
.canary-title{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-bottom:20px;}
.canary-track{display:flex;height:32px;border-radius:2px;overflow:hidden;border:1px solid var(--bdr);margin-bottom:12px;}
.canary-v1{flex:9;background:var(--blue);display:flex;align-items:center;justify-content:center;
  color:#FFF;font-size:13px;font-weight:700;}
.canary-v2{flex:1;background:var(--amber);display:flex;align-items:center;justify-content:center;
  color:#FFF;font-size:12px;font-weight:700;}
.canary-row{display:flex;justify-content:space-between;font-size:12px;}
.canary-lbl{color:var(--muted);}
.canary-val{font-weight:600;color:var(--text);}
.canary-val.green{color:var(--green);}

/* ---- S4 Governance ---- */
.s4{display:flex;}
.s4-left{flex:0 0 700px;padding:50px 48px;border-right:1px solid var(--bdr);display:flex;flex-direction:column;justify-content:center;}
.s4-right{flex:1;padding:50px 48px;display:flex;flex-direction:column;justify-content:center;}
.s4-title{font-size:13px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:28px;}
.policy-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
.policy-card{background:var(--bg);border:1px solid var(--bdr);border-radius:2px;padding:20px;box-shadow:var(--sh);}
.pc-icon{font-size:22px;margin-bottom:10px;}
.pc-icon.blue{color:var(--blue);}.pc-icon.green{color:var(--green);}.pc-icon.amber{color:var(--amber);}
.pc-name{font-size:14px;font-weight:700;color:var(--text);margin-bottom:4px;}
.pc-score{font-size:24px;font-weight:900;color:var(--green);}.pc-score.ok::after{content:' / 100';}
.pc-label{font-size:11px;color:var(--muted);}
.request-box{background:var(--amber-lt);border:1px solid #FDE68A;border-radius:2px;padding:18px 20px;margin-bottom:20px;}
.req-hdr{font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--amber);margin-bottom:8px;}
.req-text{font-size:13px;color:var(--text);line-height:1.5;}
.req-agent{font-family:'Fira Code',monospace;font-weight:700;color:var(--text);}
.flow-steps{display:flex;flex-direction:column;gap:10px;margin-bottom:24px;}
.flow-step{display:flex;align-items:center;gap:12px;padding:12px 16px;background:var(--bg);
  border:1px solid var(--bdr);border-radius:2px;}
.flow-step.approved{border-color:var(--green);background:var(--green-lt);}
.flow-icon{font-size:16px;width:20px;text-align:center;}
.flow-lbl{font-size:13px;font-weight:600;color:var(--text);}
.flow-sub{font-size:11px;color:var(--muted);}
.audit-title{font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:12px;}
.audit-entry{display:flex;align-items:flex-start;gap:10px;padding:9px 0;border-bottom:1px solid var(--bdr);font-size:12px;}
.audit-entry:last-child{border-bottom:none;}
.audit-time{color:var(--muted);width:90px;font-family:'Fira Code',monospace;flex-shrink:0;}
.audit-evt{color:var(--text);flex:1;}
.audit-hash{color:var(--muted);font-family:'Fira Code',monospace;font-size:10px;}

/* ---- S5 Observability ---- */
.s5{display:flex;flex-direction:column;padding:50px 60px;}
.s5-stats{display:flex;gap:20px;margin-bottom:36px;}
.obs-stat{flex:1;background:var(--bg);border:1px solid var(--bdr);padding:22px 24px;border-radius:2px;box-shadow:var(--sh);}
.obs-stat.alert{border-color:var(--amber);background:var(--amber-lt);}
.os-icon{font-size:20px;margin-bottom:8px;color:var(--blue);}
.os-icon.green{color:var(--green);}.os-icon.amber{color:var(--amber);}
.os-val{font-size:36px;font-weight:900;color:var(--text);line-height:1;}
.os-val.green{color:var(--green);}.os-val.amber{color:var(--amber);}
.os-unit{font-size:16px;font-weight:500;color:var(--muted);}
.os-lbl{font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-top:6px;}
.s5-main{flex:1;display:flex;gap:20px;}
.chart-panel{flex:1;background:var(--bg);border:1px solid var(--bdr);border-radius:2px;box-shadow:var(--sh);overflow:hidden;}
.chart-body{padding:20px;height:calc(100% - 48px);display:flex;align-items:flex-end;gap:5px;}
.chart-bar{flex:1;border-radius:1px 1px 0 0;min-height:4px;background:var(--blue);opacity:.8;transition:height .4s;}
.anomaly-panel{flex:0 0 480px;background:var(--bg);border:1px solid var(--bdr);border-radius:2px;
  box-shadow:var(--sh);display:flex;flex-direction:column;}
.anomaly-panel .panel-hdr{color:var(--amber);}
.anomaly-body{flex:1;padding:16px;overflow:hidden;display:flex;flex-direction:column;gap:10px;}
.anom-entry{padding:12px 14px;border-radius:2px;font-size:12px;line-height:1.5;}
.anom-entry.warn{background:var(--amber-lt);border-left:3px solid var(--amber);}
.anom-entry.ok{background:var(--green-lt);border-left:3px solid var(--green);}
.anom-entry.info{background:var(--blue-lt);border-left:3px solid var(--blue);}
.anom-time{font-size:11px;color:var(--muted);font-family:'Fira Code',monospace;}
.anom-evt{font-weight:600;color:var(--text);margin:2px 0;}
.anom-sub{color:var(--text2);}
.alert-banner{background:var(--amber);color:#FFF;padding:12px 16px;display:flex;align-items:center;gap:10px;
  font-size:13px;font-weight:700;}

/* ---- S6 Intelligence ---- */
.s6{display:flex;}
.s6-left{flex:1;padding:50px 52px;border-right:1px solid var(--bdr);}
.s6-right{flex:0 0 640px;padding:50px 48px;display:flex;flex-direction:column;gap:20px;}
.s6-title{font-size:13px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:28px;}
.trend-box{background:var(--bg);border:1px solid var(--bdr);border-radius:2px;padding:24px;box-shadow:var(--sh);margin-bottom:20px;}
.trend-val{font-size:52px;font-weight:900;color:var(--green);}
.trend-lbl{font-size:12px;color:var(--muted);margin-bottom:16px;margin-top:2px;}
.trend-chart{height:80px;display:flex;align-items:flex-end;gap:3px;}
.tb{flex:1;border-radius:1px 1px 0 0;background:var(--green-lt);border-bottom:2px solid var(--green);}
.feedback-box{background:var(--panel2);border:1px solid #C7D2FE;border-radius:2px;padding:20px;box-shadow:var(--sh);}
.feedback-title{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--blue);margin-bottom:14px;}
.feedback-row{display:flex;align-items:center;gap:10px;margin:8px 0;font-size:12px;}
.feedback-dot{width:8px;height:8px;border-radius:50%;background:var(--blue);flex-shrink:0;}
.feedback-txt{color:var(--text2);}
.feedback-arrow{color:var(--blue);font-size:14px;}
.spec-card{background:var(--bg);border:1px solid var(--bdr);border-radius:2px;padding:18px;box-shadow:var(--sh);}
.spec-card-title{font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:12px;}
.spec-row{display:flex;align-items:center;justify-content:space-between;padding:8px 0;
  border-bottom:1px solid var(--bdr);font-size:13px;}
.spec-row:last-child{border-bottom:none;}
.spec-name{font-weight:600;color:var(--text);display:flex;align-items:center;gap:8px;}
.spec-name i{color:var(--blue);width:18px;}
.spec-acc{font-weight:700;color:var(--green);}

/* ---- S7 Security ---- */
.s7{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:60px;
  background:linear-gradient(135deg,#F8FAFF 0%,#FFFFFF 100%);}
.s7-title{font-size:13px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:48px;}
.sec-layout{display:flex;align-items:center;gap:80px;}
.sec-rings{position:relative;width:320px;height:320px;flex-shrink:0;}
.sec-ring{position:absolute;border-radius:50%;border:2px solid;
  display:flex;align-items:center;justify-content:center;}
.sec-ring-1{inset:0;border-color:rgba(37,99,235,.15);background:rgba(37,99,235,.03);}
.sec-ring-2{inset:30px;border-color:rgba(37,99,235,.25);background:rgba(37,99,235,.06);}
.sec-ring-3{inset:60px;border-color:var(--blue);background:rgba(37,99,235,.12);}
.sec-center{position:absolute;inset:100px;border-radius:50%;background:var(--blue);
  display:flex;align-items:center;justify-content:center;color:#FFF;font-size:40px;box-shadow:0 0 40px rgba(37,99,235,.4);}
.sec-label{position:absolute;font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
  color:var(--blue);background:var(--bg);padding:2px 6px;border:1px solid var(--blue-lt);border-radius:2px;}
.sec-label-1{top:8px;left:50%;transform:translateX(-50%);}
.sec-label-2{bottom:8px;left:50%;transform:translateX(-50%);}
.sec-label-3{left:8px;top:50%;transform:translateY(-50%);}
.sec-label-4{right:8px;top:50%;transform:translateY(-50%);}
.sec-right{display:flex;flex-direction:column;gap:20px;flex:1;max-width:900px;}
.badge-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;}
.sec-badge{background:var(--bg);border:1px solid var(--bdr);border-radius:2px;padding:16px;text-align:center;box-shadow:var(--sh);}
.sec-badge i{font-size:22px;color:var(--blue);display:block;margin-bottom:8px;}
.sec-badge-name{font-size:12px;font-weight:700;color:var(--text);}
.sec-badge-desc{font-size:10px;color:var(--muted);margin-top:2px;}
.pentest-box{background:var(--green-lt);border:1px solid #86EFAC;border-radius:2px;padding:20px 24px;
  display:flex;align-items:center;justify-content:space-between;}
.pt-left{display:flex;align-items:center;gap:14px;}
.pt-icon{font-size:28px;color:var(--green);}
.pt-title{font-size:15px;font-weight:700;color:var(--text);}
.pt-sub{font-size:12px;color:var(--text2);}
.pt-badge{font-size:28px;font-weight:900;color:var(--green);}

/* ---- S8 Global Scale ---- */
.s8{display:flex;flex-direction:column;background:linear-gradient(180deg,#F8FAFF 0%,#FFFFFF 100%);}
.s8-hdr{padding:36px 60px;display:flex;align-items:center;justify-content:space-between;}
.s8-title{font-size:13px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);}
.s8-meta{display:flex;gap:32px;}
.s8-metric{text-align:right;}
.s8-mn{font-size:28px;font-weight:900;color:var(--blue);}
.s8-ml{font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);}
.map-wrap{flex:1;position:relative;overflow:hidden;}
.map-bg{width:100%;height:100%;
  background-image:radial-gradient(circle,#CBD5E1 1px,transparent 1px);
  background-size:22px 22px;opacity:.5;}
.map-svg{position:absolute;inset:0;}
.city-dot{fill:var(--blue);cursor:pointer;}
.city-dot.hub{fill:var(--blue);r:6;}
.city-line{stroke:var(--blue);stroke-width:1;stroke-opacity:.25;stroke-dasharray:4 4;}
.city-label{font-size:10px;fill:#334155;font-family:'Inter',sans-serif;font-weight:600;}
.city-pulse{fill:none;stroke:var(--blue);stroke-opacity:.3;animation:expand 3s ease-out infinite;}
@keyframes expand{from{r:4;stroke-opacity:.6}to{r:20;stroke-opacity:0}}

/* ---- S9 Outro ---- */
.s9{display:flex;flex-direction:column;align-items:center;justify-content:center;
  background:linear-gradient(160deg,#F0F6FF 0%,#FFFFFF 40%,#F5F3FF 100%);}
.s9-eyebrow{font-size:12px;font-weight:700;color:var(--blue);letter-spacing:.2em;text-transform:uppercase;margin-bottom:20px;}
.s9-title{font-size:100px;font-weight:900;color:var(--text);line-height:1;letter-spacing:-4px;margin-bottom:12px;}
.s9-title span{color:var(--blue);}
.s9-sub{font-size:22px;font-weight:400;color:var(--text2);margin-bottom:56px;}
.s9-lockup{display:flex;align-items:center;gap:40px;margin-bottom:52px;
  padding:28px 48px;background:var(--bg);border:1px solid var(--bdr);border-radius:2px;box-shadow:var(--sh2);}
.s9-rwt-logo{height:44px;object-fit:contain;}
.s9-divider{width:1px;height:44px;background:var(--bdr);}
.s9-harness{display:flex;align-items:center;gap:10px;}
.s9-harness-badge{background:var(--blue);color:#FFF;padding:8px 16px;font-size:13px;font-weight:700;
  letter-spacing:.1em;text-transform:uppercase;border-radius:2px;}
.s9-contact{font-size:15px;color:var(--muted);letter-spacing:.04em;}
.s9-contact strong{color:var(--text);}
</style>
</head>
<body>
<div id="stage">
<div id="camera-group">

<!-- S0: System Initialization -->
<div class="scene s0" data-dur="7000">
  <div class="s0-inner">
    <div class="s0-left">
      <div class="s0-eyebrow au">AI Agent Orchestration Platform</div>
      <div class="s0-title au d1">Serv<span>Claw</span></div>
      <div class="s0-sub au d2">Rapid AI Agent Deployment.<br>Powered by Harness.</div>
      <div class="s0-pills au d3">
        <span class="s0-pill blue">Sub-5s Deployment</span>
        <span class="s0-pill blue">99.99% Uptime</span>
        <span class="s0-pill">30+ Regions</span>
        <span class="s0-pill">ISO 27001 Certified</span>
      </div>
      <div class="s0-harness au d4">
        <i class="fa-solid fa-circle-nodes"></i>
        <span>Powered by Harness CI/CD Infrastructure</span>
      </div>
    </div>
    <div class="s0-right">
      <canvas id="s0-canvas"></canvas>
      <div class="s0-claw-label">ROBOTIC ORCHESTRATION ENGINE</div>
    </div>
  </div>
</div>

<!-- S1: Agent Provisioning -->
<div class="scene s1" data-dur="7000">
  <div class="s1-left">
    <div class="term-bar au">
      <div class="td td-r"></div><div class="td td-y"></div><div class="td td-g"></div>
      <span class="term-title">servclaw-terminal — bash</span>
    </div>
    <div class="au d1 mono" style="font-size:15px;color:#94A3B8;margin-bottom:12px;">
      <span class="t-prompt">$ </span>
      <span class="t-cmd">servclaw deploy <span class="t-flag">--agent</span> <span class="t-val">core_support</span> <span class="t-flag">--env</span> <span class="t-val">production</span></span>
    </div>
    <div class="t-line au d2 mono">Connecting to ServClaw Orchestration Layer...</div>
    <div class="t-line au d2 mono" style="margin-bottom:20px;">Authenticating via Harness RBAC... <span style="color:#22C55E;">OK</span></div>
    <div class="t-step au d3">
      <i class="fa-solid fa-circle-check t-ok"></i>
      <div><div class="t-step-txt">Provisioning compute resources</div>
        <div class="t-step-sub mono">vpc-prod-east-1 — 4 vCPU, 8 GB RAM</div></div>
    </div>
    <div class="t-step au d4">
      <i class="fa-solid fa-circle-check t-ok"></i>
      <div><div class="t-step-txt">Injecting agent logic and knowledge base</div>
        <div class="t-step-sub mono">core_support-v1.0.0.tar.gz (142 MB)</div></div>
    </div>
    <div class="t-step au d5">
      <i class="fa-solid fa-circle-check t-ok"></i>
      <div><div class="t-step-txt">Connecting enterprise data streams</div>
        <div class="t-step-sub mono">CRM, Ticketing, KB — 3 integrations active</div></div>
    </div>
    <div class="t-step au d6">
      <i class="fa-solid fa-circle-check t-ok"></i>
      <div><div class="t-step-txt">Health checks passing — endpoint live</div>
        <div class="t-step-sub mono">https://api.servclaw.io/agents/core_support</div></div>
    </div>
    <div class="t-success-box au d7">
      <div class="t-success-lbl">AGENT DEPLOYED SUCCESSFULLY</div>
      <div class="t-success-val">core_support initialized in 4.7 seconds</div>
    </div>
  </div>
  <div class="s1-right">
    <div class="ac-title">Agent Status Card</div>
    <div class="ac-main apt d2">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px;">
        <div class="dot-live"></div>
        <span class="badge b-green">ACTIVE</span>
      </div>
      <div class="ac-name">core_support</div>
      <div class="ac-ver">v1.0.0 — Production Environment</div>
      <div class="ac-row"><span class="ac-lbl">Agent ID</span><span class="ac-val blue mono">AGT-2024-0891</span></div>
      <div class="ac-row"><span class="ac-lbl">Environment</span><span class="ac-val">Production</span></div>
      <div class="ac-row"><span class="ac-lbl">Region</span><span class="ac-val">UAE East — Dubai</span></div>
      <div class="ac-row"><span class="ac-lbl">Data Streams</span><span class="ac-val">3 Active</span></div>
      <div class="ac-row"><span class="ac-lbl">Memory Usage</span><span class="ac-val">1.4 GB / 8 GB</span></div>
      <div class="ac-row"><span class="ac-lbl">Health</span><span class="ac-val" style="color:var(--green);">All Checks Passing</span></div>
    </div>
    <div class="ac-time apt d4">
      <div class="ac-time-n">4.7s</div>
      <div class="ac-time-l">Deployment Time</div>
    </div>
  </div>
</div>

<!-- S2: Fleet Management -->
<div class="scene s2" data-dur="7000">
  <div class="s2-hdr">
    <div>
      <div class="s2-title au">Agent Fleet Dashboard</div>
      <div class="au d1" style="font-size:13px;color:var(--muted);margin-top:4px;">Real-time orchestration — Auto-scaling enabled</div>
    </div>
    <div class="s2-stats au d2">
      <div class="stat-chip"><div class="stat-n green">12</div><div class="stat-l">Active</div></div>
      <div class="stat-chip"><div class="stat-n amber">3</div><div class="stat-l">Standby</div></div>
      <div class="stat-chip"><div class="stat-n blue">0</div><div class="stat-l">Errors</div></div>
      <div class="stat-chip"><div class="stat-n">15</div><div class="stat-l">Total</div></div>
    </div>
  </div>
  <div class="agent-grid">
    <div class="agent-card au d1">
      <div class="ag-top"><span class="ag-id">AGT-0891</span><span class="badge b-green">ACTIVE</span></div>
      <div class="ag-row"><span class="ag-lbl">Role</span><span class="ag-val">Customer Support</span></div>
      <div class="ag-row"><span class="ag-lbl">Ops Today</span><span class="ag-val">2,841</span></div>
      <div class="ag-row"><span class="ag-lbl">Uptime</span><span class="ag-val" style="color:var(--green)">99.97%</span></div>
      <div class="ag-bars">
        <div class="ag-bar-row"><span class="ag-bar-lbl">CPU</span><div class="ag-bar-track"><div class="ag-bar-fill" style="width:34%"></div></div><span class="ag-bar-val">34%</span></div>
        <div class="ag-bar-row"><span class="ag-bar-lbl">RAM</span><div class="ag-bar-track"><div class="ag-bar-fill" style="width:58%"></div></div><span class="ag-bar-val">58%</span></div>
      </div>
    </div>
    <div class="agent-card au d2">
      <div class="ag-top"><span class="ag-id">AGT-0892</span><span class="badge b-green">ACTIVE</span></div>
      <div class="ag-row"><span class="ag-lbl">Role</span><span class="ag-val">Sales Assistant</span></div>
      <div class="ag-row"><span class="ag-lbl">Ops Today</span><span class="ag-val">1,547</span></div>
      <div class="ag-row"><span class="ag-lbl">Uptime</span><span class="ag-val" style="color:var(--green)">100%</span></div>
      <div class="ag-bars">
        <div class="ag-bar-row"><span class="ag-bar-lbl">CPU</span><div class="ag-bar-track"><div class="ag-bar-fill" style="width:22%"></div></div><span class="ag-bar-val">22%</span></div>
        <div class="ag-bar-row"><span class="ag-bar-lbl">RAM</span><div class="ag-bar-track"><div class="ag-bar-fill" style="width:41%"></div></div><span class="ag-bar-val">41%</span></div>
      </div>
    </div>
    <div class="agent-card au d3">
      <div class="ag-top"><span class="ag-id">AGT-0893</span><span class="badge b-green">ACTIVE</span></div>
      <div class="ag-row"><span class="ag-lbl">Role</span><span class="ag-val">Data Extraction</span></div>
      <div class="ag-row"><span class="ag-lbl">Ops Today</span><span class="ag-val">8,129</span></div>
      <div class="ag-row"><span class="ag-lbl">Uptime</span><span class="ag-val" style="color:var(--green)">99.99%</span></div>
      <div class="ag-bars">
        <div class="ag-bar-row"><span class="ag-bar-lbl">CPU</span><div class="ag-bar-track"><div class="ag-bar-fill amber" style="width:71%"></div></div><span class="ag-bar-val">71%</span></div>
        <div class="ag-bar-row"><span class="ag-bar-lbl">RAM</span><div class="ag-bar-track"><div class="ag-bar-fill" style="width:63%"></div></div><span class="ag-bar-val">63%</span></div>
      </div>
    </div>
    <div class="agent-card au d4">
      <div class="ag-top"><span class="ag-id">AGT-0894</span><span class="badge b-green">ACTIVE</span></div>
      <div class="ag-row"><span class="ag-lbl">Role</span><span class="ag-val">Ops Monitoring</span></div>
      <div class="ag-row"><span class="ag-lbl">Ops Today</span><span class="ag-val">4,302</span></div>
      <div class="ag-row"><span class="ag-lbl">Uptime</span><span class="ag-val" style="color:var(--green)">99.98%</span></div>
      <div class="ag-bars">
        <div class="ag-bar-row"><span class="ag-bar-lbl">CPU</span><div class="ag-bar-track"><div class="ag-bar-fill" style="width:45%"></div></div><span class="ag-bar-val">45%</span></div>
        <div class="ag-bar-row"><span class="ag-bar-lbl">RAM</span><div class="ag-bar-track"><div class="ag-bar-fill" style="width:52%"></div></div><span class="ag-bar-val">52%</span></div>
      </div>
    </div>
    <div class="agent-card standby au d5">
      <div class="ag-top"><span class="ag-id">AGT-0895</span><span class="badge b-amber">STANDBY</span></div>
      <div class="ag-row"><span class="ag-lbl">Role</span><span class="ag-val">Fraud Detection</span></div>
      <div class="ag-row"><span class="ag-lbl">Ops Today</span><span class="ag-val">0</span></div>
      <div class="ag-row"><span class="ag-lbl">Trigger</span><span class="ag-val" style="color:var(--amber)">Threshold: 1k RPS</span></div>
      <div class="ag-bars">
        <div class="ag-bar-row"><span class="ag-bar-lbl">CPU</span><div class="ag-bar-track"><div class="ag-bar-fill" style="width:2%"></div></div><span class="ag-bar-val">2%</span></div>
        <div class="ag-bar-row"><span class="ag-bar-lbl">RAM</span><div class="ag-bar-track"><div class="ag-bar-fill" style="width:8%"></div></div><span class="ag-bar-val">8%</span></div>
      </div>
    </div>
    <div class="agent-card au d6">
      <div class="ag-top"><span class="ag-id">AGT-0896</span><span class="badge b-green">ACTIVE</span></div>
      <div class="ag-row"><span class="ag-lbl">Role</span><span class="ag-val">Report Generator</span></div>
      <div class="ag-row"><span class="ag-lbl">Ops Today</span><span class="ag-val">612</span></div>
      <div class="ag-row"><span class="ag-lbl">Uptime</span><span class="ag-val" style="color:var(--green)">100%</span></div>
      <div class="ag-bars">
        <div class="ag-bar-row"><span class="ag-bar-lbl">CPU</span><div class="ag-bar-track"><div class="ag-bar-fill" style="width:18%"></div></div><span class="ag-bar-val">18%</span></div>
        <div class="ag-bar-row"><span class="ag-bar-lbl">RAM</span><div class="ag-bar-track"><div class="ag-bar-fill" style="width:29%"></div></div><span class="ag-bar-val">29%</span></div>
      </div>
    </div>
    <div class="agent-card au d7">
      <div class="ag-top"><span class="ag-id">AGT-0897</span><span class="badge b-green">ACTIVE</span></div>
      <div class="ag-row"><span class="ag-lbl">Role</span><span class="ag-val">Lead Qualifier</span></div>
      <div class="ag-row"><span class="ag-lbl">Ops Today</span><span class="ag-val">934</span></div>
      <div class="ag-row"><span class="ag-lbl">Uptime</span><span class="ag-val" style="color:var(--green)">99.95%</span></div>
      <div class="ag-bars">
        <div class="ag-bar-row"><span class="ag-bar-lbl">CPU</span><div class="ag-bar-track"><div class="ag-bar-fill" style="width:27%"></div></div><span class="ag-bar-val">27%</span></div>
        <div class="ag-bar-row"><span class="ag-bar-lbl">RAM</span><div class="ag-bar-track"><div class="ag-bar-fill" style="width:38%"></div></div><span class="ag-bar-val">38%</span></div>
      </div>
    </div>
    <div class="agent-card standby au d8">
      <div class="ag-top"><span class="ag-id">AGT-0898</span><span class="badge b-amber">STANDBY</span></div>
      <div class="ag-row"><span class="ag-lbl">Role</span><span class="ag-val">Load Balancer</span></div>
      <div class="ag-row"><span class="ag-lbl">Ops Today</span><span class="ag-val">0</span></div>
      <div class="ag-row"><span class="ag-lbl">Trigger</span><span class="ag-val" style="color:var(--amber)">Auto-scale Event</span></div>
      <div class="ag-bars">
        <div class="ag-bar-row"><span class="ag-bar-lbl">CPU</span><div class="ag-bar-track"><div class="ag-bar-fill" style="width:1%"></div></div><span class="ag-bar-val">1%</span></div>
        <div class="ag-bar-row"><span class="ag-bar-lbl">RAM</span><div class="ag-bar-track"><div class="ag-bar-fill" style="width:5%"></div></div><span class="ag-bar-val">5%</span></div>
      </div>
    </div>
  </div>
</div>

<!-- S3: CI/CD Pipeline -->
<div class="scene s3" data-dur="7000">
  <div class="s3-title au">CI/CD Integration — Powered by Harness</div>
  <div class="pipeline au d2">
    <div class="pipe-node">
      <div class="pipe-circle done"><i class="fa-solid fa-code-branch"></i></div>
      <div class="pipe-lbl">Commit</div>
      <div class="pipe-sub">main branch</div>
    </div>
    <div class="pipe-arrow lit"><i class="fa-solid fa-chevron-right"></i></div>
    <div class="pipe-node">
      <div class="pipe-circle done"><i class="fa-solid fa-hammer"></i></div>
      <div class="pipe-lbl">Build</div>
      <div class="pipe-sub">2m 14s</div>
    </div>
    <div class="pipe-arrow lit"><i class="fa-solid fa-chevron-right"></i></div>
    <div class="pipe-node">
      <div class="pipe-circle done"><i class="fa-solid fa-vial-circle-check"></i></div>
      <div class="pipe-lbl">Test</div>
      <div class="pipe-sub">847 passed</div>
    </div>
    <div class="pipe-arrow lit"><i class="fa-solid fa-chevron-right"></i></div>
    <div class="pipe-node">
      <div class="pipe-circle harness" style="position:relative;">
        <i class="fa-solid fa-rocket"></i>
        <div class="harness-badge">HARNESS</div>
      </div>
      <div class="pipe-lbl">Deploy</div>
      <div class="pipe-sub">Canary release</div>
    </div>
    <div class="pipe-arrow lit"><i class="fa-solid fa-chevron-right"></i></div>
    <div class="pipe-node">
      <div class="pipe-circle active"><i class="fa-solid fa-chart-line"></i></div>
      <div class="pipe-lbl">Monitor</div>
      <div class="pipe-sub">In progress</div>
    </div>
  </div>
  <div class="canary-box au d3">
    <div class="canary-title">Canary Traffic Routing — Version 2.0 Release</div>
    <div class="canary-track">
      <div class="canary-v1">v1.0 — 90% Traffic</div>
      <div class="canary-v2">v2.0</div>
    </div>
    <div class="canary-row">
      <span class="canary-lbl">Traffic split</span><span class="canary-val">v1.0: 90% / v2.0: 10%</span>
      <span class="canary-lbl">Error rate v2.0</span><span class="canary-val green">0.00%</span>
      <span class="canary-lbl">Latency delta</span><span class="canary-val green">+2ms — within threshold</span>
      <span class="canary-lbl">Auto-promote at</span><span class="canary-val">Error rate below 0.1% for 10 min</span>
    </div>
  </div>
</div>

<!-- S4: Governance -->
<div class="scene s4" data-dur="7000">
  <div class="s4-left">
    <div class="s4-title au">Automated Governance</div>
    <div class="policy-grid">
      <div class="policy-card au d2">
        <div class="pc-icon blue"><i class="fa-solid fa-shield-halved"></i></div>
        <div class="pc-name">Security Policy</div>
        <div class="pc-score ok">98</div>
        <div class="pc-label">All endpoints secured</div>
      </div>
      <div class="policy-card au d3">
        <div class="pc-icon green"><i class="fa-solid fa-scale-balanced"></i></div>
        <div class="pc-name">Compliance</div>
        <div class="pc-score ok">100</div>
        <div class="pc-label">ISO 27001, SOC 2 active</div>
      </div>
      <div class="policy-card au d4">
        <div class="pc-icon amber"><i class="fa-solid fa-key"></i></div>
        <div class="pc-name">Access Control</div>
        <div class="pc-score ok">97</div>
        <div class="pc-label">RBAC — least privilege</div>
      </div>
      <div class="policy-card au d5">
        <div class="pc-icon blue"><i class="fa-solid fa-list-check"></i></div>
        <div class="pc-name">Audit Trail</div>
        <div class="pc-score ok">100</div>
        <div class="pc-label">Immutable log — verified</div>
      </div>
    </div>
  </div>
  <div class="s4-right">
    <div class="s4-title au">Policy Engine — Live Request</div>
    <div class="request-box au d2">
      <div class="req-hdr"><i class="fa-solid fa-triangle-exclamation"></i> Access Request Received</div>
      <div class="req-text"><span class="req-agent">Agent #409 (core_support)</span> has requested read-access to the Client Database schema. Evaluating against active policy set.</div>
    </div>
    <div class="flow-steps">
      <div class="flow-step au d3">
        <i class="fa-solid fa-circle-check flow-icon" style="color:var(--green)"></i>
        <div><div class="flow-lbl">Policy Engine Review</div><div class="flow-sub">Role permissions verified — agent scope allows read-only</div></div>
      </div>
      <div class="flow-step au d4">
        <i class="fa-solid fa-circle-check flow-icon" style="color:var(--green)"></i>
        <div><div class="flow-lbl">Data Classification Check</div><div class="flow-sub">Schema metadata — classified: Internal. Access permitted.</div></div>
      </div>
      <div class="flow-step approved au d5">
        <i class="fa-solid fa-circle-check flow-icon" style="color:var(--green)"></i>
        <div><div class="flow-lbl" style="color:var(--green)">Access Approved — Action Logged</div><div class="flow-sub">Cryptographic hash appended to audit trail. Token TTL: 15m.</div></div>
      </div>
    </div>
    <div class="audit-title au d6">Audit Trail — Last 5 Actions</div>
    <div style="background:var(--bg);border:1px solid var(--bdr);border-radius:2px;padding:12px 16px;" class="au d7">
      <div class="audit-entry">
        <span class="audit-time">09:42:18</span>
        <span class="audit-evt">AGT-409 granted read-access to client_db schema</span>
        <span class="audit-hash">sha:7f3a9b...</span>
      </div>
      <div class="audit-entry">
        <span class="audit-time">09:41:55</span>
        <span class="audit-evt">AGT-892 sales query completed — 12 records accessed</span>
        <span class="audit-hash">sha:2c81d4...</span>
      </div>
      <div class="audit-entry">
        <span class="audit-time">09:41:30</span>
        <span class="audit-evt">Policy engine updated — Security Policy v2.4</span>
        <span class="audit-hash">sha:9e04c7...</span>
      </div>
      <div class="audit-entry">
        <span class="audit-time">09:40:12</span>
        <span class="audit-evt">AGT-895 deployment verified — Canary 10% rollout</span>
        <span class="audit-hash">sha:1b77f2...</span>
      </div>
    </div>
  </div>
</div>

<!-- S5: Observability -->
<div class="scene s5" data-dur="7000">
  <div class="s5-stats">
    <div class="obs-stat au d1">
      <div class="os-icon green"><i class="fa-solid fa-bolt"></i></div>
      <div class="os-val">2<span class="os-unit">,847</span></div>
      <div class="os-lbl">Requests / Second</div>
    </div>
    <div class="obs-stat au d2">
      <div class="os-icon green"><i class="fa-solid fa-gauge-high"></i></div>
      <div class="os-val">148<span class="os-unit">ms</span></div>
      <div class="os-lbl">Avg Response Time</div>
    </div>
    <div class="obs-stat au d3">
      <div class="os-icon green"><i class="fa-solid fa-circle-check"></i></div>
      <div class="os-val green">0.03<span class="os-unit">%</span></div>
      <div class="os-lbl">Error Rate</div>
    </div>
    <div class="obs-stat au d4">
      <div class="os-icon blue"><i class="fa-solid fa-server"></i></div>
      <div class="os-val">15<span class="os-unit"> agents</span></div>
      <div class="os-lbl">Active Fleet</div>
    </div>
    <div class="obs-stat alert au d5">
      <div class="os-icon amber"><i class="fa-solid fa-triangle-exclamation"></i></div>
      <div class="os-val amber">1</div>
      <div class="os-lbl">Anomaly Detected</div>
    </div>
  </div>
  <div class="s5-main">
    <div class="chart-panel au d2">
      <div class="panel-hdr"><i class="fa-solid fa-chart-area" style="color:var(--blue)"></i> Request Throughput (60s window)</div>
      <div class="chart-body">
        <div class="chart-bar" style="height:45%"></div><div class="chart-bar" style="height:52%"></div>
        <div class="chart-bar" style="height:48%"></div><div class="chart-bar" style="height:61%"></div>
        <div class="chart-bar" style="height:58%"></div><div class="chart-bar" style="height:72%"></div>
        <div class="chart-bar" style="height:68%"></div><div class="chart-bar" style="height:75%"></div>
        <div class="chart-bar" style="height:70%"></div><div class="chart-bar" style="height:82%"></div>
        <div class="chart-bar" style="height:78%"></div><div class="chart-bar" style="height:74%"></div>
        <div class="chart-bar" style="height:68%"></div><div class="chart-bar" style="height:71%"></div>
        <div class="chart-bar" style="height:65%"></div><div class="chart-bar" style="height:79%"></div>
        <div class="chart-bar" style="height:85%"></div><div class="chart-bar" style="height:92%"></div>
        <div class="chart-bar" style="height:88%"></div><div class="chart-bar" style="height:76%"></div>
        <div class="chart-bar" style="height:80%"></div><div class="chart-bar" style="height:84%"></div>
        <div class="chart-bar" style="height:79%"></div><div class="chart-bar" style="height:75%"></div>
        <div class="chart-bar" style="height:71%"></div><div class="chart-bar" style="height:68%"></div>
        <div class="chart-bar" style="height:73%"></div><div class="chart-bar" style="height:77%"></div>
        <div class="chart-bar" style="height:82%"></div><div class="chart-bar" style="height:86%"></div>
      </div>
    </div>
    <div class="anomaly-panel au d4">
      <div class="alert-banner"><i class="fa-solid fa-triangle-exclamation"></i> ANOMALY DETECTION ACTIVE</div>
      <div class="panel-hdr" style="color:var(--amber)"><i class="fa-solid fa-radar"></i> Detection Feed</div>
      <div class="anomaly-body">
        <div class="anom-entry warn">
          <div class="anom-time">09:42:33</div>
          <div class="anom-evt">Latency spike detected — AGT-0893</div>
          <div class="anom-sub">P99 latency exceeded 500ms threshold. Auto-failover initiated. Zero downtime incurred.</div>
        </div>
        <div class="anom-entry ok">
          <div class="anom-time">09:42:35</div>
          <div class="anom-evt">Failover complete — traffic rerouted to AGT-0897</div>
          <div class="anom-sub">Recovery time: 1.8s. No client-facing disruption recorded.</div>
        </div>
        <div class="anom-entry info">
          <div class="anom-time">09:42:40</div>
          <div class="anom-evt">Root cause analysis initiated</div>
          <div class="anom-sub">Memory pressure on AGT-0893 — scaling event queued.</div>
        </div>
        <div class="anom-entry ok">
          <div class="anom-time">09:42:50</div>
          <div class="anom-evt">All metrics nominal — monitoring resumed</div>
          <div class="anom-sub">System health restored. Incident logged for review.</div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- S6: Agent Intelligence -->
<div class="scene s6" data-dur="7000">
  <div class="s6-left">
    <div class="s6-title au">Agent Intelligence and Optimization</div>
    <div class="trend-box au d2">
      <div class="trend-val">98.5%</div>
      <div class="trend-lbl">Task Resolution Accuracy — core_support</div>
      <div class="trend-chart">
        <div class="tb" style="height:60%"></div><div class="tb" style="height:63%"></div>
        <div class="tb" style="height:67%"></div><div class="tb" style="height:66%"></div>
        <div class="tb" style="height:70%"></div><div class="tb" style="height:72%"></div>
        <div class="tb" style="height:75%"></div><div class="tb" style="height:78%"></div>
        <div class="tb" style="height:80%"></div><div class="tb" style="height:82%"></div>
        <div class="tb" style="height:84%"></div><div class="tb" style="height:86%"></div>
        <div class="tb" style="height:88%"></div><div class="tb" style="height:90%"></div>
        <div class="tb" style="height:93%"></div><div class="tb" style="height:95%"></div>
        <div class="tb" style="height:97%"></div><div class="tb" style="height:98%"></div>
        <div class="tb" style="height:99%"></div><div class="tb" style="height:99%"></div>
      </div>
    </div>
    <div class="feedback-box au d4">
      <div class="feedback-title"><i class="fa-solid fa-rotate"></i> Continuous Learning Loop</div>
      <div class="feedback-row">
        <div class="feedback-dot"></div>
        <span class="feedback-txt">Agent resolves customer query</span>
        <i class="fa-solid fa-arrow-right feedback-arrow"></i>
        <span class="feedback-txt">Human reviewer validates</span>
      </div>
      <div class="feedback-row">
        <div class="feedback-dot"></div>
        <span class="feedback-txt">Feedback ingested to model</span>
        <i class="fa-solid fa-arrow-right feedback-arrow"></i>
        <span class="feedback-txt">Accuracy baseline updates</span>
      </div>
      <div class="feedback-row">
        <div class="feedback-dot"></div>
        <span class="feedback-txt">Agent resolution accuracy increasing via automated human feedback ingestion</span>
      </div>
    </div>
  </div>
  <div class="s6-right">
    <div class="spec-card au d2">
      <div class="spec-card-title">Agent Specialization Registry</div>
      <div class="spec-row">
        <span class="spec-name"><i class="fa-solid fa-headset"></i> Customer Support</span>
        <span class="spec-acc">98.5%</span>
      </div>
      <div class="spec-row">
        <span class="spec-name"><i class="fa-solid fa-chart-bar"></i> Sales Intelligence</span>
        <span class="spec-acc">96.2%</span>
      </div>
      <div class="spec-row">
        <span class="spec-name"><i class="fa-solid fa-gears"></i> Operations Monitor</span>
        <span class="spec-acc">99.1%</span>
      </div>
      <div class="spec-row">
        <span class="spec-name"><i class="fa-solid fa-file-contract"></i> Contract Analysis</span>
        <span class="spec-acc">97.8%</span>
      </div>
      <div class="spec-row">
        <span class="spec-name"><i class="fa-solid fa-shield-halved"></i> Fraud Detection</span>
        <span class="spec-acc">99.7%</span>
      </div>
    </div>
    <div style="background:var(--bg);border:1px solid var(--bdr);border-radius:2px;padding:20px;box-shadow:var(--sh);" class="au d4">
      <div class="panel-hdr" style="border-bottom:none;padding:0 0 14px;font-size:11px;">Learning Velocity</div>
      <div style="display:flex;flex-direction:column;gap:12px;">
        <div>
          <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:6px;">
            <span style="color:var(--muted)">Resolution rate improvement / week</span>
            <span style="font-weight:700;color:var(--green)">+1.4%</span>
          </div>
          <div class="bar-track"><div class="bar-fill bf-green" style="width:74%"></div></div>
        </div>
        <div>
          <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:6px;">
            <span style="color:var(--muted)">Avg feedback loop duration</span>
            <span style="font-weight:700;color:var(--blue)">4.2h</span>
          </div>
          <div class="bar-track"><div class="bar-fill bf-blue" style="width:42%"></div></div>
        </div>
        <div>
          <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:6px;">
            <span style="color:var(--muted)">Human-in-loop corrections this month</span>
            <span style="font-weight:700;color:var(--text)">312</span>
          </div>
          <div class="bar-track"><div class="bar-fill bf-blue" style="width:31%"></div></div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- S7: Security Architecture -->
<div class="scene s7" data-dur="7000">
  <div class="s7-title au">Enterprise Security Architecture</div>
  <div class="sec-layout">
    <div class="sec-rings apt d2">
      <div class="sec-ring sec-ring-1">
        <span class="sec-label sec-label-1">AES-256</span>
        <span class="sec-label sec-label-2">TLS 1.3</span>
        <span class="sec-label sec-label-3">RBAC</span>
        <span class="sec-label sec-label-4">WAF</span>
      </div>
      <div class="sec-ring sec-ring-2"></div>
      <div class="sec-ring sec-ring-3"></div>
      <div class="sec-center"><i class="fa-solid fa-robot"></i></div>
    </div>
    <div class="sec-right">
      <div class="badge-grid au d3">
        <div class="sec-badge">
          <i class="fa-solid fa-file-contract"></i>
          <div class="sec-badge-name">ISO 27001</div>
          <div class="sec-badge-desc">Certified</div>
        </div>
        <div class="sec-badge">
          <i class="fa-solid fa-shield-check"></i>
          <div class="sec-badge-name">SOC 2 Type II</div>
          <div class="sec-badge-desc">Audited annually</div>
        </div>
        <div class="sec-badge">
          <i class="fa-solid fa-scale-balanced"></i>
          <div class="sec-badge-name">UAE PDPL</div>
          <div class="sec-badge-desc">Data residency</div>
        </div>
        <div class="sec-badge">
          <i class="fa-solid fa-lock"></i>
          <div class="sec-badge-name">AES-256</div>
          <div class="sec-badge-desc">At rest and transit</div>
        </div>
        <div class="sec-badge">
          <i class="fa-solid fa-server"></i>
          <div class="sec-badge-name">On-Premise</div>
          <div class="sec-badge-desc">Air-gapped option</div>
        </div>
        <div class="sec-badge">
          <i class="fa-solid fa-flag-checkered"></i>
          <div class="sec-badge-name">UAE Sovereign</div>
          <div class="sec-badge-desc">Cloud verified</div>
        </div>
        <div class="sec-badge">
          <i class="fa-solid fa-eye"></i>
          <div class="sec-badge-name">Zero Trust</div>
          <div class="sec-badge-desc">No implicit access</div>
        </div>
        <div class="sec-badge">
          <i class="fa-solid fa-rotate"></i>
          <div class="sec-badge-name">Key Rotation</div>
          <div class="sec-badge-desc">90-day automated</div>
        </div>
      </div>
      <div class="pentest-box au d5">
        <div class="pt-left">
          <i class="fa-solid fa-terminal pt-icon"></i>
          <div>
            <div class="pt-title">Penetration Test — Last Run: 48h ago</div>
            <div class="pt-sub">27 vectors tested. UAE Data Residency active. On-premise deployment verified. Zero critical findings.</div>
          </div>
        </div>
        <div class="pt-badge">SECURE</div>
      </div>
    </div>
  </div>
</div>

<!-- S8: Global Scale -->
<div class="scene s8" data-dur="7000">
  <div class="s8-hdr">
    <div>
      <div class="s8-title au">Global Infrastructure Deployment</div>
      <div class="au d1" style="font-size:13px;color:var(--muted);margin-top:4px;">Active nodes — real-time</div>
    </div>
    <div class="s8-meta au d2">
      <div class="s8-metric"><div class="s8-mn">50,000+</div><div class="s8-ml">Agents Deployed</div></div>
      <div class="s8-metric"><div class="s8-mn">30</div><div class="s8-ml">Regions Active</div></div>
      <div class="s8-metric"><div class="s8-mn" style="color:var(--green)">99.99%</div><div class="s8-ml">Uptime SLA</div></div>
    </div>
  </div>
  <div class="map-wrap">
    <div class="map-bg"></div>
    <svg class="map-svg" viewBox="0 0 1920 800" xmlns="http://www.w3.org/2000/svg">
      <!-- Connection lines -->
      <line class="city-line" x1="563" y1="220" x2="960" y2="215"/>
      <line class="city-line" x1="960" y1="215" x2="970" y2="218"/>
      <line class="city-line" x1="970" y1="218" x2="1253" y2="348"/>
      <line class="city-line" x1="1253" y1="348" x2="1347" y2="397"/>
      <line class="city-line" x1="1253" y1="348" x2="1514" y2="493"/>
      <line class="city-line" x1="1514" y1="493" x2="1706" y2="300"/>
      <line class="city-line" x1="1514" y1="493" x2="1764" y2="680"/>
      <line class="city-line" x1="563" y1="220" x2="736" y2="628"/>
      <line class="city-line" x1="563" y1="220" x2="592" y2="230"/>
      <line class="city-line" x1="976" y1="448" x2="1347" y2="397"/>
      <line class="city-line" x1="1706" y1="300" x2="1637" y2="295"/>
      <!-- Pulse rings (animation) -->
      <circle cx="1253" cy="348" r="4" fill="none" stroke="#2563EB" stroke-opacity=".4">
        <animate attributeName="r" from="4" to="30" dur="3s" repeatCount="indefinite"/>
        <animate attributeName="stroke-opacity" from=".6" to="0" dur="3s" repeatCount="indefinite"/>
      </circle>
      <circle cx="1514" cy="493" r="4" fill="none" stroke="#2563EB" stroke-opacity=".4">
        <animate attributeName="r" from="4" to="24" dur="2.5s" begin="0.8s" repeatCount="indefinite"/>
        <animate attributeName="stroke-opacity" from=".5" to="0" dur="2.5s" begin="0.8s" repeatCount="indefinite"/>
      </circle>
      <!-- Major city dots -->
      <circle class="city-dot hub" cx="563" cy="220" r="7"/><text class="city-label" x="575" y="217">New York</text>
      <circle class="city-dot hub" cx="960" cy="215" r="7"/><text class="city-label" x="972" y="212">London</text>
      <circle class="city-dot hub" cx="970" cy="218" r="5"/><text class="city-label" x="980" y="235">Paris</text>
      <circle class="city-dot hub" cx="1253" cy="348" r="9" fill="#1D4ED8"/><text class="city-label" x="1265" y="344">Dubai</text>
      <circle class="city-dot hub" cx="1347" cy="397" r="6"/><text class="city-label" x="1358" y="393">Mumbai</text>
      <circle class="city-dot hub" cx="1514" cy="493" r="9" fill="#1D4ED8"/><text class="city-label" x="1526" y="489">Singapore</text>
      <circle class="city-dot hub" cx="1706" cy="300" r="7"/><text class="city-label" x="1718" y="297">Tokyo</text>
      <circle class="city-dot hub" cx="1637" cy="295" r="5"/><text class="city-label" x="1648" y="312">Seoul</text>
      <circle class="city-dot hub" cx="736" cy="628" r="6"/><text class="city-label" x="748" y="624">Sao Paulo</text>
      <circle class="city-dot hub" cx="976" cy="448" r="6"/><text class="city-label" x="988" y="444">Lagos</text>
      <circle class="city-dot hub" cx="1764" cy="680" r="6"/><text class="city-label" x="1776" y="676">Sydney</text>
      <circle class="city-dot hub" cx="592" cy="230" r="5"/><text class="city-label" x="604" y="247">Toronto</text>
    </svg>
  </div>
</div>

<!-- S9: Attribution -->
<div class="scene s9" data-dur="9000">
  <div class="s9-eyebrow au">Red White Tech</div>
  <div class="s9-title au d1">Serv<span>Claw</span></div>
  <div class="s9-sub au d2">Enterprise Agent Orchestration.</div>
  <div class="s9-lockup au d3">
    <img class="s9-rwt-logo" src="__RWT_LOGO__" alt="Red White Tech">
    <div class="s9-divider"></div>
    <div class="s9-harness">
      <i class="fa-solid fa-circle-nodes" style="color:var(--blue);font-size:20px;"></i>
      <div class="s9-harness-badge">Powered by Harness</div>
    </div>
  </div>
  <div class="s9-contact au d4"><strong>Initiate Deployment</strong> — Contact Enterprise Sales</div>
</div>

</div><!-- /camera-group -->

<div id="blur-overlay"></div>
<div id="feature-hdr">
  <i class="fa-solid fa-microchip fh-icon"></i>
  <span class="fh-text">LOADING</span>
</div>
<div id="tl"></div>
</div><!-- /stage -->

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
<script>
/* ---- Fit stage to viewport ---- */
function fit(){
  var W=window.innerWidth,H=window.innerHeight,s=Math.min(W/1920,H/1080);
  document.getElementById('stage').style.transform=
    'translate('+(((W-1920*s)/2)|0)+'px,'+(((H-1080*s)/2)|0)+'px) scale('+s+')';
}
window.addEventListener('resize',fit,{passive:true});
fit();

/* ---- Scene system ---- */
var camGrp=document.getElementById('camera-group');
var fhdr=document.getElementById('feature-hdr');
var blur=document.getElementById('blur-overlay');
var tlWrap=document.getElementById('tl');
var scenes=Array.from(document.querySelectorAll('.scene'));
var durs=scenes.map(function(s){return +(s.dataset.dur)||7000;});
var total=durs.reduce(function(a,b){return a+b;},0);

var ZOOM_CFG=[
  {at:4000,tx:1540,ty:480,sc:1.8,hdr:'ENTERPRISE AGENT ORCHESTRATION'},
  {at:3000,tx:1340,ty:510,sc:2.2,hdr:'SUB-5-SECOND DEPLOYMENT'},
  {at:3000,tx:1430,ty:710,sc:2.0,hdr:'DYNAMIC FLEET SCALING'},
  {at:3000,tx:960, ty:660,sc:2.2,hdr:'HARNESS-POWERED CANARY RELEASES'},
  {at:3000,tx:1440,ty:770,sc:2.1,hdr:'IMMUTABLE AUDIT TRAIL'},
  {at:3000,tx:1440,ty:480,sc:2.0,hdr:'PREDICTIVE ANOMALY DETECTION'},
  {at:3000,tx:700, ty:810,sc:2.2,hdr:'CONTINUOUS LEARNING LOOP'},
  {at:3000,tx:960, ty:760,sc:2.0,hdr:'SOVEREIGN DATA COMPLIANCE'},
  {at:3000,tx:960, ty:380,sc:1.8,hdr:'GLOBAL EDGE DEPLOYMENT'},
  {at:4000,tx:960, ty:540,sc:1.4,hdr:'PROUDLY DEVELOPED BY RED WHITE TECH'}
];

window.__captureConfig={zoomCfg:ZOOM_CFG};

/* Build timeline dots */
scenes.forEach(function(_,i){
  var d=document.createElement('div');d.className='tl-dot';
  d.addEventListener('click',function(){goTo(i,true);});
  tlWrap.appendChild(d);
});
var dots=Array.from(document.querySelectorAll('.tl-dot'));

var idx=0,sceneT=performance.now(),paused=false,transitioning=false;

function setDots(i){
  dots.forEach(function(d,k){
    d.classList.toggle('done',k<i);d.classList.toggle('active',k===i);
  });
}

function setZoom(cfg){
  if(!cfg)return;
  var ex=960-cfg.tx*cfg.sc,ey=540-cfg.ty*cfg.sc;
  camGrp.style.transform='translate('+ex+'px,'+ey+'px) scale('+cfg.sc+')';
  blur.classList.add('visible');
  fhdr.querySelector('.fh-text').textContent=cfg.hdr;
  fhdr.classList.add('visible');
}

function resetZoom(){
  camGrp.style.transform='translate(0px,0px) scale(1)';
  blur.classList.remove('visible');
  fhdr.classList.remove('visible');
}

function goTo(n,user){
  if(n>=scenes.length){if(!user)return;n=0;}
  transitioning=true;
  var prev=scenes[idx],next=scenes[n];
  prev.classList.remove('is-active');prev.classList.add('exiting');
  next.classList.add('entering','is-active');
  resetZoom();
  idx=n;sceneT=performance.now();setDots(n);
  if(ZOOM_CFG[n]){setTimeout(function(){setZoom(ZOOM_CFG[n]);},ZOOM_CFG[n].at);}
  setTimeout(function(){prev.classList.remove('exiting');next.classList.remove('entering');transitioning=false;},600);
}

function tick(now){
  if(!paused&&!transitioning){var el=now-sceneT;if(el>=durs[idx]){goTo(idx+1);}}
  requestAnimationFrame(tick);
}

scenes[0].classList.add('is-active');
setDots(0);
if(ZOOM_CFG[0]){setTimeout(function(){setZoom(ZOOM_CFG[0]);},ZOOM_CFG[0].at);}
requestAnimationFrame(tick);

window.__iris={goTo:goTo,pause:function(){paused=true;},play:function(){paused=false;sceneT=performance.now();},
  scenes:scenes,durations:durs,total:total};

/* Debug mode: press D, click to log stage coordinates */
var _dbg=false;
document.addEventListener('keydown',function(e){
  if(e.key==='d'||e.key==='D'){_dbg=!_dbg;console.log('Debug:',_dbg?'ON':'OFF');}
});
document.addEventListener('click',function(e){
  if(!_dbg)return;
  var st=document.getElementById('stage');
  var r=st.getBoundingClientRect();
  var m=st.style.transform.match(/translate\(([^,]+)px,([^p]+)px\)\s*scale\(([^)]+)\)/);
  if(!m)return;
  var sc=parseFloat(m[3]),ox=parseFloat(m[1]),oy=parseFloat(m[2]);
  var sx=(e.clientX-ox)/sc,sy=(e.clientY-oy)/sc;
  console.log('S'+idx+': tx:'+Math.round(sx)+', ty:'+Math.round(sy));
});

/* ---- Three.js robotic claw (Scene 0) ---- */
(function(){
  function init(){
    if(!window.THREE){setTimeout(init,100);return;}
    var c=document.getElementById('s0-canvas');
    if(!c)return;
    var W=700,H=700;
    var renderer=new THREE.WebGLRenderer({canvas:c,alpha:true,antialias:true});
    renderer.setSize(W,H);renderer.setClearColor(0xFFFFFF,0);

    var scene=new THREE.Scene();
    var camera=new THREE.PerspectiveCamera(42,W/H,.1,100);
    camera.position.set(10,6,14);camera.lookAt(0,2,0);

    var blue=new THREE.LineBasicMaterial({color:0x2563EB,transparent:true,opacity:.85});
    var dim=new THREE.LineBasicMaterial({color:0x2563EB,transparent:true,opacity:.3});
    var grn=new THREE.LineBasicMaterial({color:0x16A34A,transparent:true,opacity:.8});

    var root=new THREE.Group();

    /* Base platform */
    var baseG=new THREE.BoxGeometry(4,.4,4);
    root.add(new THREE.LineSegments(new THREE.WireframeGeometry(baseG),dim));
    root.children[0].position.y=-3.8;

    /* Lower arm */
    var loG=new THREE.CylinderGeometry(.5,.65,3.2,10);
    var lo=new THREE.LineSegments(new THREE.WireframeGeometry(loG),blue);
    lo.position.y=-1.8;root.add(lo);

    /* Elbow joint */
    var ej=new THREE.LineSegments(new THREE.WireframeGeometry(new THREE.OctahedronGeometry(.9,1)),grn);
    ej.position.y=.3;root.add(ej);

    /* Upper arm angled */
    var upG=new THREE.CylinderGeometry(.35,.5,3,10);
    var up=new THREE.LineSegments(new THREE.WireframeGeometry(upG),blue);
    up.position.set(1.8,2.2,0);up.rotation.z=-Math.PI/5;root.add(up);

    /* Wrist */
    var wj=new THREE.LineSegments(new THREE.WireframeGeometry(new THREE.OctahedronGeometry(.65,1)),grn);
    wj.position.set(3.6,4,.0);root.add(wj);

    /* Three claw fingers */
    for(var i=0;i<3;i++){
      var a=(i/3)*Math.PI*2;
      var fg=new THREE.CylinderGeometry(.06,.22,2.4,7);
      var fi=new THREE.LineSegments(new THREE.WireframeGeometry(fg),blue);
      fi.position.set(3.6+Math.sin(a)*1.4,5.6,Math.cos(a)*1.4);
      fi.rotation.z=Math.sin(a)*.6;fi.rotation.x=Math.cos(a)*.6;
      root.add(fi);
    }

    /* Point cloud */
    var pts=[];
    for(var j=0;j<80;j++){
      pts.push((Math.random()-.5)*14,(Math.random()-.5)*12+2,(Math.random()-.5)*14);
    }
    var ptG=new THREE.BufferGeometry();
    ptG.setAttribute('position',new THREE.Float32BufferAttribute(pts,3));
    scene.add(new THREE.Points(ptG,new THREE.PointsMaterial({color:0x2563EB,size:.1,transparent:true,opacity:.35})));

    scene.add(root);

    function animate(){
      requestAnimationFrame(animate);
      root.rotation.y+=.007;
      renderer.render(scene,camera);
    }
    animate();
  }
  init();
})();
</script>
</body>
</html>"""

HTML = HTML.replace('__RWT_LOGO__', LOGO_B64)
out = pathlib.Path('servclaw.html')
out.write_text(HTML, encoding='utf-8')
print('Built ' + str(out) + ' (' + str(round(len(HTML)/1024)) + ' KB)')

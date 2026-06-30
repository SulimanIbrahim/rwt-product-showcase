#!/usr/bin/env node

import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { existsSync, mkdirSync, readFileSync, rmSync } from 'node:fs';
import { dirname, extname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawn } from 'node:child_process';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const DEFAULT_HTML = 'nexarena.html';

const args = parseArgs(process.argv.slice(2));
const fps = readNumber(args.fps, 30);
const width = readNumber(args.width, 1920);
const height = readNumber(args.height, 1080);
const crf = readNumber(args.crf, 16);
const preset = readString(args.preset, 'slow');
const format = readString(args.format, 'mp4');
const frameFormat = normalizeFrameFormat(readString(args.frameFormat, 'jpg'));
const frameExtension = frameFormat === 'jpeg' ? 'jpg' : 'png';
const frameQuality = clamp(readNumber(args.quality, 96), 1, 100);
const htmlPath = resolve(ROOT, readString(args.html, DEFAULT_HTML));
const framesDir = resolve(
  ROOT,
  readString(args.framesDir, `render/iris_frames_${width}x${height}_${fps}fps_${frameExtension}`)
);
const outPath = resolve(
  ROOT,
  readString(args.out, format === 'prores'
    ? `render/iris_launch_edit_${width}x${height}_${fps}fps.mov`
    : `render/iris_launch_edit_${width}x${height}_${fps}fps.mp4`)
);
const shouldEncode = !readFlag(args.noEncode, false);
const cleanFrames = !readFlag(args.noClean, false);
const showControls = readFlag(args.showControls, false) || readFlag(args.showUi, false);
const maxFrames = args.maxFrames === undefined ? null : readNumber(args.maxFrames, null);
const fromMsArg = args.fromMs === undefined ? args['from-ms'] : args.fromMs;
const toMsArg = args.toMs === undefined ? args['to-ms'] : args.toMs;
const durationMsArg = args.durationMs === undefined ? args['duration-ms'] : args.durationMs;
const fromSecondsArg = firstDefined(args.from, args.start, args.fromSeconds, args.fromSec);
const toSecondsArg = firstDefined(args.to, args.end, args.toSeconds, args.toSec);
const durationSecondsArg = firstDefined(args.duration, args.seconds, args.durationSeconds, args.durationSec);

if (!existsSync(htmlPath)) {
  fail(`Cannot find HTML file: ${htmlPath}`);
}
if (fps <= 0 || width <= 0 || height <= 0) {
  fail('fps, width, and height must be positive numbers.');
}
if (!['mp4', 'prores'].includes(format)) {
  fail('format must be "mp4" or "prores".');
}
if (!['png', 'jpeg'].includes(frameFormat)) {
  fail('frame format must be "jpg", "jpeg", or "png".');
}

await main();

// --- local HTTP server (lets CDN resources load; file:// blocks them) ---

async function startLocalServer(rootDir) {
  const MIME = {
    '.html': 'text/html; charset=utf-8',
    '.js': 'application/javascript',
    '.mjs': 'application/javascript',
    '.css': 'text/css',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.svg': 'image/svg+xml',
    '.woff': 'font/woff',
    '.woff2': 'font/woff2',
    '.ico': 'image/x-icon',
    '.json': 'application/json',
  };

  const server = createServer((req, res) => {
    try {
      const urlPath = decodeURIComponent(req.url.split('?')[0]);
      const filePath = resolve(rootDir, '.' + urlPath);
      if (!filePath.startsWith(resolve(rootDir))) {
        res.writeHead(403); res.end('Forbidden'); return;
      }
      if (!existsSync(filePath)) {
        res.writeHead(404); res.end('Not found'); return;
      }
      const contentType = MIME[extname(filePath).toLowerCase()] || 'application/octet-stream';
      res.writeHead(200, { 'Content-Type': contentType, 'Cache-Control': 'no-cache' });
      res.end(readFileSync(filePath));
    } catch {
      res.writeHead(500); res.end('Server error');
    }
  });

  return new Promise(ok => server.listen(0, '127.0.0.1', () => ok({ server, port: server.address().port })));
}

// --- main ---

async function main() {
  console.log(`Opening ${relative(htmlPath)}`);
  console.log(`Viewport: ${width}x${height} at ${fps} fps`);
  console.log(`Frames: ${frameExtension.toUpperCase()}${frameFormat === 'jpeg' ? ` quality ${frameQuality}` : ' lossless'}`);
  console.log(`Playback UI: ${showControls ? 'shown' : 'hidden for clean export'}`);

  if (cleanFrames && existsSync(framesDir)) {
    rmSync(framesDir, { recursive: true, force: true });
  }
  mkdirSync(framesDir, { recursive: true });
  mkdirSync(dirname(outPath), { recursive: true });

  const { server, port: serverPort } = await startLocalServer(ROOT);

  if (!htmlPath.startsWith(ROOT + '/') && htmlPath !== ROOT) {
    server.close();
    fail(`HTML file must live under ${ROOT}`);
  }
  const htmlRelative = htmlPath.slice(ROOT.length + 1);
  const pageUrl = `http://127.0.0.1:${serverPort}/${htmlRelative}`;

  // SwiftShader enables WebGL (Three.js) in headless Chromium.
  const browser = await chromium.launch({
    headless: true,
    args: ['--use-gl=swiftshader', '--ignore-gpu-blocklist'],
  });
  const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 1 });
  page.on('pageerror', error => console.warn(`Page error: ${error.message}`));

  try {
    await page.goto(pageUrl, { waitUntil: 'domcontentloaded' });
    await page.waitForLoadState('networkidle', { timeout: 60000 }).catch(() => {});
    await waitForAssets(page);

    // Read optional capture config exposed by the page (e.g., zoom config in rotation14).
    const captureConfig = await page.evaluate(() => window.__captureConfig || null);
    await installFrameRenderer(page, { showControls, captureConfig });

    const meta = await page.evaluate(() => ({
      total: window.__iris?.total || 0,
      durations: window.__iris?.durations || [],
      sceneCount: window.__iris?.scenes?.length || 0,
    }));

    if (!meta.total || !meta.sceneCount) {
      fail('The page did not expose window.__iris timing data.');
    }

    const fromMs = clamp(
      readTimeMs({ msValue: fromMsArg, secondsValue: fromSecondsArg, fallback: 0 }),
      0, meta.total
    );
    const explicitToMs = hasValue(toMsArg) || hasValue(toSecondsArg)
      ? readTimeMs({ msValue: toMsArg, secondsValue: toSecondsArg, fallback: meta.total })
      : null;
    const durationMs = hasValue(durationMsArg) || hasValue(durationSecondsArg)
      ? readTimeMs({ msValue: durationMsArg, secondsValue: durationSecondsArg, fallback: null })
      : null;
    const toMs = clamp(explicitToMs ?? (durationMs === null ? meta.total : fromMs + durationMs), fromMs, meta.total);
    const frameDuration = 1000 / fps;
    let frameCount = Math.ceil((toMs - fromMs) / frameDuration);
    if (maxFrames !== null) frameCount = Math.min(frameCount, maxFrames);

    console.log(`Scenes: ${meta.sceneCount}`);
    console.log(`Duration: ${((toMs - fromMs) / 1000).toFixed(1)}s (${frameCount} frames)`);
    console.log(`Saving frames to ${relative(framesDir)}`);

    const startedAt = Date.now();
    for (let frame = 0; frame < frameCount; frame++) {
      const ms = Math.min(fromMs + frame * frameDuration, toMs - 0.001);
      await page.evaluate(time => window.__irisCaptureRenderAt(time), ms);
      const screenshotOptions = {
        path: join(framesDir, `frame_${String(frame).padStart(5, '0')}.${frameExtension}`),
        type: frameFormat,
        fullPage: false,
        caret: 'hide',
      };
      if (frameFormat === 'jpeg') screenshotOptions.quality = frameQuality;
      await page.screenshot(screenshotOptions);

      if (frame === 0 || (frame + 1) % fps === 0 || frame + 1 === frameCount) {
        const done = frame + 1;
        const pct = ((done / frameCount) * 100).toFixed(1);
        const elapsed = (Date.now() - startedAt) / 1000;
        const rate = done / Math.max(elapsed, 0.001);
        const remaining = (frameCount - done) / Math.max(rate, 0.001);
        console.log(`Frames ${done}/${frameCount} (${pct}%) - eta ${formatSeconds(remaining)}`);
      }
    }
  } finally {
    await browser.close();
    server.close();
  }

  if (shouldEncode) {
    await encodeVideo({ fps, framesDir, outPath, crf, preset, format, frameExtension });
    console.log(`Video saved to ${relative(outPath)}`);
  } else {
    console.log('Skipped video encode (--no-encode).');
  }
}

// --- asset wait ---

async function waitForAssets(page) {
  await page.evaluate(async () => {
    if (document.fonts?.ready) await document.fonts.ready.catch(() => {});
    const images = Array.from(document.images);
    await Promise.all(images.map(async img => {
      if (img.complete && img.naturalWidth > 0) return;
      if (typeof img.decode === 'function') { await img.decode().catch(() => {}); return; }
      await new Promise(resolve => {
        img.addEventListener('load', resolve, { once: true });
        img.addEventListener('error', resolve, { once: true });
      });
    }));
    const videos = Array.from(document.querySelectorAll('video'));
    await Promise.all(videos.map(video => {
      video.load();
      if (video.readyState >= 1) return Promise.resolve();
      return new Promise(resolve => {
        video.addEventListener('loadedmetadata', resolve, { once: true });
        video.addEventListener('error', resolve, { once: true });
      });
    }));
  });
}

// --- frame renderer (injected into page context) ---

async function installFrameRenderer(page, { showControls, captureConfig }) {
  await page.evaluate(({ showControls: shouldShowControls, captureConfig: cfg }) => {
    // Add BOTH class names: 'capture-mode' (used by both HTML files) and
    // 'iris-capture-mode' (legacy alias kept for compatibility).
    document.documentElement.classList.add('capture-mode', 'iris-capture-mode');
    document.documentElement.classList.toggle('iris-show-controls', shouldShowControls);
    document.documentElement.classList.toggle('iris-clean-export', !shouldShowControls);
    window.dispatchEvent(new Event('resize'));
    window.__iris?.pause?.();

    const TYPE_LINE = 'Track my monthly expenses from FAB Bank and log each transaction';
    const ZOOM_CFG = cfg?.zoomCfg || null;
    const ZOOM_DURATION = 800; // ms — matches the CSS transition on #camera-group

    // Cubic ease-out matching CSS cubic-bezier(0.25,0.46,0.45,0.94) (close enough).
    function easeOut(t) { return 1 - Math.pow(1 - t, 3); }

    // Apply zoom transform and feature-header state for rotation14-style pages.
    // Called every frame with the scene index and local time within that scene.
    function applyZoom(sceneIndex, localMs) {
      const camGrp = document.getElementById('camera-group');
      if (!camGrp) return; // nexarena has no camera-group → skip silently

      const fhdr = document.getElementById('feature-hdr');
      const blurEl = document.getElementById('blur-overlay');
      const zc = ZOOM_CFG ? ZOOM_CFG[sceneIndex] : null;

      if (!zc || localMs < zc.at) {
        // Before or no zoom config: reset to identity
        camGrp.style.transform = 'translate(0px,0px) scale(1)';
        if (fhdr) fhdr.classList.remove('visible');
        return;
      }

      // Interpolate from scale(1)/translate(0,0) toward the target zoom.
      const raw = Math.min(1, (localMs - zc.at) / ZOOM_DURATION);
      const p = easeOut(raw);
      const scale = 1 + (zc.sc - 1) * p;
      // At full zoom: translate(960 - tx*sc, 540 - ty*sc) to center (tx,ty) on screen.
      const finalEx = 960 - zc.tx * zc.sc;
      const finalEy = 540 - zc.ty * zc.sc;
      camGrp.style.transform = `translate(${finalEx * p}px,${finalEy * p}px) scale(${scale})`;

      // Keep blur hidden (already hidden by capture-mode CSS, but make sure).
      if (blurEl) blurEl.classList.remove('visible');

      // Show feature header immediately at zoom start.
      if (fhdr) {
        const fhText = fhdr.querySelector('.fh-text');
        if (fhText) fhText.textContent = zc.hdr;
        fhdr.classList.add('visible');
        fhdr.style.transform = 'translateY(0)';
      }
    }

    function fmt(ms) {
      const s = Math.max(0, Math.floor(ms / 1000));
      return `${String(Math.floor(s / 60)).padStart(2, '0')} : ${String(s % 60).padStart(2, '0')}`;
    }

    window.__irisCaptureRenderAt = async ms => {
      const scenes = window.__iris?.scenes || Array.from(document.querySelectorAll('.scene'));
      const durations = window.__iris?.durations || scenes.map(s => +s.dataset.dur || 5000);
      const total = durations.reduce((a, b) => a + b, 0);
      const clampedMs = Math.max(0, Math.min(ms, total - 0.001));

      let sceneIndex = 0;
      let sceneStart = 0;
      for (let i = 0; i < durations.length; i++) {
        if (clampedMs < sceneStart + durations[i]) { sceneIndex = i; break; }
        sceneStart += durations[i];
      }
      const localMs = clampedMs - sceneStart;
      const activeScene = scenes[sceneIndex];

      // Supports both nexarena (.dot inside .timeline) and rotation14 (.tl-dot).
      const dots = Array.from(document.querySelectorAll('.tl-dot, .timeline .dot'));
      const sceneLabel = document.getElementById('scene-label');
      const timeLabel = document.getElementById('time');

      // Determine exiting scene (IRIS overlap transitions).
      const earlySharedExit = sceneIndex > 1 && sceneIndex <= 3;
      const closingRecapExit = sceneIndex === 12;
      let exitingIndex = localMs < 720 && (earlySharedExit || closingRecapExit) ? sceneIndex - 1 : -1;
      const previousScene = scenes[sceneIndex - 1];
      if (
        localMs < 1050
        && previousScene?.classList.contains('s-era')
        && activeScene?.classList.contains('s-payments')
      ) exitingIndex = sceneIndex - 1;

      scenes.forEach((scene, i) => {
        scene.classList.toggle('is-active', i === sceneIndex);
        scene.classList.toggle('is-exiting', i === exitingIndex);
      });

      dots.forEach((dot, i) => {
        // Handle both class naming conventions across files.
        dot.classList.toggle('is-done', i < sceneIndex);
        dot.classList.toggle('is-active', i === sceneIndex);
        dot.classList.toggle('done', i < sceneIndex);
        dot.classList.toggle('active', i === sceneIndex);
        const progress = i < sceneIndex ? 100 : i === sceneIndex
          ? Math.min(100, (localMs / durations[sceneIndex]) * 100) : 0;
        dot.style.setProperty('--p', `${progress}%`);
      });

      if (sceneLabel && activeScene) {
        sceneLabel.textContent = (activeScene.dataset.screenLabel || `${sceneIndex} · Scene`).toUpperCase();
      }
      if (timeLabel) timeLabel.textContent = `${fmt(clampedMs)} / ${fmt(total)}`;

      const typedLine = document.getElementById('typed-line');
      if (typedLine && activeScene?.classList.contains('s-listen')) {
        typedLine.textContent = TYPE_LINE.slice(0, Math.max(0, Math.floor((localMs - 800) / 56)));
      }

      // Zoom/camera transform for rotation14-style pages.
      applyZoom(sceneIndex, localMs);

      // Sync any data-sync-video elements.
      const pendingVideoSeeks = [];
      for (const video of document.querySelectorAll('video[data-sync-video]')) {
        const inActiveScene = activeScene?.contains(video);
        video.pause();
        if (!inActiveScene) { video.currentTime = 0; continue; }
        const delay = +(video.dataset.delay || 0);
        const speed = +(video.dataset.speed || 0.72);
        const stopMs = +(video.dataset.stop || 6450);
        const mediaMs = Math.max(0, Math.min(localMs - delay, stopMs - delay));
        const dur = Number.isFinite(video.duration) && video.duration > 0 ? video.duration : 999;
        const targetTime = Math.min((mediaMs / 1000) * speed, Math.max(0, dur - 0.05));
        if (Math.abs(video.currentTime - targetTime) > 0.02) {
          pendingVideoSeeks.push(new Promise(resolve => {
            const timer = setTimeout(resolve, 250);
            video.addEventListener('seeked', () => { clearTimeout(timer); resolve(); }, { once: true });
            video.currentTime = targetTime;
          }));
        }
      }
      await Promise.all(pendingVideoSeeks);
      await Promise.all(Array.from(document.querySelectorAll('video[data-sync-video]')).map(video => {
        if (!activeScene?.contains(video) || video.readyState < 2 || !video.requestVideoFrameCallback) {
          return Promise.resolve();
        }
        return new Promise(resolve => {
          const timer = setTimeout(resolve, 140);
          video.requestVideoFrameCallback(() => { clearTimeout(timer); resolve(); });
        });
      }));

      // Two RAF ticks: lets Three.js and CSS paint settle before screenshot.
      await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));

      // Force layout flush, then seek all CSS animations to the exact frame.
      document.body.offsetHeight;
      for (const animation of document.getAnimations({ subtree: true })) {
        const owningScene = animation.effect?.target?.closest?.('.scene');
        const animMs = owningScene
          ? (owningScene.classList.contains('is-active') || owningScene.classList.contains('is-exiting') ? localMs : 0)
          : clampedMs;
        try {
          animation.pause();
          animation.currentTime = Math.max(0, animMs);
        } catch { /* some browser-internal animations reject currentTime writes */ }
      }

      return { sceneIndex, localMs, total };
    };
  }, { showControls, captureConfig });
}

// --- FFmpeg encode ---

async function encodeVideo({ fps, framesDir, outPath, crf, preset, format, frameExtension }) {
  console.log(`Encoding ${relative(outPath)}`);
  const inputPattern = join(framesDir, `frame_%05d.${frameExtension}`);
  const baseArgs = [
    '-hide_banner', '-loglevel', 'error', '-y',
    '-framerate', String(fps), '-start_number', '0',
    '-i', inputPattern,
  ];
  const codecArgs = format === 'prores'
    ? ['-c:v', 'prores_ks', '-profile:v', '3', '-pix_fmt', 'yuv422p10le']
    : ['-c:v', 'libx264', '-preset', preset, '-crf', String(crf), '-pix_fmt', 'yuv420p', '-movflags', '+faststart'];
  await run('ffmpeg', [...baseArgs, ...codecArgs, outPath]);
}

// --- utilities ---

function run(command, commandArgs) {
  return new Promise((res, rej) => {
    const child = spawn(command, commandArgs, { cwd: ROOT, stdio: ['ignore', 'pipe', 'pipe'] });
    let out = '';
    child.stdout.on('data', c => { out += c; });
    child.stderr.on('data', c => { out += c; });
    child.on('error', rej);
    child.on('close', code => code === 0 ? res() : rej(new Error(`${command} exited ${code}\n${out}`)));
  });
}

function parseArgs(rawArgs) {
  const parsed = {};
  for (let i = 0; i < rawArgs.length; i++) {
    const token = rawArgs[i];
    if (!token.startsWith('--')) continue;
    const bare = token.slice(2);
    const eq = bare.indexOf('=');
    if (eq !== -1) {
      parsed[normalizeKey(bare.slice(0, eq))] = bare.slice(eq + 1);
      continue;
    }
    const key = normalizeKey(bare);
    const next = rawArgs[i + 1];
    if (!next || next.startsWith('--')) { parsed[key] = true; }
    else { parsed[key] = next; i++; }
  }
  return parsed;
}

function normalizeKey(key) {
  return key.replace(/-([a-z])/g, (_, l) => l.toUpperCase());
}

function normalizeFrameFormat(value) {
  const n = String(value).toLowerCase();
  return n === 'jpg' ? 'jpeg' : n;
}

function readString(value, fallback) {
  return value === undefined || value === true ? fallback : String(value);
}

function readNumber(value, fallback) {
  if (value === undefined || value === true || value === null) return fallback;
  const n = Number(value);
  return Number.isFinite(n) ? n : fallback;
}

function readTimeMs({ msValue, secondsValue, fallback }) {
  if (hasValue(msValue)) return readNumber(msValue, fallback);
  if (hasValue(secondsValue)) {
    const s = readNumber(secondsValue, null);
    return s === null ? fallback : s * 1000;
  }
  return fallback;
}

function firstDefined(...values) { return values.find(hasValue); }

function hasValue(value) {
  return value !== undefined && value !== null && value !== true && value !== '';
}

function readFlag(value, fallback) {
  if (value === undefined) return fallback;
  if (value === true) return true;
  return ['1', 'true', 'yes', 'on'].includes(String(value).toLowerCase());
}

function clamp(value, min, max) { return Math.min(Math.max(value, min), max); }

function formatSeconds(seconds) {
  if (!Number.isFinite(seconds) || seconds < 0) return 'unknown';
  const r = Math.round(seconds);
  const m = Math.floor(r / 60);
  return m > 0 ? `${m}m ${r % 60}s` : `${r}s`;
}

function relative(path) { return path.replace(`${ROOT}/`, ''); }

function fail(message) { console.error(message); process.exit(1); }

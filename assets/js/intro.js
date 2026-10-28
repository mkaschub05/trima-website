// Scroll scene for the intro: a tall [data-scene] with a sticky stage. p runs from 0 (scene top at the top of the
// screen) to 1 (scene bottom at the bottom of the screen). No scroll hijacking: the page scrolls natively.
//
// PC (hover): CSS does the work – scroll-driven animations where supported, otherwise --p set here.
// Touch: Safari on iPhone mis-reports scroll-driven animations inside a sticky ancestor, so here the script reads
// the scroll position every frame and writes transform/opacity directly on a few elements. A light easing towards
// the target hides the small delay between finger and frame.
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var scene = document.querySelector("[data-scene]");
  if (!scene) return;
  var root = document.documentElement;
  if (reduce) {
    scene.classList.add("static");
    scene.style.setProperty("--p", 1);
    return;
  }
  var touch = window.matchMedia("(hover: none)").matches;
  var cssDriven = !touch && window.CSS && CSS.supports("animation-timeline: --a");

  var top = 0, range = 1, vh = window.innerHeight;
  function measure() {
    vh = window.innerHeight;
    var r = scene.getBoundingClientRect();
    top = r.top + window.scrollY;
    range = Math.max(scene.offsetHeight - vh, 1);
  }
  function progress() { return Math.min(Math.max((window.scrollY - top) / range, 0), 1); }
  function clamp(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }
  function setIntro(p) {
    var inIntro = p < 0.9;
    if (root.classList.contains("in-intro") !== inIntro) root.classList.toggle("in-intro", inIntro);
  }

  // Touch: direct writes, eased.
  var q = function (sel) { return scene.querySelector(sel); };
  var el = {
    figure: q(".figure"), sketch: q(".sketch"), track: q(".cast-track"), inner: q(".cast-in"),
    molten: q(".molten"), glow: q(".glow"), word: q(".wordmark"), hint: q(".scroll-hint"),
    lines: [].slice.call(scene.querySelectorAll(".line"))
  };
  var windows = el.lines.map(function (l) {
    return [parseFloat(l.style.getPropertyValue("--a")) || 0, parseFloat(l.style.getPropertyValue("--b")) || 1];
  });
  // The cast only starts after the visitor really scrolled (finger, wheel, keys), never from load-time shifts.
  var userScrolled = false;
  ["touchstart", "touchmove", "wheel", "keydown"].forEach(function (type) {
    window.addEventListener(type, function () { userScrolled = true; }, { passive: true, once: true });
  });
  var shown = -1;
  function render(p) {
    var c = clamp((p - 0.04) * 2.6), m = clamp((p - 0.1) * 5), f = clamp((p - 0.88) * 8.5);
    el.figure.style.transform = "translate3d(0," + (-(4 + m * 16) * vh / 100).toFixed(1) + "px,0) scale(" + (1 - m * 0.18 - f * 0.04).toFixed(4) + ")";
    el.figure.style.opacity = (1 - f).toFixed(3);
    el.sketch.style.opacity = (0.9 - c * 0.5).toFixed(3);
    el.track.style.transform = "translate3d(0," + ((1 - c) * 100).toFixed(2) + "%,0)";
    el.inner.style.transform = "translate3d(0," + ((c - 1) * 100).toFixed(2) + "%,0)";
    el.molten.style.opacity = (Math.min(c * 12, 1) * Math.min((1 - c) * 12, 1)).toFixed(3);
    el.glow.style.transform = "translate3d(" + (48 - p * 30).toFixed(2) + "%," + (-6 + p * 110).toFixed(2) + "%,0)";
    el.glow.style.opacity = c.toFixed(3);
    el.word.style.opacity = clamp((0.1 - p) * 12).toFixed(3);
    if (el.hint) el.hint.style.opacity = clamp(1 - p * 25).toFixed(3);
    el.lines.forEach(function (l, i) {
      var a = windows[i][0], b = windows[i][1];
      var inn = clamp((p - a) * 9), out = clamp((b - p) * 9);
      l.style.opacity = Math.min(inn, out).toFixed(3);
      l.style.transform = "translate3d(0," + ((1 - inn) * 28).toFixed(1) + "px,0)";
    });
  }

  var current = 0, running = false;
  function tick() {
    var target = userScrolled ? progress() : 0;
    current += (target - current) * 0.22;                  // easing towards the scroll position
    if (Math.abs(target - current) < 0.0005) current = target;
    if (current !== shown) { render(current); shown = current; }
    setIntro(progress());
    if (current !== target) requestAnimationFrame(tick); else running = false;
  }
  function kick() { if (!running) { running = true; requestAnimationFrame(tick); } }

  // PC fallback without scroll-driven CSS: --p on the scene.
  var ticking = false;
  function pcUpdate() {
    var p = progress();
    if (!cssDriven) scene.style.setProperty("--p", p.toFixed(4));
    setIntro(p);
    ticking = false;
  }

  measure();
  window.addEventListener("resize", function () { measure(); touch ? kick() : pcUpdate(); });
  window.addEventListener("load", function () { measure(); touch ? kick() : pcUpdate(); });
  if (touch) {
    window.addEventListener("scroll", kick, { passive: true });
    render(0); shown = 0; setIntro(progress());
  } else {
    window.addEventListener("scroll", function () {
      if (!ticking) { ticking = true; requestAnimationFrame(pcUpdate); }
    }, { passive: true });
    pcUpdate();
  }

  // Intro entrance (engraving drawn in, wordmark wipe) starts once the line art is loaded, so the drawing is
  // never half done before the picture arrives. At most 2.5 s wait on a slow connection.
  var started = false;
  function start() {
    if (started) return;
    started = true;
    void document.body.offsetHeight;
    root.classList.add("intro-on");
  }
  var art = new Image();
  art.onload = art.onerror = start;
  art.src = "/assets/img/justitia-lines-bronze.webp";
  if (art.complete) start();
  setTimeout(start, 2500);
})();

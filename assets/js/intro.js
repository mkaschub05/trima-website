// Scroll scenes for the intro previews. Each [data-scene] is taller than the screen and holds a sticky
// stage; while it scrolls past, --p runs from 0 to 1 and the CSS moves everything from that value.
// No scroll hijacking: the page scrolls normally, the stage only reads the position.
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var scenes = [].slice.call(document.querySelectorAll("[data-scene]"));
  if (!scenes.length) return;
  if (reduce) {
    scenes.forEach(function (s) { s.classList.add("static"); s.style.setProperty("--p", 1); });
    return;
  }
  // With CSS scroll-driven animations the browser moves everything itself (see intro.css); then JS only
  // hides the header while the scene runs and does not touch --p.
  var cssDriven = window.CSS && CSS.supports("animation-timeline: --a");
  // Touch devices: the intro plays by itself (time-based CSS, see intro.css); JS never touches --p there.
  var touch = window.matchMedia("(hover: none)").matches;
  var ticking = false;
  function update() {
    var vh = window.innerHeight;
    scenes.forEach(function (s) {
      var r = s.getBoundingClientRect();
      var total = s.offsetHeight - vh;
      var p = total > 0 ? Math.min(Math.max(-r.top / total, 0), 1) : 0;
      if (!cssDriven && !touch) s.style.setProperty("--p", p.toFixed(4));
      // Header hidden while the scene fills the screen: pinned scene → until 90 %; unpinned (touch) → until half of it has scrolled away.
      var inIntro = total > 0 ? p < 0.9 : r.bottom > vh * 0.5;
      if (s === scenes[0] && document.documentElement.classList.contains("in-intro") !== inIntro) {
        document.documentElement.classList.toggle("in-intro", inIntro);
      }
    });
    ticking = false;
  }
  window.addEventListener("scroll", function () {
    if (!ticking) { ticking = true; requestAnimationFrame(update); }
  }, { passive: true });
  window.addEventListener("resize", update);
  update();
  // Intro entrance (wordmark wipe, figure from darkness) starts once the page is ready.
  void document.body.offsetHeight;
  document.documentElement.classList.add("intro-on");
})();

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
  var ticking = false;
  function update() {
    var vh = window.innerHeight;
    scenes.forEach(function (s) {
      var r = s.getBoundingClientRect();
      var total = s.offsetHeight - vh;
      var p = total > 0 ? Math.min(Math.max(-r.top / total, 0), 1) : 0;
      s.style.setProperty("--p", p.toFixed(4));
      s.classList.toggle("started", p > 0.01);
      if (s === scenes[0]) document.documentElement.classList.toggle("in-intro", p < 0.9);
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

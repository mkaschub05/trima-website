// Trima – small motion layer. Without JS (or with reduced motion) everything is simply visible.
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var root = document.documentElement;

  // Headline: wrap each word so it can rise in one after another.
  document.querySelectorAll("[data-words]").forEach(function (el) {
    var words = el.textContent.trim().split(/\s+/);
    el.textContent = "";
    words.forEach(function (w, i) {
      var outer = document.createElement("span");
      outer.className = "w";
      var inner = document.createElement("span");
      inner.textContent = w;
      inner.style.setProperty("--i", i);
      outer.appendChild(inner);
      el.appendChild(outer);
      if (i < words.length - 1) el.appendChild(document.createTextNode(" "));
    });
    el.setAttribute("aria-label", words.join(" ").replace(/­/g, ""));
  });

  // Reveal on scroll.
  var items = document.querySelectorAll("[data-reveal]");
  if (reduce || !("IntersectionObserver" in window)) {
    items.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  }
  // Above the fold: start right away (forced style flush instead of waiting for a frame or the observer,
  // so the hero never stays hidden in throttled or background tabs).
  void document.body.offsetHeight;
  root.classList.add("ready");
  document.querySelectorAll(".hero [data-reveal]").forEach(function (el) { el.classList.add("in"); });

  // Header gets a firmer background once the page scrolls.
  var header = document.querySelector(".site-header");
  var art = document.querySelector(".hero-art .frame");
  var ticking = false;
  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle("scrolled", y > 8);
    if (art && !reduce && window.innerWidth > 960) art.style.transform = "translateY(" + (y * 0.06).toFixed(1) + "px)";
    ticking = false;
  }
  window.addEventListener("scroll", function () {
    if (!ticking) { ticking = true; requestAnimationFrame(onScroll); }
  }, { passive: true });
  onScroll();

  // Soft light that follows the pointer on cards.
  if (!reduce) {
    document.querySelectorAll("[data-spot]").forEach(function (el) {
      el.addEventListener("pointermove", function (e) {
        var r = el.getBoundingClientRect();
        el.style.setProperty("--mx", (e.clientX - r.left) + "px");
        el.style.setProperty("--my", (e.clientY - r.top) + "px");
      });
    });
  }
})();

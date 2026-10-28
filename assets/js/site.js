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
  var hero = document.querySelector(".hero");
  var art = document.querySelector(".hero-art .frame");
  var ticking = false;
  var pointerOnArt = false;
  function wide() { return window.innerWidth > 960; }
  function setLight(x, y) {
    art.style.setProperty("--lx", x.toFixed(1) + "%");
    art.style.setProperty("--ly", y.toFixed(1) + "%");
  }
  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle("scrolled", y > 8);
    if (art && !reduce) {
      art.style.transform = "translateY(" + (y * (wide() ? 0.06 : 0.12)).toFixed(1) + "px)";
      if (wide() && !pointerOnArt && hero) {
        // Scrolling down the hero moves the light from the head down over the robe.
        var p = Math.min(Math.max(y / hero.offsetHeight, 0), 1);
        setLight(58 - p * 18, 22 + p * 60);
      }
    }
    ticking = false;
  }
  if (art && !reduce) {
    var heroArt = art.parentNode;
    heroArt.addEventListener("pointermove", function (e) {
      if (!wide()) return;
      pointerOnArt = true;
      var r = art.getBoundingClientRect();
      setLight((e.clientX - r.left) / r.width * 100, (e.clientY - r.top) / r.height * 100);
    });
    heroArt.addEventListener("pointerleave", function () { pointerOnArt = false; onScroll(); });
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

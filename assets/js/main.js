/* Ridgeway Roofing & Construction — site behavior */
(function () {
  "use strict";

  /* sticky header shadow */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("scrolled", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* mobile nav */
  var burger = document.querySelector(".nav-burger");
  var nav = document.querySelector(".main-nav");
  if (burger && nav) {
    burger.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = nav.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { nav.classList.remove("open"); });
    });
    document.addEventListener("click", function (e) {
      if (nav.classList.contains("open") && !nav.contains(e.target)) {
        nav.classList.remove("open");
        burger.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* services dropdown (click on mobile, hover handled by CSS focus-within) */
  document.querySelectorAll(".nav-drop > button").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      btn.parentElement.classList.toggle("open");
    });
  });
  document.addEventListener("click", function () {
    document.querySelectorAll(".nav-drop.open").forEach(function (d) { d.classList.remove("open"); });
  });

  /* reveal on scroll */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px" });
    document.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("in"); });
  }

  /* lightbox (any <a data-lightbox> gallery) */
  var lbLinks = Array.prototype.slice.call(document.querySelectorAll("a[data-lightbox]"));
  if (lbLinks.length) {
    var lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML = '<button class="lb-close" aria-label="Close">&times;</button>' +
      '<button class="lb-prev" aria-label="Previous">&#8249;</button>' +
      '<img alt="Project photo">' +
      '<button class="lb-next" aria-label="Next">&#8250;</button>';
    document.body.appendChild(lb);
    var lbImg = lb.querySelector("img");
    var idx = 0;
    var show = function (i) {
      idx = (i + lbLinks.length) % lbLinks.length;
      lbImg.src = lbLinks[idx].getAttribute("href");
      var alt = lbLinks[idx].querySelector("img");
      lbImg.alt = alt ? alt.alt : "Project photo";
      lb.classList.add("open");
    };
    lbLinks.forEach(function (a, i) {
      a.addEventListener("click", function (e) { e.preventDefault(); show(i); });
    });
    lb.querySelector(".lb-close").addEventListener("click", function () { lb.classList.remove("open"); });
    lb.querySelector(".lb-prev").addEventListener("click", function () { show(idx - 1); });
    lb.querySelector(".lb-next").addEventListener("click", function () { show(idx + 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) lb.classList.remove("open"); });
    document.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("open")) return;
      if (e.key === "Escape") lb.classList.remove("open");
      if (e.key === "ArrowLeft") show(idx - 1);
      if (e.key === "ArrowRight") show(idx + 1);
    });
  }

  /* gallery filter */
  var filterBtns = document.querySelectorAll("[data-filter]");
  if (filterBtns.length) {
    filterBtns.forEach(function (b) {
      b.addEventListener("click", function (e) {
        e.preventDefault();
        filterBtns.forEach(function (x) { x.classList.remove("active"); });
        b.classList.add("active");
        var f = b.getAttribute("data-filter");
        document.querySelectorAll("[data-cat]").forEach(function (card) {
          card.style.display = (f === "all" || card.getAttribute("data-cat").indexOf(f) !== -1) ? "" : "none";
        });
      });
    });
  }

  /* footer year */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();

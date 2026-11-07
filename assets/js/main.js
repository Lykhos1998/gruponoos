/* GRUPO NOOS — interacciones del sitio */
(function () {
  "use strict";

  // Número de WhatsApp (formato internacional, sin "+" ni espacios).
  var WHATSAPP = "525523781229";

  var doc = document.documentElement;
  doc.classList.remove("no-js");

  // Header con fondo al hacer scroll
  var header = document.querySelector(".site-header");
  function onScroll() {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 24);
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  // Menú móvil
  var toggle = document.querySelector(".nav-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.querySelectorAll(".nav a").forEach(function (a) {
      a.addEventListener("click", function () {
        document.body.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && document.body.classList.contains("nav-open")) {
        document.body.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  // Aparición al hacer scroll
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("is-visible"); });
  }

  // Contadores animados en estadísticas
  document.querySelectorAll("[data-count]").forEach(function (el) {
    var target = parseInt(el.getAttribute("data-count"), 10);
    if (isNaN(target) || !("IntersectionObserver" in window)) return;
    var done = false;
    var obs = new IntersectionObserver(function (entries) {
      if (done || !entries[0].isIntersecting) return;
      done = true;
      var start = null;
      function tick(t) {
        if (!start) start = t;
        var p = Math.min((t - start) / 1400, 1);
        el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3)));
        if (p < 1) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
      obs.disconnect();
    }, { threshold: 0.5 });
    obs.observe(el);
  });

  // Formulario de contacto → abre WhatsApp con el mensaje armado
  var form = document.getElementById("contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var d = new FormData(form);
      var lines = [
        "Hola, Grupo Noos. Me gustaría solicitar una cotización.",
        "",
        "*Nombre:* " + d.get("nombre"),
        d.get("empresa") ? "*Empresa:* " + d.get("empresa") : null,
        "*Teléfono:* " + d.get("telefono"),
        d.get("correo") ? "*Correo:* " + d.get("correo") : null,
        "*Servicio:* " + d.get("servicio"),
        "",
        d.get("mensaje")
      ].filter(function (l) { return l !== null; });
      var url = "https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(lines.join("\n"));
      window.open(url, "_blank", "noopener");
    });
  }

  // Año del footer
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();

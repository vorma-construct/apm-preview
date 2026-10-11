/* Reformas APM — comportamiento común */


/* Mejoras opcionales. Si el navegador no ejecuta esto, la web sigue funcionando. */
(function(){
  /* Si una foto no se puede descargar, la cambiamos por un píxel transparente:
     así desaparece el icono de "imagen rota" y se ve el fondo incrustado. */
  var PX='data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==';
  document.addEventListener('error', function(e){
    var t=e.target;
    if(t && t.tagName==='IMG' && !t.dataset.px){ t.dataset.px='1'; t.classList.add('ph-err'); t.src=PX; }
  }, true);
  window.addEventListener('load', function(){
    document.querySelectorAll('img').forEach(function(i){
      if(i.complete && i.naturalWidth===0 && !i.dataset.px){ i.dataset.px='1'; i.classList.add('ph-err'); i.src=PX; }
    });
  });

  /* Foto que no carga -> copia incrustada */
  function swap(img){
    if(img.dataset.fbDone) return;
    var src = img.getAttribute('src');
    if(src && window.__FB && window.__FB[src]){
      img.dataset.fbDone='1'; img.classList.remove('img-off'); img.src = window.__FB[src];
    }
  }
  document.addEventListener('error', function(e){
    if(e.target && e.target.tagName==='IMG') swap(e.target);
  }, true);
  function sweep(){
    document.querySelectorAll('img').forEach(function(img){
      if(img.complete && img.naturalWidth===0) swap(img);
    });
  }
  window.addEventListener('load', sweep);
  setTimeout(sweep, 2000);

  /* Marca en el menú la página actual */
  (function(){
    var aqui = location.pathname.replace(/index\.html$/, '');
    document.querySelectorAll('.nav a, .mobile-nav a').forEach(function(a){
      var h = a.getAttribute('href'); if(h && h === aqui) a.classList.add('active');
    });
  })();

  /* Bloquear el scroll del fondo con el menú abierto */
  var cb = document.getElementById('mnav-toggle');
  if(cb) cb.addEventListener('change', function(){
    document.body.classList.toggle('menu-open', cb.checked);
  });

})();



/* Reformas APM — interacciones v2 */
(function () {
  "use strict";

  /* ---- Imágenes que no cargan: dejamos el degradado, sin icono roto ---- */
  // Si existe una copia incrustada (data:) ya se encarga otro script de ponerla:
  // en ese caso no marcamos la imagen como rota.
  function marcarRota(img) {
    if (img.dataset.fbDone) return;                       // ya sustituida
    if (img.dataset.ph) return;  // tiene dibujo de respaldo (clase ph-err): que se vea
    if (window.__FB && window.__FB[img.getAttribute("src")]) return;  // hay copia disponible
    img.classList.add("img-off");
    var mark = img.closest(".brand__mark");
    if (mark) mark.classList.add("is-broken");
  }
  document.addEventListener("error", function (e) {
    var t = e.target;
    if (t && t.tagName === "IMG") setTimeout(function () { marcarRota(t); }, 60);
  }, true);
  // por si alguna ya falló antes de registrar el listener
  window.addEventListener("load", function () {
    setTimeout(function () {
      document.querySelectorAll("img").forEach(function (img) {
        if (img.complete && img.naturalWidth === 0) marcarRota(img);
      });
    }, 120);
  });

  /* ---- Header pegajoso + barra de progreso ---- */
  var header = document.querySelector(".header");
  var bar = document.querySelector(".progress");
  function onScroll() {
    var y = window.scrollY || document.documentElement.scrollTop;
    if (header) header.classList.toggle("is-stuck", y > 10);
    if (bar) {
      var h = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.width = (h > 0 ? (y / h) * 100 : 0) + "%";
    }
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---- Menú móvil (lo abre una casilla CSS; esto solo lo acompaña) ---- */
  var cbMenu = document.getElementById("mnav-toggle");
  var mnav = document.querySelector(".mobile-nav");
  if (cbMenu) {
    cbMenu.addEventListener("change", function () {
      document.body.classList.toggle("menu-open", cbMenu.checked);
    });
  }
  if (mnav) {
    mnav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        if (cbMenu) cbMenu.checked = false;
        document.body.classList.remove("menu-open");
      }
    });
  }

  /* ---- Aparición al hacer scroll ---- */
  function initReveal(root) {
    var items = (root || document).querySelectorAll("[data-reveal]:not(.in)");
    if (!items.length) return;
    if (!("IntersectionObserver" in window)) {
      items.forEach(function (el) { el.classList.add("in"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.08, rootMargin: "0px 0px -30px 0px" });
    items.forEach(function (el) { io.observe(el); });

    /* Red de seguridad: si por lo que sea el observador no dispara,
       un barrido al hacer scroll revela todo lo que ya asomó en pantalla. */
    var barriendo = false;
    function barrido() {
      barriendo = false;
      var lim = (window.innerHeight || 800) * 1.06;
      items.forEach(function (el) {
        if (!el.classList.contains("in") && el.getBoundingClientRect().top < lim) {
          el.classList.add("in");
        }
      });
    }
    function pideBarrido() {
      if (!barriendo) { barriendo = true; requestAnimationFrame(barrido); }
    }
    window.addEventListener("scroll", pideBarrido, { passive: true });
    window.addEventListener("resize", pideBarrido, { passive: true });
    setTimeout(barrido, 900);
  }
  window.__apmReveal = initReveal;
  initReveal(document);

  /* ---- Contadores ---- */
  function initCounters(root) {
    var els = (root || document).querySelectorAll("[data-count]:not([data-done])");
    if (!els.length || !("IntersectionObserver" in window)) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        el.setAttribute("data-done", "1");
        io.unobserve(el);
        var target = parseFloat(el.getAttribute("data-count"));
        var pre = el.getAttribute("data-pre") || "";
        var post = el.getAttribute("data-post") || "";
        var dec = (el.getAttribute("data-dec") === "1");
        var t0 = null, dur = 1100;
        function step(ts) {
          if (!t0) t0 = ts;
          var p = Math.min((ts - t0) / dur, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          var v = target * eased;
          el.textContent = pre + (dec ? v.toFixed(1).replace(".", ",") : Math.round(v)) + post;
          if (p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
      });
    }, { threshold: 0.4 });
    els.forEach(function (el) { io.observe(el); });
  }
  window.__apmCounters = initCounters;
  initCounters(document);

  /* ---- Galería (lightbox) ---- */
  var lb = document.querySelector(".lightbox");
  if (lb) {
    var lbImg = lb.querySelector("img");
    var lbCap = lb.querySelector(".lb-cap");
    document.addEventListener("click", function (e) {
      var item = e.target.closest("[data-lightbox]");
      if (item) {
        e.preventDefault();
        var src = item.getAttribute("data-lightbox");
        var cap = item.getAttribute("data-cap") || "";
        lbImg.setAttribute("src", src);
        lbCap.textContent = cap;
        lb.classList.add("open");
        document.body.style.overflow = "hidden";
        return;
      }
      if (e.target.closest(".lightbox")) {
        lb.classList.remove("open");
        document.body.style.overflow = "";
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && lb.classList.contains("open")) {
        lb.classList.remove("open");
        document.body.style.overflow = "";
      }
    });
  }

  /* ---- Cookies y mapa de Google ---------------------------------------
     El mapa no se carga hasta que el visitante acepta. Si prefiere no
     aceptar, se queda el recuadro con la dirección y el enlace a Google. */
  var KEY = "apm_cookies";
  function leer() {
    try { return localStorage.getItem(KEY); } catch (e) { return window.__apmCk || null; }
  }
  function guardar(v) {
    try { localStorage.setItem(KEY, v); } catch (e) { window.__apmCk = v; }
  }
  function cargarMapas() {
    document.querySelectorAll("[data-map] iframe[data-map-src]").forEach(function (fr) {
      if (!fr.getAttribute("src")) fr.setAttribute("src", fr.getAttribute("data-map-src"));
      var cont = fr.closest("[data-map]");
      if (cont) cont.classList.add("loaded");
    });
  }
  var barra = document.getElementById("cookiebar");
  function mostrarBarra() { if (barra) barra.classList.add("show"); }
  function ocultarBarra() { if (barra) barra.classList.remove("show"); }

  var elegido = leer();
  if (elegido === "accept") cargarMapas();
  else if (!elegido) setTimeout(mostrarBarra, 900);

  document.addEventListener("click", function (e) {
    var btn = e.target.closest("[data-cookie]");
    if (btn) {
      var v = btn.getAttribute("data-cookie");
      guardar(v);
      ocultarBarra();
      if (v === "accept") cargarMapas();
      return;
    }
    // "Ver el mapa" desde la propia tarjeta: acepta y carga
    if (e.target.closest("[data-map-accept]")) {
      guardar("accept");
      ocultarBarra();
      cargarMapas();
      return;
    }
    // Volver a abrir la configuración desde el pie
    if (e.target.closest("[data-cookie-open]")) {
      e.preventDefault();
      mostrarBarra();
    }
  });

  /* ---- Año actual ---- */
  var yr = new Date().getFullYear();
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = yr; });
})();


(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var root = document.documentElement;

  // Revela o nome no topo assim que a página carrega
  requestAnimationFrame(function () {
    document.querySelectorAll('[data-load]').forEach(function (el) { el.classList.add('is-loaded'); });
  });

  // Entradas ao rolar a página, com pequeno atraso entre irmãos
  var items = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
    items.forEach(function (el) {
      var sibs = el.parentElement ? Array.prototype.filter.call(el.parentElement.children, function (c) { return c.hasAttribute('data-reveal'); }) : [];
      var i = sibs.indexOf(el);
      if (i > 0 && !el.style.getPropertyValue('--d')) el.style.setProperty('--d', Math.min(i, 5) * 0.08 + 's');
      io.observe(el);
    });
  } else {
    items.forEach(function (el) { el.classList.add('is-in'); });
  }

  // Números da pesquisa contam até o valor final
  var stats = document.querySelectorAll('.stat b');
  if ('IntersectionObserver' in window && !reduce && stats.length) {
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target, end = parseInt(el.textContent, 10), suffix = el.textContent.replace(/[0-9]/g, '');
        var t0 = null;
        function step(t) {
          if (!t0) t0 = t;
          var p = Math.min((t - t0) / 1200, 1), v = Math.round(end * (1 - Math.pow(1 - p, 3)));
          el.textContent = v + suffix;
          if (p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
        so.unobserve(el);
      });
    }, { threshold: 0.6 });
    stats.forEach(function (el) { so.observe(el); });
  }

  // Navegação some ao rolar para baixo e volta ao rolar para cima; barra de progresso
  var nav = document.querySelector('.nav');
  var bar = document.querySelector('.progress');
  var last = window.scrollY, ticking = false;
  function onScroll() {
    var y = window.scrollY;
    if (nav) {
      nav.classList.toggle('is-scrolled', y > 8);
      nav.classList.toggle('is-hidden', y > last && y > 240);
    }
    if (bar) {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.transform = 'scaleX(' + (max > 0 ? y / max : 0) + ')';
    }
    last = y; ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });
  onScroll();

  // Selo "Ver projeto" que acompanha o cursor sobre as imagens
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  if (fine && !reduce) {
    var badge = document.createElement('div');
    badge.className = 'cursor';
    badge.setAttribute('aria-hidden', 'true');
    document.body.appendChild(badge);
    var x = 0, y = 0, bx = 0, by = 0, raf = null;
    function loop() {
      bx += (x - bx) * 0.2; by += (y - by) * 0.2;
      badge.style.left = bx + 'px'; badge.style.top = by + 'px';
      raf = requestAnimationFrame(loop);
    }
    document.querySelectorAll('[data-cursor]').forEach(function (el) {
      el.addEventListener('mouseenter', function (ev) {
        badge.textContent = el.getAttribute('data-cursor');
        x = bx = ev.clientX; y = by = ev.clientY;
        badge.classList.add('is-on');
        if (!raf) raf = requestAnimationFrame(loop);
      });
      el.addEventListener('mousemove', function (ev) { x = ev.clientX; y = ev.clientY; });
      el.addEventListener('mouseleave', function () {
        badge.classList.remove('is-on');
        cancelAnimationFrame(raf); raf = null;
      });
    });
  }

  // Órbita da foto: segue o mouse no computador e a rolagem no celular
  var orbits = document.querySelectorAll('.orbit__g');
  if (orbits.length && !reduce) {
    var tx = 0, ty = 0, cx = 0, cy = 0, orbitRaf = null;
    var ellipses = document.querySelectorAll('.orbit ellipse');
    function orbitLoop() {
      cx += (tx - cx) * 0.08; cy += (ty - cy) * 0.08;
      var ang = (-16 + cx * 28).toFixed(2), ry = (20 + cy * 10).toFixed(2);
      orbits.forEach(function (g) { g.setAttribute('transform', 'rotate(' + ang + ')'); });
      ellipses.forEach(function (e) { e.setAttribute('ry', ry); });
      if (Math.abs(tx - cx) > 0.001 || Math.abs(ty - cy) > 0.001) orbitRaf = requestAnimationFrame(orbitLoop);
      else orbitRaf = null;
    }
    function kick() { if (!orbitRaf) orbitRaf = requestAnimationFrame(orbitLoop); }
    if (fine) {
      window.addEventListener('mousemove', function (ev) {
        tx = ev.clientX / window.innerWidth * 2 - 1;
        ty = ev.clientY / window.innerHeight * 2 - 1;
        kick();
      }, { passive: true });
    } else {
      window.addEventListener('scroll', function () {
        var y = window.scrollY;
        tx = Math.sin(y / 160);
        ty = Math.cos(y / 240) * 0.8 - 0.8;
        kick();
      }, { passive: true });
    }
  }

  // Compartilhar: WhatsApp, LinkedIn, copiar link e compartilhamento nativo no celular
  document.querySelectorAll('[data-share]').forEach(function (box) {
    var url = location.origin + location.pathname;
    var text = box.getAttribute('data-share-text') || document.title;
    var wa = box.querySelector('[data-share-wa]'), li = box.querySelector('[data-share-li]');
    var cp = box.querySelector('[data-share-copy]'), nat = box.querySelector('[data-share-native]');
    var ok = box.querySelector('.share__ok');
    if (wa) wa.href = 'https://wa.me/?text=' + encodeURIComponent(text + ' ' + url);
    if (li) li.href = 'https://www.linkedin.com/sharing/share-offsite/?url=' + encodeURIComponent(url);
    if (nat && navigator.share && !window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
      nat.hidden = false;
      nat.addEventListener('click', function () { navigator.share({ title: document.title, text: text, url: url }).catch(function () {}); });
    }
    if (cp) cp.addEventListener('click', function () {
      function done() { if (ok) { ok.textContent = 'Link copiado'; setTimeout(function () { ok.textContent = ''; }, 2200); } }
      if (navigator.clipboard) navigator.clipboard.writeText(url).then(done, function () { prompt('Copie o link:', url); });
      else prompt('Copie o link:', url);
    });
  });

  // Alternar modo claro/escuro
  var tt = document.querySelector('[data-theme-toggle]');
  function syncToggle() {
    var dark = root.getAttribute('data-theme') === 'dark';
    if (tt) tt.setAttribute('aria-label', dark ? 'Mudar para modo claro' : 'Mudar para modo escuro');
    var m = document.querySelector('meta[name=theme-color]');
    if (m) m.setAttribute('content', dark ? '#0e0f11' : '#f3f4f5');
  }
  if (tt) {
    syncToggle();
    tt.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('tema', next); } catch (e) {}
      syncToggle();
    });
  }

  // Copiar e-mail
  document.querySelectorAll('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var t = b.getAttribute('data-copy'), label = b.textContent;
      if (!navigator.clipboard) { window.location.href = 'mailto:' + t; return; }
      navigator.clipboard.writeText(t).then(function () {
        b.textContent = 'E-mail copiado';
        setTimeout(function () { b.textContent = label; }, 2200);
      }, function () { window.location.href = 'mailto:' + t; });
    });
  });

  var ano = document.getElementById('ano');
  if (ano) ano.textContent = new Date().getFullYear();
})();

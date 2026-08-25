// Mobile navigation disclosure. The `has-js` class is what lets the CSS
// collapse the nav behind the toggle -- without JS the nav stays a plain
// visible list.
(function () {
  var btn = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (!btn || !nav) return;

  document.documentElement.classList.add('has-js');

  function close() {
    btn.setAttribute('aria-expanded', 'false');
    nav.classList.remove('is-open');
  }

  btn.addEventListener('click', function () {
    var open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!open));
    nav.classList.toggle('is-open', !open);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && btn.getAttribute('aria-expanded') === 'true') {
      close();
      btn.focus();
    }
  });
})();

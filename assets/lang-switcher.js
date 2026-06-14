// Shared language switching logic for agent-architecture-notes
(function() {
  var BASE = '/agent-architecture-notes';

  function getCurrentLang() {
    return window.location.pathname.indexOf('/zh/') !== -1 ? 'zh' : 'en';
  }

  function getPagePath() {
    var path = window.location.pathname.replace(BASE, '');
    if (path.indexOf('/zh/') === 0) {
      path = path.replace('/zh/', '/');
    }
    return path;
  }

  window.switchLang = function(lang) {
    if (lang === getCurrentLang()) return;
    localStorage.setItem('lang', lang);
    var newPath = lang === 'zh' ? BASE + '/zh' + getPagePath() : BASE + getPagePath();
    window.location.href = newPath;
  };

  // Set active class on nav after DOM ready
  document.addEventListener('DOMContentLoaded', function() {
    var current = getCurrentLang();
    var links = document.querySelectorAll('.lang-nav a');
    for (var i = 0; i < links.length; i++) {
      var link = links[i];
      var lang = link.getAttribute('data-lang');
      if (lang === current) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
      link.addEventListener('click', function(e) {
        e.preventDefault();
        window.switchLang(this.getAttribute('data-lang'));
      });
    }
  });
})();

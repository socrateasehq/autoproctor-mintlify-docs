// Add language selector and home icon to the sidebar logo row.
// Uses MutationObserver to re-apply after client-side navigation.
(function () {
  var LANGUAGES = [
    { code: 'en', label: 'English', prefix: '' },
    { code: 'es', label: 'Español', prefix: '/es' },
    { code: 'pt', label: 'Português', prefix: '/pt' }
  ];

  function getCurrentLang() {
    var path = window.location.pathname;
    for (var i = 0; i < LANGUAGES.length; i++) {
      if (LANGUAGES[i].prefix && path.startsWith(LANGUAGES[i].prefix + '/')) {
        return LANGUAGES[i];
      }
    }
    return LANGUAGES[0]; // English (default)
  }

  function switchLanguage(targetLang) {
    var currentLang = getCurrentLang();
    var path = window.location.pathname;

    // Strip current language prefix.
    if (currentLang.prefix) {
      path = path.substring(currentLang.prefix.length);
    }

    // Add target language prefix.
    var newPath = targetLang.prefix + path;
    window.location.href = newPath || '/';
  }

  function setup() {
    var sidebar = document.querySelector('nav[aria-label="Pages"]');
    if (!sidebar) return false;

    var logoRow = sidebar.querySelector('#sidebar-content > div:first-child');
    if (!logoRow) return false;

    // Remove previous instance if it exists (handles re-renders).
    var existing = logoRow.querySelector('.custom-sidebar-icons');
    if (existing) existing.remove();

    var currentLang = getCurrentLang();

    // Create container.
    var icons = document.createElement('div');
    icons.className = 'custom-sidebar-icons';
    icons.style.cssText = 'display:flex;align-items:center;gap:0.625rem;';

    // --- Language selector (dropdown) ---
    var langContainer = document.createElement('div');
    langContainer.style.cssText = 'position:relative;';

    var langBtn = document.createElement('button');
    langBtn.type = 'button';
    langBtn.title = 'Select language';
    langBtn.style.cssText = 'font-size:0.75rem;color:#6b7280;cursor:pointer;display:flex;align-items:center;gap:0.25rem;border:none;background:none;padding:0.25rem 0.375rem;border-radius:0.375rem;transition:background .15s;line-height:1;';
    langBtn.onmouseenter = function () { this.style.background = '#f3f4f6'; };
    langBtn.onmouseleave = function () { this.style.background = 'none'; };
    // Globe SVG icon.
    langBtn.innerHTML =
      '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' +
      '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/>' +
      '<path d="M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/>' +
      '</svg>' +
      '<span>' + currentLang.label + '</span>' +
      '<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>';

    var dropdown = document.createElement('div');
    dropdown.style.cssText = 'display:none;position:absolute;top:100%;left:0;margin-top:0.25rem;background:white;border:1px solid #e5e7eb;border-radius:0.5rem;box-shadow:0 4px 12px rgba(0,0,0,0.1);z-index:100;min-width:8rem;padding:0.25rem;';

    LANGUAGES.forEach(function (lang) {
      var item = document.createElement('button');
      item.type = 'button';
      item.style.cssText = 'display:block;width:100%;text-align:left;padding:0.375rem 0.625rem;font-size:0.75rem;color:' + (lang.code === currentLang.code ? '#1f398a' : '#374151') + ';background:none;border:none;cursor:pointer;border-radius:0.375rem;font-weight:' + (lang.code === currentLang.code ? '600' : '400') + ';';
      item.textContent = lang.label;
      item.onmouseenter = function () { this.style.background = '#f3f4f6'; };
      item.onmouseleave = function () { this.style.background = 'none'; };
      item.onclick = function () {
        if (lang.code !== currentLang.code) switchLanguage(lang);
        dropdown.style.display = 'none';
      };
      dropdown.appendChild(item);
    });

    langBtn.onclick = function (e) {
      e.stopPropagation();
      dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none';
    };

    // Close dropdown on outside click.
    document.addEventListener('click', function () {
      dropdown.style.display = 'none';
    });

    langContainer.appendChild(langBtn);
    langContainer.appendChild(dropdown);
    icons.appendChild(langContainer);

    // --- Home icon ---
    var homeLink = document.createElement('a');
    homeLink.href = 'https://www.autoproctor.co';
    homeLink.target = '_blank';
    homeLink.rel = 'noopener noreferrer';
    homeLink.title = 'Go to AutoProctor';
    homeLink.style.cssText = 'color:#6b7280;display:flex;align-items:center;transition:color .15s;';
    homeLink.onmouseenter = function () { this.style.color = '#1f398a'; };
    homeLink.onmouseleave = function () { this.style.color = '#6b7280'; };
    homeLink.innerHTML =
      '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-4 0a1 1 0 01-1-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 01-1 1h-2z"/>' +
      '</svg>';

    icons.appendChild(homeLink);

    logoRow.appendChild(icons);
    return true;
  }

  // Initial setup with retry.
  var attempts = 0;
  var interval = setInterval(function () {
    if (setup() || attempts > 50) clearInterval(interval);
    attempts++;
  }, 200);

  // Re-apply after client-side navigations.
  var observer = new MutationObserver(function () {
    var sidebar = document.querySelector('nav[aria-label="Pages"]');
    if (sidebar && !sidebar.querySelector('.custom-sidebar-icons')) {
      setup();
    }
  });
  observer.observe(document.body, { childList: true, subtree: true });
})();

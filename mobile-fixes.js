/*
  Mobile-only home scroll reset.
  Below 1024px, arriving on the home page (link, browser back, or bfcache)
  starts at the top. Desktop never touches scroll restoration.
  In-page hashes are left to the browser.
*/
(function () {
  var QUERY = "(max-width: 1023px)";
  var HOME = { "/": 1, "/he": 1, "/en": 1 };
  var lastKey = location.pathname + location.search + location.hash;
  var resetToken = 0;

  function mobile() {
    return window.matchMedia(QUERY).matches;
  }

  function homePath() {
    var path = location.pathname.replace(/\/index\.html$/, "").replace(/\/+$/, "");
    if (!path) path = "/";
    return HOME[path] === 1;
  }

  function syncRestoration() {
    if (!("scrollRestoration" in history)) return;
    history.scrollRestoration = mobile() ? "manual" : "auto";
  }

  function forceTop() {
    var token = ++resetToken;
    var run = function () {
      if (token !== resetToken) return;
      if (!mobile() || !homePath() || location.hash) return;
      var root = document.documentElement;
      var previous = root.style.scrollBehavior;
      root.style.scrollBehavior = "auto";
      window.scrollTo(0, 0);
      root.style.scrollBehavior = previous;
    };
    run();
    requestAnimationFrame(function () {
      requestAnimationFrame(run);
    });
    [0, 60, 180, 400].forEach(function (delay) {
      setTimeout(run, delay);
    });
  }

  function onArrival(fromCache) {
    syncRestoration();
    var key = location.pathname + location.search + location.hash;
    var changed = key !== lastKey;
    lastKey = key;
    if (!mobile() || !homePath() || location.hash) return;
    if (!fromCache && !changed) return;
    forceTop();
  }

  syncRestoration();

  window.addEventListener("pageshow", function (event) {
    onArrival(event.persisted);
  });

  window.addEventListener("popstate", function () {
    onArrival(false);
  });

  window.addEventListener("hashchange", function () {
    lastKey = location.pathname + location.search + location.hash;
    resetToken += 1;
  });

  var pushState = history.pushState;
  var replaceState = history.replaceState;
  history.pushState = function () {
    var result = pushState.apply(this, arguments);
    onArrival(false);
    return result;
  };
  history.replaceState = function () {
    var result = replaceState.apply(this, arguments);
    onArrival(false);
    return result;
  };

  window.addEventListener(
    "touchstart",
    function () {
      resetToken += 1;
    },
    { passive: true }
  );
  window.addEventListener(
    "wheel",
    function () {
      resetToken += 1;
    },
    { passive: true }
  );

  window.addEventListener("resize", syncRestoration);
})();

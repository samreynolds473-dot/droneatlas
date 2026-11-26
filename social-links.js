/*
  Social profile URLs. Leave a value empty until the account exists.
  A non-empty URL is applied to the matching link and opens in a new tab.

  The rows are inserted after hydration because the pages are a Next.js
  client render. React would drop markup that is not in its tree.
*/
(function () {
  var URLS = {
    facebook: "",
    instagram: "",
    linkedin: ""
  };

  window.DRONEATLAS_SOCIAL = URLS;

  var COPY = {
    he: {
      group: "רשתות חברתיות",
      facebook: "פייסבוק",
      instagram: "אינסטגרם",
      linkedin: "לינקדאין"
    },
    en: {
      group: "Social media",
      facebook: "Facebook",
      instagram: "Instagram",
      linkedin: "LinkedIn"
    }
  };

  var ICONS = {
    facebook:
      '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="width:20px;height:20px;display:block"><path d="M14.2 8.2H16.5V5.5h-2.4C11.6 5.5 10.4 7 10.4 9.4V11H8v2.6h2.4V20h2.8v-6.4h2.3l.4-2.6h-2.7V9.6c0-.7.3-1.4 1-1.4z"/></svg>',
    instagram:
      '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true" style="width:20px;height:20px;display:block"><rect x="4.5" y="4.5" width="15" height="15" rx="4"/><circle cx="12" cy="12" r="3.4"/><circle cx="17.2" cy="6.8" r="0.9" fill="currentColor" stroke="none"/></svg>',
    linkedin:
      '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="width:20px;height:20px;display:block"><path d="M6.7 9.4H4.2V20h2.5V9.4zM5.4 4C4.5 4 3.8 4.7 3.8 5.6S4.5 7.2 5.4 7.2 7 6.5 7 5.6 6.3 4 5.4 4zM20 20h-2.5v-5.5c0-1.5-.6-2.5-2-2.5-1 0-1.6.7-1.9 1.4-.1.2-.1.6-.1.9V20H11V9.4h2.4v1.5c.4-.8 1.4-1.8 3.2-1.8 2.3 0 3.4 1.5 3.4 4.6V20z"/></svg>'
  };

  var ROW_STYLE = "display:flex;flex-direction:row;flex-wrap:wrap;align-items:center;justify-content:flex-start;gap:0.65rem;margin:1.75rem 0 0;padding:0;list-style:none";
  var LINK_STYLE = "display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;box-sizing:border-box;flex:0 0 auto;border:1px solid color-mix(in srgb, currentColor 32%, transparent);border-radius:999px;text-decoration:none";

  function language() {
    return document.documentElement.lang === "en" ? "en" : "he";
  }

  function configured() {
    var keys = ["facebook", "instagram", "linkedin"];
    var items = [];
    for (var i = 0; i < keys.length; i++) {
      var url = (URLS[keys[i]] || "").trim();
      if (url) items.push({ key: keys[i], url: url });
    }
    return items;
  }

  function buildRow(items) {
    var copy = COPY[language()];
    var list = document.createElement("ul");
    list.className = "social-row";
    list.setAttribute("aria-label", copy.group);
    list.setAttribute("style", ROW_STYLE);
    items.forEach(function (item) {
      var li = document.createElement("li");
      li.setAttribute("style", "display:flex;margin:0;padding:0;list-style:none");
      var link = document.createElement("a");
      link.href = item.url;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.setAttribute("style", LINK_STYLE);
      link.setAttribute("data-social", item.key);
      link.setAttribute("aria-label", copy[item.key]);
      link.innerHTML = ICONS[item.key];
      li.appendChild(link);
      list.appendChild(li);
    });
    return list;
  }

  function applyUrls(root) {
    var links = (root || document).querySelectorAll("a[data-social]");
    for (var i = 0; i < links.length; i++) {
      var link = links[i];
      var url = (URLS[link.getAttribute("data-social")] || "").trim();
      if (!url) {
        link.href = "#";
        link.removeAttribute("target");
        link.removeAttribute("rel");
        continue;
      }
      link.href = url;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
    }
  }

  function place(slot, items, beforeHeading) {
    if (!slot) return;
    var existing = slot.querySelector(".social-row");
    if (!items.length) {
      if (existing) existing.remove();
      return;
    }
    if (existing) return;
    var row = buildRow(items);
    if (beforeHeading) {
      var heading = slot.querySelector("h3");
      if (heading) slot.insertBefore(row, heading);
      else slot.appendChild(row);
    } else {
      slot.appendChild(row);
    }
  }

  function ensure() {
    var items = configured();
    place(document.querySelector("footer .lg\\:col-span-4"), items, false);
    place(document.querySelector("#contact .lg\\:col-span-5"), items, true);
  }

  document.addEventListener("click", function (event) {
    var link = event.target.closest && event.target.closest("a[data-social]");
    if (!link) return;
    var url = (URLS[link.getAttribute("data-social")] || "").trim();
    if (url) return;
    event.preventDefault();
  });

  var scheduled = false;
  function schedule() {
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(function () {
      scheduled = false;
      ensure();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", schedule);
  } else {
    schedule();
  }

  new MutationObserver(schedule).observe(document.documentElement, {
    childList: true,
    subtree: true
  });

  window.addEventListener("pageshow", schedule);
})();

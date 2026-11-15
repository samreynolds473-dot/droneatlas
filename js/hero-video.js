/* Three placeholder clips, played once each, then crossfaded.
   Missing files are skipped. If none exist, the poster image stays. */
(() => {
  const stages = [...document.querySelectorAll("[data-hero-stage]")];
  if (!stages.length) return;

  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const narrow = matchMedia("(max-width: 720px)").matches;
  const conn = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
  const saveData = !!(conn && (conn.saveData || /2g/.test(conn.effectiveType || "")));
  if (reduce || narrow || saveData) return;

  const tag = document.querySelector("script[src*='hero-video.js']");
  if (!tag) return;
  const root = tag.src.replace(/\/js\/hero-video\.js.*$/, "");

  function exists(url) {
    return fetch(url, { method: "HEAD" }).then((res) => {
      if (res.ok) return true;
      if (res.status === 405 || res.status === 501) {
        return fetch(url, { method: "GET", headers: { Range: "bytes=0-0" } }).then(
          (g) => g.ok || g.status === 206
        );
      }
      return false;
    }).catch(() => false);
  }

  function resolveClips() {
    const jobs = [1, 2, 3].map(async (n) => {
      const webm = root + "/assets/video/hero-" + n + ".webm";
      const mp4 = root + "/assets/video/hero-" + n + ".mp4";
      if (await exists(webm)) return webm;
      if (await exists(mp4)) return mp4;
      return null;
    });
    return Promise.all(jobs).then((list) => list.filter(Boolean));
  }

  function makeVideo(poster) {
    const v = document.createElement("video");
    v.className = "hero-vid";
    v.muted = true;
    v.defaultMuted = true;
    v.playsInline = true;
    v.autoplay = true;
    v.preload = "none";
    v.setAttribute("muted", "");
    v.setAttribute("playsinline", "");
    v.setAttribute("autoplay", "");
    v.setAttribute("aria-hidden", "true");
    v.tabIndex = -1;
    if (poster) v.poster = poster;
    return v;
  }

  function mount(stage, clips) {
    const img = stage.querySelector("img");
    const poster = img ? (img.currentSrc || img.getAttribute("src") || "") : "";
    const a = makeVideo(poster);
    const b = makeVideo(poster);
    stage.appendChild(a);
    stage.appendChild(b);
    const host = stage.classList.contains("hero") || stage.classList.contains("page-hero")
      ? stage
      : stage.closest(".hero, .page-hero");
    if (host) host.classList.add("has-video");

    let cur = a;
    let nxt = b;
    let index = 0;
    let alive = true;

    function arm(video, src) {
      if (video.dataset.src === src) return;
      video.dataset.src = src;
      video.preload = "metadata";
      video.poster = src.replace(/hero-(\d+)\.(webm|mp4)(\?.*)?$/, "hero-$1-poster.jpg");
      video.src = src;
    }

    function failAll() {
      alive = false;
      a.remove();
      b.remove();
      if (host) host.classList.remove("has-video");
    }

    function play(video) {
      const attempt = video.play();
      if (attempt && attempt.catch) attempt.catch(() => {});
    }

    function show(video) {
      video.classList.add("is-on");
      play(video);
    }

    function bind(video) {
      video.addEventListener("playing", () => {
        if (!alive || video !== cur) return;
        const ahead = clips[(index + 1) % clips.length];
        arm(nxt, ahead);
      }, { once: true });
      video.addEventListener("ended", () => {
        if (!alive || video !== cur) return;
        const nextIndex = (index + 1) % clips.length;
        const go = () => {
          if (!alive) return;
          show(nxt);
          cur.classList.remove("is-on");
          const old = cur;
          window.setTimeout(() => { if (alive) old.pause(); }, 900);
          cur = nxt;
          nxt = old;
          index = nextIndex;
          bind(cur);
        };
        if (nxt.readyState >= 2) go();
        else nxt.addEventListener("canplay", go, { once: true });
      }, { once: true });
      video.addEventListener("error", () => {
        if (video === cur) failAll();
      }, { once: true });
    }

    arm(cur, clips[0]);
    cur.addEventListener("canplay", () => { if (alive) show(cur); }, { once: true });
    bind(cur);
  }

  resolveClips().then((clips) => {
    if (!clips.length) return;
    stages.forEach((stage) => mount(stage, clips));
  });
})();

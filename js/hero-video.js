/* Three clips, each played once, then crossfaded. The poster stays until
   the first clip is actually playing. If play() is rejected, the poster remains. */
(() => {
  const stages = [...document.querySelectorAll("[data-hero-stage]")];
  if (!stages.length) return;

  const narrow = matchMedia("(max-width: 480px)").matches;
  const conn = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
  const saveData = !!(conn && (conn.saveData || /2g/.test(conn.effectiveType || "")));
  if (narrow || saveData) return;

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
    v.preload = "auto";
    v.setAttribute("muted", "");
    v.setAttribute("playsinline", "");
    v.setAttribute("autoplay", "");
    v.setAttribute("preload", "auto");
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
    b.autoplay = false;
    b.preload = "none";
    b.removeAttribute("autoplay");
    b.setAttribute("preload", "none");
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

    function arm(video, src, primary) {
      if (video.dataset.src === src) return;
      video.dataset.src = src;
      video.muted = true;
      video.defaultMuted = true;
      video.playsInline = true;
      video.preload = primary ? "auto" : "metadata";
      video.poster = src.replace(/hero-(\d+)\.(webm|mp4)(\?.*)?$/, "hero-$1-poster.jpg");
      if (primary) {
        video.autoplay = true;
        video.setAttribute("autoplay", "");
        video.setAttribute("preload", "auto");
      } else {
        video.autoplay = false;
        video.removeAttribute("autoplay");
        video.setAttribute("preload", "metadata");
      }
      video.src = src;
    }

    function failAll() {
      alive = false;
      a.remove();
      b.remove();
      if (host) host.classList.remove("has-video");
    }

    function reveal(video) {
      if (!alive || video !== cur) return;
      video.classList.add("is-on");
    }

    function kick(video) {
      const attempt = video.play();
      if (attempt && attempt.then) {
        attempt.then(() => reveal(video)).catch(() => {
          /* Poster stays. The clip remains hidden at opacity 0. */
        });
      }
      return attempt;
    }

    function bind(video) {
      video.addEventListener("playing", () => reveal(video));
      video.addEventListener("loadeddata", () => {
        if (!alive || video !== cur || video.classList.contains("is-on")) return;
        if (!video.paused) reveal(video);
        else kick(video);
      });
      video.addEventListener("playing", () => {
        if (!alive || video !== cur) return;
        const ahead = clips[(index + 1) % clips.length];
        arm(nxt, ahead, false);
      }, { once: true });
      video.addEventListener("ended", () => {
        if (!alive || video !== cur) return;
        const nextIndex = (index + 1) % clips.length;
        const go = () => {
          if (!alive) return;
          cur.classList.remove("is-on");
          const old = cur;
          cur = nxt;
          nxt = old;
          index = nextIndex;
          reveal(cur);
          kick(cur);
          window.setTimeout(() => { if (alive) old.pause(); }, 900);
          bind(cur);
        };
        if (nxt.readyState >= 2) go();
        else nxt.addEventListener("loadeddata", go, { once: true });
      }, { once: true });
      video.addEventListener("error", () => {
        if (video === cur) failAll();
      }, { once: true });
    }

    arm(cur, clips[0], true);
    bind(cur);
    kick(cur);
  }

  resolveClips().then((clips) => {
    if (!clips.length) return;
    stages.forEach((stage) => mount(stage, clips));
  });
})();

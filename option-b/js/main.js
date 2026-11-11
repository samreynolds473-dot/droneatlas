(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  const header = $("#header");
  if (header) {
    const onScroll = () => header.classList.toggle("scrolled", scrollY > 30);
    addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  const mnav = $("#mnav");
  $("#burger")?.addEventListener("click", () => mnav?.classList.add("open"));
  $("#mclose")?.addEventListener("click", () => mnav?.classList.remove("open"));
  if (mnav) $$("a", mnav).forEach((a) => a.addEventListener("click", () => mnav.classList.remove("open")));

  const io = new IntersectionObserver((es) => es.forEach((e) => {
    if (!e.isIntersecting) return;
    e.target.classList.add("in", "in-view");
    io.unobserve(e.target);
  }), { threshold: 0.15, rootMargin: "0px 0px -6% 0px" });
  $$(".rv").forEach((el) => io.observe(el));

  $$(".qa button").forEach((b) => b.addEventListener("click", () => {
    const qa = b.parentElement;
    const open = qa.classList.toggle("open");
    b.setAttribute("aria-expanded", open);
  }));

  $$(".ba").forEach((ba) => {
    let drag = false;
    const set = (p) => {
      p = Math.max(2, Math.min(98, p));
      ba.style.setProperty("--pos", p + "%");
      ba.setAttribute("aria-valuenow", Math.round(p));
    };
    const fromEvt = (e) => {
      const r = ba.getBoundingClientRect();
      set(((e.clientX - r.left) / r.width) * 100);
    };
    ba.addEventListener("pointerdown", (e) => { drag = true; ba.setPointerCapture(e.pointerId); fromEvt(e); });
    ba.addEventListener("pointermove", (e) => { if (drag) fromEvt(e); });
    ba.addEventListener("pointerup", () => { drag = false; });
    ba.addEventListener("keydown", (e) => {
      const cur = parseFloat(getComputedStyle(ba).getPropertyValue("--pos")) || 50;
      if (e.key === "ArrowLeft") set(cur - 4);
      if (e.key === "ArrowRight") set(cur + 4);
    });
  });

  const yr = $("#yr") || $("[data-year]");
  if (yr) yr.textContent = String(new Date().getFullYear());

  // Contact form: if the action is still a placeholder, go to the thank-you page.
  const form = $("[data-contact-form], #leadForm");
  if (form) {
    form.addEventListener("submit", (e) => {
      const action = form.getAttribute("action") || "";
      if (action.includes("FORM_ACTION") || action.includes("{{")) {
        e.preventDefault();
        const thanks = form.getAttribute("data-thanks");
        if (thanks) location.href = thanks;
        else $("#formBox")?.classList.add("done");
      }
    });
  }

  // WhatsApp placeholder: don't navigate to an incomplete wa.me link
  $$("[data-whatsapp]").forEach((a) => {
    a.addEventListener("click", (e) => {
      const href = a.getAttribute("href") || "";
      if (href.includes("TO FILL") || href.includes("להשלמה") || href.includes("XXXXXXXXX")) {
        e.preventDefault();
      }
    });
  });
})();

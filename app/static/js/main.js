/* =========================================================
   Portfolio — main.js  (Black bg, interactive pop effects)
   ========================================================= */

gsap.registerPlugin(ScrollTrigger);

/* ---- Custom cursor ---- */
const cursorDot  = document.getElementById("cursor-dot");
const cursorRing = document.getElementById("cursor-ring");
let mouseX = 0, mouseY = 0;
let ringX  = 0, ringY  = 0;

window.addEventListener("mousemove", e => {
  mouseX = e.clientX;
  mouseY = e.clientY;
  gsap.set(cursorDot, { x: mouseX, y: mouseY });
});

(function animateRing() {
  ringX += (mouseX - ringX) * 0.5;
  ringY += (mouseY - ringY) * 0.5;
  gsap.set(cursorRing, { x: ringX, y: ringY });
  requestAnimationFrame(animateRing);
})();

document.querySelectorAll("a, button, .mag-btn, .tilt-card").forEach(el => {
  el.addEventListener("mouseenter", () => document.body.classList.add("cursor-hover"));
  el.addEventListener("mouseleave", () => document.body.classList.remove("cursor-hover"));
});

/* ---- Nav logo entrance + pulse ---- */
gsap.from(".nav-logo", { opacity: 0, x: -30, duration: 0.8, delay: 0.2, ease: "back.out(2)" });
gsap.to(".nav-logo", {
  textShadow: "0 0 20px #06b6d4, 0 0 40px #06b6d4",
  duration: 1.4, repeat: -1, yoyo: true, ease: "sine.inOut", delay: 1,
});

/* ---- Navbar scroll ---- */
window.addEventListener("scroll", () => {
  document.getElementById("navbar").classList.toggle("scrolled", window.scrollY > 50);
});

/* ---- Split hero name into chars and animate ---- */
const heroNameEl = document.getElementById("hero-name");
const nameText   = heroNameEl.textContent.trim();
heroNameEl.innerHTML = nameText.split("").map(ch =>
  ch === " " ? '<span class="char">&nbsp;</span>' : `<span class="char">${ch}</span>`
).join("");

/* ---- Hero entrance timeline ---- */
const heroTl = gsap.timeline({ defaults: { ease: "back.out(1.7)" } });
heroTl
  .to("#hero-greeting", { opacity: 1, y: 0, duration: 0.7, delay: 0.2, ease: "power3.out" })
  .to("#hero-name",     { opacity: 1, duration: 0 })
  .to("#hero-name .char", {
      opacity: 1, y: 0, rotate: 0,
      scale: 1,
      duration: 0.7, stagger: 0.06, ease: "back.out(3)",
    }, "-=0.1")
  .to("#hero-title",   { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, "-=0.2")
  .to("#hero-tagline", { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, "-=0.4")
  .to("#hero-buttons", { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, "-=0.3");

/* ---- Continuous wave on hero name letters after entrance ---- */
heroTl.call(() => {
  gsap.utils.toArray("#hero-name .char").forEach((ch, i) => {
    gsap.to(ch, {
      y: -10,
      duration: 0.6,
      ease: "sine.inOut",
      repeat: -1,
      yoyo: true,
      delay: i * 0.08,
    });
    // Subtle color flash cycle per letter
    gsap.to(ch, {
      color: "#06b6d4",
      duration: 1.5,
      ease: "sine.inOut",
      repeat: -1,
      yoyo: true,
      delay: i * 0.15,
    });
  });
});

/* ---- Magnetic buttons ---- */
document.querySelectorAll(".mag-btn").forEach(btn => {
  btn.addEventListener("mousemove", e => {
    const rect = btn.getBoundingClientRect();
    const dx = e.clientX - (rect.left + rect.width  / 2);
    const dy = e.clientY - (rect.top  + rect.height / 2);
    gsap.to(btn, { x: dx * 0.35, y: dy * 0.35, duration: 0.3, ease: "power2.out" });
  });
  btn.addEventListener("mouseleave", () => {
    gsap.to(btn, { x: 0, y: 0, duration: 0.5, ease: "elastic.out(1, 0.4)" });
  });
});

/* ---- Hero image fade on scroll ---- */
gsap.to("#hero-bg", {
  opacity: 0,
  ease: "none",
  scrollTrigger: {
    trigger: "#hero",
    start: "top top",
    end: "bottom top",
    scrub: true,
  },
});

/* ---- About section ---- */
gsap.to(".about-text", {
  opacity: 1, y: 0, duration: 0.9, ease: "power3.out",
  scrollTrigger: { trigger: "#about", start: "top 75%" },
});
gsap.to(".about-card", {
  opacity: 1, y: 0, duration: 0.9, ease: "back.out(1.4)", delay: 0.2,
  scrollTrigger: { trigger: "#about", start: "top 75%" },
});

/* ---- About card inner pop on scroll ---- */
gsap.from(".about-card-inner", {
  scale: 0.85, duration: 0.9, ease: "back.out(1.7)",
  scrollTrigger: { trigger: "#about", start: "top 70%" },
});

/* ---- Skill bars + counter ---- */
gsap.utils.toArray(".skill-bar-wrap").forEach((wrap, i) => {
  const bar = wrap.querySelector(".skill-bar");
  const pct = wrap.querySelector(".skill-pct");
  const target = parseInt(bar.dataset.width);

  gsap.to(wrap, {
    opacity: 1, y: 0, duration: 0.6, ease: "power3.out",
    delay: i * 0.09,
    scrollTrigger: { trigger: "#skills", start: "top 72%" },
  });

  ScrollTrigger.create({
    trigger: "#skills",
    start: "top 72%",
    once: true,
    onEnter: () => {
      gsap.to(bar, { width: target + "%", duration: 1.3, delay: i * 0.09 + 0.2, ease: "power2.out" });
      // counter
      const obj = { val: 0 };
      gsap.to(obj, {
        val: target, duration: 1.3, delay: i * 0.09 + 0.2, ease: "power2.out",
        onUpdate: () => { pct.textContent = Math.round(obj.val) + "%"; },
      });
    },
  });
});

/* ---- Project cards — staggered pop ---- */
gsap.utils.toArray(".project-card").forEach((card, i) => {
  gsap.to(card, {
    opacity: 1, y: 0, duration: 0.7, ease: "back.out(1.4)",
    delay: i * 0.15,
    scrollTrigger: { trigger: "#projects", start: "top 72%" },
  });
});

/* ---- Card tilt on mouse move ---- */
document.querySelectorAll(".tilt-card").forEach(card => {
  card.addEventListener("mousemove", e => {
    const rect = card.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width  - 0.5;
    const y = (e.clientY - rect.top)  / rect.height - 0.5;
    gsap.to(card, {
      rotateY: x * 12, rotateX: -y * 12,
      duration: 0.4, ease: "power2.out",
    });
  });
  card.addEventListener("mouseleave", () => {
    gsap.to(card, { rotateY: 0, rotateX: 0, duration: 0.6, ease: "elastic.out(1, 0.5)" });
  });
});

/* ---- Contact cards staggered pop ---- */
gsap.utils.toArray(".contact-card").forEach((card, i) => {
  gsap.from(card, {
    opacity: 0, y: 40, scale: 0.9, duration: 0.6, ease: "back.out(1.7)",
    delay: i * 0.1,
    scrollTrigger: { trigger: "#contact", start: "top 75%" },
  });
});

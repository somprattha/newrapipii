
document.addEventListener("DOMContentLoaded", function () {
  function createHeart() {
    const heart = document.createElement("div");
    heart.textContent = "💖";
    heart.style.position = "fixed";
    heart.style.left = Math.random() * window.innerWidth + "px";
    heart.style.bottom = "0px";
    heart.style.fontSize = Math.random() * 20 + 20 + "px";
    heart.style.opacity = 0.8;
    heart.style.animation = "floatUp 4s ease-out forwards";
    heart.style.zIndex = 9999;
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 4000);
  }
  setInterval(createHeart, 500);

  const style = document.createElement("style");
  style.textContent = `@keyframes floatUp { 0% { transform: translateY(0); opacity: 1; } 100% { transform: translateY(-100vh); opacity: 0; } }`;
  document.head.appendChild(style);
});

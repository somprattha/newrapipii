
document.addEventListener("DOMContentLoaded", function () {
  function createBat() {
    const bat = document.createElement("div");
    bat.textContent = "🦇";
    bat.style.position = "fixed";
    bat.style.top = Math.random() * window.innerHeight + "px";
    bat.style.left = "-50px";
    bat.style.fontSize = "25px";
    bat.style.animation = "flyBat 6s linear forwards";
    bat.style.zIndex = 9999;
    document.body.appendChild(bat);
    setTimeout(() => bat.remove(), 6000);
  }
  setInterval(createBat, 800);

  const style = document.createElement("style");
  style.textContent = `@keyframes flyBat { 0% { transform: translateX(0); } 100% { transform: translateX(110vw); } }`;
  document.head.appendChild(style);
});

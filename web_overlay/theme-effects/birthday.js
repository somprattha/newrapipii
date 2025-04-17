
document.addEventListener("DOMContentLoaded", function () {
  function createBalloon() {
    const balloon = document.createElement("div");
    balloon.textContent = "🎈";
    balloon.style.position = "fixed";
    balloon.style.left = Math.random() * window.innerWidth + "px";
    balloon.style.bottom = "-30px";
    balloon.style.fontSize = "30px";
    balloon.style.animation = "rise 6s linear forwards";
    balloon.style.zIndex = 9999;
    document.body.appendChild(balloon);
    setTimeout(() => balloon.remove(), 6000);
  }
  setInterval(createBalloon, 600);

  const style = document.createElement("style");
  style.textContent = `@keyframes rise { from { transform: translateY(0); } to { transform: translateY(-100vh); } }`;
  document.head.appendChild(style);
});

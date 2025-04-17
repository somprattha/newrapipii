
document.addEventListener("DOMContentLoaded", function () {
  const snowContainer = document.createElement("div");
  snowContainer.style.position = "fixed";
  snowContainer.style.top = "0";
  snowContainer.style.left = "0";
  snowContainer.style.width = "100%";
  snowContainer.style.height = "100%";
  snowContainer.style.pointerEvents = "none";
  snowContainer.style.zIndex = "9999";
  document.body.appendChild(snowContainer);

  function createSnowflake() {
    const snowflake = document.createElement("div");
    snowflake.textContent = "❄️";
    snowflake.style.position = "absolute";
    snowflake.style.left = Math.random() * window.innerWidth + "px";
    snowflake.style.top = "-40px";
    snowflake.style.fontSize = Math.random() * 20 + 10 + "px";
    snowflake.style.opacity = Math.random();
    snowflake.style.animation = "fall 5s linear infinite";
    snowContainer.appendChild(snowflake);
    setTimeout(() => snowflake.remove(), 5000);
  }
  setInterval(createSnowflake, 300);

  const style = document.createElement("style");
  style.textContent = `@keyframes fall { 0% { transform: translateY(0); } 100% { transform: translateY(100vh); } }`;
  document.head.appendChild(style);
});

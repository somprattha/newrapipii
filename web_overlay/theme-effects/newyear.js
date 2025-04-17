
document.addEventListener("DOMContentLoaded", function () {
  function createFirework() {
    const spark = document.createElement("div");
    spark.textContent = "🎆";
    spark.style.position = "fixed";
    spark.style.left = Math.random() * window.innerWidth + "px";
    spark.style.top = Math.random() * window.innerHeight + "px";
    spark.style.fontSize = "25px";
    spark.style.opacity = 1;
    spark.style.zIndex = 9999;
    document.body.appendChild(spark);
    setTimeout(() => spark.remove(), 1500);
  }
  setInterval(createFirework, 700);
});

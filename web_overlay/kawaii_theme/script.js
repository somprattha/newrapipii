
setInterval(() => {
  const messageBox = document.getElementById("message");
  const messages = [
    "✨ ราพีพี้อยู่ตรงนี้เสมอน้า~",
    "🎀 ขอบคุณที่มาดูไลฟ์วันนี้นะคะ",
    "💬 พิมพ์แชทมาได้เลย ราพีพี้ฟังอยู่~",
    "🌸 ทักได้เลยน้า อย่าเขิน~"
  ];
  const msg = messages[Math.floor(Math.random() * messages.length)];
  messageBox.textContent = msg;
}, 6000);

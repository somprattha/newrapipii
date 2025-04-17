
const chatbox = document.getElementById("chatbox");
const emotionBox = document.getElementById("emotionBox");

const emotions = [
  { emoji: "😄", color: "#ffe1ec" },
  { emoji: "😭", color: "#d0e7ff" },
  { emoji: "😡", color: "#ffe1e1" },
  { emoji: "😳", color: "#fff0f5" },
  { emoji: "😍", color: "#fff9e6" },
];

function addMessage(name, message) {
  const div = document.createElement("div");
  div.className = "chat-message";
  div.innerHTML = `<strong>${name}:</strong> ${message}`;
  chatbox.appendChild(div);
  if (chatbox.children.length > 5) chatbox.removeChild(chatbox.firstChild);
  chatbox.scrollTop = chatbox.scrollHeight;
}

// Random emotion change every 10s
setInterval(() => {
  const rand = emotions[Math.floor(Math.random() * emotions.length)];
  emotionBox.innerText = rand.emoji;
  document.body.style.background = `linear-gradient(135deg, ${rand.color} 0%, #fff)`;
}, 10000);

// Simulate chat (replace with WebSocket later)
setInterval(() => {
  const names = ["แฟนคลับ A", "แฟนคลับ B", "You", "Raphee"];
  const msgs = ["สวัสดีค่าาา~", "น่ารักที่สุดเลย", "วันนี้สนุกไหม?", "เย้ๆๆๆ"];
  addMessage(names[Math.floor(Math.random() * names.length)], msgs[Math.floor(Math.random() * msgs.length)]);
}, 7000);

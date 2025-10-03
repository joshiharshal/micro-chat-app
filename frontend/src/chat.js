let ws;
const username = localStorage.getItem("username");

function connectChat() {
  ws = new WebSocket("ws://localhost:8080/api/chat/ws"); // via gateway

  ws.onmessage = (event) => {
    const msgBox = document.getElementById("messages");
    const msg = document.createElement("div");
    msg.textContent = event.data;
    msgBox.appendChild(msg);
  };
}

function sendMessage() {
  const input = document.getElementById("msg");
  ws.send(JSON.stringify({ user: username, text: input.value }));
  input.value = "";
}

window.onload = connectChat;

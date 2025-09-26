const ws = new WebSocket("ws://localhost:8003/ws");

ws.onmessage = (event) => {
    const chat = document.getElementById("chat");
    chat.innerHTML += `<div>${event.data}</div>`;
};

function sendMessage() {
    const msgInput = document.getElementById("msg");
    ws.send(msgInput.value);
    msgInput.value = "";
}

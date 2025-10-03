async function login() {
  const username = document.getElementById("username").value;

  const res = await fetch("/api/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username })
  });

  if (res.ok) {
    localStorage.setItem("username", username);
    window.location.href = "chat.html"; // go to chat page
  } else {
    alert("Login failed");
  }
}

async function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const res = await fetch("/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });

  if (res.ok) {
    localStorage.setItem("username", username);
    window.location.href = "chat.html"; // go to chat page
  } else {
    const error = await res.json();
    alert("Login failed: " + JSON.stringify(error));
  }
}

async function loadProfile() {
  const res = await fetch("/api/user/profile", {
    headers: { "Authorization": "Bearer " + localStorage.getItem("username") }
  });

  if (res.ok) {
    const profile = await res.json();
    document.getElementById("profile").innerHTML = `
      <p><b>Username:</b> ${profile.username}</p>
      <p><b>Email:</b> ${profile.email || "N/A"}</p>
    `;
  } else {
    document.getElementById("profile").innerHTML = "Failed to load profile.";
  }
}

window.onload = loadProfile;

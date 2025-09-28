# Microservices Chat App

A simple real-time chat application built with **Python (FastAPI)** microservices, **WebSocket**, and **Docker Compose**. Each service is isolated and communicates via a **gateway** using **NGINX**.

---

## 🏗 Project Structure

.
├── analytics-service
├── auth-service
├── chat-service
├── frontend
├── gateway
├── group-service
├── media-service
├── message-history-service
├── notification-service
├── user-service
├── docker-compose.yaml
└── README.md


- **frontend** – HTML/CSS/JS for the chat UI.
- **gateway** – NGINX reverse proxy routing requests to services.
- **auth-service** – Handles authentication (optional/simple user tracking).
- **user-service** – User management (register/login).
- **chat-service** – Real-time chat using WebSocket.
- **message-history-service** – Stores chat history.
- **group-service** – Manage chat groups.
- **media-service** – Media uploads (images, files).
- **notification-service** – Notifications (optional).
- **analytics-service** – Chat usage stats.

---

## ⚙️ Prerequisites

- Docker & Docker Compose installed
- Node.js (optional for frontend dev)
- Python 3.12+ (for service development)

---

## 🐳 Running the App

1. **Clone the repository**

```bash
git clone <repo-url>
cd micro-chat-app
---
## 
2. **Build and start all services**
docker-compose up --build

docker ps


You should see containers like:

micro-chat-app-frontend-1

micro-chat-app-chat-service-1

micro-chat-app-auth-service-1

etc.

🌐 Accessing the App

Frontend: http://localhost:8090/

Health check URLs (via NGINX gateway)
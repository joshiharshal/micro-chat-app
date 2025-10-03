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



docker compose exec gateway sh
# Auth service
curl http://auth-service:8000/health

# User service
curl http://user-service:8000/

# Chat service
curl http://chat-service:8000/

# Message history service
curl http://message-history-service:8000/messages

# Group service
curl http://group-service:8000/groups

# Notification service
curl http://notification-service:8000/health
curl -X POST http://notification-service:8000/notify \
     -H "Content-Type: application/json" \
     -d '{"message":"Hello from gateway container"}'

# Media service (if implemented)
curl http://media-service:8000/

# Analytics service
curl http://analytics-service:8000/metrics
    
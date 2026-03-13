![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-blue)
![Clerk](https://img.shields.io/badge/Auth-Clerk-purple)
![License](https://img.shields.io/badge/license-MIT-green)

# TaskBoard --- B2B SaaS Task Management Platform

A **full‑stack B2B SaaS application** that allows organizations to
manage team tasks using a Kanban board system with **multi‑tenant
architecture**, **role‑based access control**, and **subscription‑based
feature limits**.

This project demonstrates production‑style SaaS architecture using
**FastAPI**, **React**, **Clerk authentication**, and **webhook
automation**.

------------------------------------------------------------------------

## 🚀 Live Demo

Frontend: (add your deployed frontend URL)\
API Docs: (add your deployed backend URL)/docs

------------------------------------------------------------------------

## 🧠 Problem Solved

Many teams need a lightweight task management system that supports:

-   Multiple organizations
-   Team collaboration
-   Role‑based permissions
-   Scalable SaaS billing architecture

This project implements those concepts in a modern **SaaS‑style backend
architecture**.

------------------------------------------------------------------------

## ✨ Features

### Multi‑Tenant Architecture

-   Each organization has isolated tasks and members
-   Secure organization‑based access control

### Authentication & Authorization

-   Clerk authentication
-   Protected API routes
-   Organization membership roles

### Task Management

-   Kanban board interface
-   Create / update / delete tasks
-   Status workflow (Pending → Started → Completed)

### Team Collaboration

-   Invite members to organizations
-   Role‑based permissions (Admin / Editor / Member)

### SaaS Subscription Logic

-   Free tier membership limits
-   Pro tier unlimited members
-   Billing event automation

### Webhook Automation

-   Clerk webhook integration
-   Subscription updates automatically change organization limits

------------------------------------------------------------------------

## 🏗 Architecture

The application follows a **layered backend architecture**:

    Backend (FastAPI)
    │
    ├── API Layer
    │   Handles HTTP endpoints and request validation
    │
    ├── Core Layer
    │   Authentication, configuration, database setup
    │
    ├── Models
    │   SQLAlchemy database models
    │
    ├── Schemas
    │   Pydantic request/response validation
    │
    └── Services / Logic
        Business logic for tasks and organization limits

------------------------------------------------------------------------

## 🧩 Tech Stack

### Backend

-   FastAPI
-   SQLAlchemy
-   Pydantic
-   Clerk Python SDK
-   Svix Webhooks

### Frontend

-   React
-   Vite
-   Clerk React SDK

### Infrastructure

-   Clerk Authentication
-   Webhooks
-   SQLite (development)
-   PostgreSQL ready (production)

------------------------------------------------------------------------

## 📂 Project Structure

    taskboard-saas
    │
    ├── backend
    │   ├── app
    │   │   ├── api
    │   │   ├── core
    │   │   ├── models
    │   │   ├── schemas
    │   │   └── main.py
    │   │
    │   ├── requirements.txt
    │   └── start.py
    │
    ├── frontend
    │   ├── src
    │   ├── package.json
    │   └── vite.config.js
    │
    └── README.md

------------------------------------------------------------------------

## ⚙️ Running Locally

### 1️⃣ Clone Repository

    git clone https://github.com/YOUR_USERNAME/taskboard-saas.git
    cd taskboard-saas

------------------------------------------------------------------------

### 2️⃣ Start Backend

    cd backend
    pip install -r requirements.txt
    uvicorn app.main:app --reload

Backend runs at:

    http://localhost:8000

API docs:

    http://localhost:8000/docs

------------------------------------------------------------------------

### 3️⃣ Start Frontend

    cd frontend
    npm install
    npm run dev

Frontend runs at:

    http://localhost:5173

------------------------------------------------------------------------

## 🔐 Environment Variables

Example backend `.env`:

    CLERK_SECRET_KEY=
    CLERK_PUBLISHABLE_KEY=
    CLERK_JWKS_URL=
    CLERK_WEBHOOK_SECRET=

    DATABASE_URL=sqlite:///./taskboard.db

    FRONTEND_URL=http://localhost:5173

------------------------------------------------------------------------

## 🔗 Webhook Integration

Clerk sends subscription events to:

    /api/webhooks/clerk

These events automatically:

-   Detect subscription changes
-   Update organization member limits
-   Enable Pro tier functionality

------------------------------------------------------------------------

## 🧪 Example API Endpoints

### Get Tasks

    GET /api/tasks

### Create Task

    POST /api/tasks

### Update Task

    PATCH /api/tasks/{task_id}

### Delete Task

    DELETE /api/tasks/{task_id}

------------------------------------------------------------------------

## 📊 SaaS Concepts Demonstrated

This project showcases several important SaaS engineering concepts:

-   Multi‑tenant architecture
-   Role‑based access control
-   Subscription‑based feature gating
-   Webhook‑driven automation
-   Backend API design with FastAPI
-   Modern authentication integration

------------------------------------------------------------------------

## 📸 Screenshots

(Add screenshots here once deployed)

Suggested screenshots:

-   Dashboard
-   Kanban board
-   Organization members
-   Subscription upgrade flow

------------------------------------------------------------------------

## 🧑‍💻 Author

Built as a portfolio project demonstrating **modern SaaS backend
architecture**.

If you found this project interesting, feel free to connect.

------------------------------------------------------------------------

## 📜 License

MIT License

# TaskBoard --- B2B SaaS Task Management Platform

![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-blue)
![Clerk](https://img.shields.io/badge/Auth-Clerk-purple)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-success)
![License](https://img.shields.io/badge/license-MIT-green) ![Backend
Tests](https://github.com/ricothenfx/b2b-saas-taskboard/actions/workflows/backend-tests.yml/badge.svg)

A **full-stack B2B SaaS task management platform** built with modern
backend architecture.

The application allows organizations to manage team tasks using a
**Kanban board system** with **multi-tenant architecture**, **role-based
access control**, and **subscription-based feature limits**.

This project demonstrates production-style SaaS architecture using:

-   FastAPI backend
-   React frontend
-   Clerk authentication
-   PostgreSQL (Neon serverless database)
-   Webhook automation
-   Automated CI testing

------------------------------------------------------------------------

## 🚀 Live Demo

Frontend:  
🔗 https://b2b-saas-taskboard.vercel.app/

API Docs (Swagger UI):  
🔗 https://b2b-saas-taskboard.onrender.com/docs

------------------------------------------------------------------------

## 🧠 Problem Solved

Many teams need a lightweight task management system that supports:

-   Multiple organizations
-   Team collaboration
-   Role-based permissions
-   SaaS-style subscription limits
-   Scalable backend architecture

This project implements those concepts using a **modern SaaS backend
design**.

------------------------------------------------------------------------

## ✨ Features

### Multi-Tenant Architecture

-   Each organization has isolated tasks and members
-   Secure organization-based access control

### Authentication & Authorization

-   Clerk authentication
-   Protected API routes
-   Organization membership roles

### Task Management

-   Kanban board interface
-   Create / update / delete tasks
-   Task workflow:

**Pending → Started → Completed**

### Team Collaboration

-   Invite members to organizations
-   Role-based permissions (Admin / Editor / Member)

### SaaS Subscription Logic

-   Free tier member limits
-   Pro tier unlimited members
-   Billing event automation

### Webhook Automation

-   Clerk webhook integration
-   Subscription events automatically update organization limits

------------------------------------------------------------------------

## 🏗 Architecture

    Backend (FastAPI)

    API Layer
    │
    ├── Handles HTTP endpoints
    ├── Request validation
    │
    Core Layer
    │
    ├── Authentication
    ├── Configuration
    ├── Database connection
    │
    Models
    │
    ├── SQLAlchemy database models
    │
    Schemas
    │
    ├── Pydantic request/response models
    │
    Services / Business Logic
    │
    └── Task management & SaaS rules

------------------------------------------------------------------------

## 🧩 Tech Stack

### Backend

-   FastAPI
-   SQLAlchemy
-   Pydantic
-   Clerk Python SDK
-   Svix Webhooks
-   pytest (unit testing)

### Frontend

-   React
-   Vite
-   Clerk React SDK

### Infrastructure

-   PostgreSQL (Neon serverless database)
-   SQLite (local development)
-   GitHub Actions (CI pipeline)
-   uv (fast Python package manager)

------------------------------------------------------------------------

## 🧪 Automated Testing

The backend includes **unit tests with pytest**.

Tests automatically run in **GitHub Actions CI** on every push.

Current test coverage:

    ~74%

Run tests locally:

    cd backend
    uv run pytest --cov=app

------------------------------------------------------------------------

## 📂 Project Structure

    b2b-saas-taskboard
    │
    ├── backend
    │   ├── app
    │   │   ├── api
    │   │   ├── core
    │   │   ├── models
    │   │   ├── schemas
    │   │   └── main.py
    │   │
    │   ├── tests
    │   │   ├── test_tasks.py
    │   │   ├── test_auth.py
    │   │   ├── test_webhooks.py
    │   │   └── test_database.py
    │   │
    │   ├── pyproject.toml
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

### Clone Repository

    git clone https://github.com/ricothenfx/b2b-saas-taskboard.git
    cd b2b-saas-taskboard

------------------------------------------------------------------------

### Start Backend

Install dependencies:

    cd backend
    uv sync

Run server:

    uv run start.py

Or:

    uv run uvicorn app.main:app --reload

Backend:

    http://localhost:8000

API docs:

    http://localhost:8000/docs

------------------------------------------------------------------------

### Start Frontend

    cd frontend
    npm install
    npm run dev

Frontend:

    http://localhost:5173

------------------------------------------------------------------------

## 🔐 Environment Variables

Example `.env`:

    CLERK_SECRET_KEY=
    CLERK_PUBLISHABLE_KEY=
    CLERK_JWKS_URL=
    CLERK_WEBHOOK_SECRET=

    DATABASE_URL=postgresql://user:password@host/db

    FRONTEND_URL=http://localhost:5173

For local development:

    DATABASE_URL=sqlite:///./taskboard.db

------------------------------------------------------------------------

## 🔗 Webhook Integration

Clerk sends subscription events to:

    /api/webhooks/clerk

These events automatically:

-   detect subscription changes
-   update organization member limits
-   enable Pro tier functionality

------------------------------------------------------------------------

## 📊 SaaS Concepts Demonstrated

-   Multi-tenant architecture
-   Role-based access control
-   Subscription-based feature gating
-   Webhook-driven automation
-   Backend API design with FastAPI
-   CI/CD automated testing

------------------------------------------------------------------------

## 🧑‍💻 Author

Built as a portfolio project demonstrating **modern SaaS backend
architecture**.

------------------------------------------------------------------------

## 📜 License

MIT License

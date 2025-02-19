# 🚀 FastAPI Boilerplate with JWT Authentication & SQLModel

A **scalable and modular** FastAPI boilerplate with **JWT authentication**, **user management**, and a clean project structure for large-scale applications. Built with **FastAPI** and **SQLModel**, this template provides a good enough foundation for backend development.

## 🔥 Features
- ✅ **FastAPI + SQLModel** for modern, async-ready backend development
- 🔐 **JWT-based authentication** (register, login, token validation)
- 👥 **User management** (CRUD operations)
- 🗄️ **Database integration** with SQLModel & SQLite (easily switch to PostgreSQL/MySQL)
- 🔒 **Secure password hashing** with Passlib (bcrypt)
- ⚡ **Event-based startup/shutdown lifecycle** with FastAPI `lifespan`
- 📂 **Modular and scalable project structure**
- 🌍 **API versioning (`/api/v1/`)** for long-term maintainability

## 📂 Project Structure

project/

├── app/

│   ├── core/               # Configuration & security utilities

│   ├── db/                 # Database session & the database itself

│   ├── models/             # SQLModel database models

│   ├── schemas/            # Pydantic schemas for data validation

│   ├── api/                # API routes (auth, users, etc.)

│   │   ├── v1/             # API version 1

│   │       ├── endpoints/  # Authentication and user management endpoints

│   ├── utils/              # Helper functions (JWT, etc.)

│   ├── main.py             # FastAPI application entry point

└── requirements.txt        # Dependencies

## 🚀 Quick Start

### I°) Clone the repository

```bash
   git clone https://github.com/your-username/fastapi-boilerplate.git
   cd FastAPI-SQLModel-Boilerplate
```

### II°) Install dependencies

```bash
   pip install -r requirements.txt
```

### III°) Run the server

```bash
   uvicorn app.main:app --reload
```

## 🎯 Future Enhancements

✅ Role-based access control (RBAC)
✅ Refresh tokens support
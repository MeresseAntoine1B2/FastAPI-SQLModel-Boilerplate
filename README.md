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

project/<br>
├── app/<br>
│   ├── core/               # Configuration & security utilities<br>
│   ├── db/                 # Database session & the database itself<br>
│   ├── models/             # SQLModel database models<br>
│   ├── schemas/            # Pydantic schemas for data validation<br>
│   ├── api/                # API routes (auth, users, etc.)<br>
│   │   ├── v1/             # API version 1<br>
│   │       ├── endpoints/  # Authentication and user management endpoints<br>
│   ├── utils/              # Helper functions (JWT, etc.)<br>
│   ├── main.py             # FastAPI application entry point<br>
└── requirements.txt        # Dependencies<br>

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
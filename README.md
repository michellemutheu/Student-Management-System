# Student Management System

![Python](https://img.shields.io/badge/Python-3.12-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-green) ![SQLite](https://img.shields.io/badge/Database-SQLite-orange) ![Auth](https://img.shields.io/badge/Auth-JWT-red)

## Overview

A REST API for managing student records, built with FastAPI and SQLAlchemy. Features full CRUD operations for students, user authentication with JWT tokens, and a SQLite database backend.

---

## Features

- Add, view, update, and delete student records
- User registration and login with hashed passwords (bcrypt)
- JWT token-based authentication (OAuth2)
- SQLite database with SQLAlchemy ORM
- Pydantic schemas for request/response validation

---

## Tech Stack

| Layer | Technology |
|---|---|
| API Framework | FastAPI |
| Database ORM | SQLAlchemy |
| Database | SQLite |
| Auth | JWT (jose) + bcrypt (passlib) |
| Validation | Pydantic (BaseModel) |
| Language | Python 3.12 |

---

## Project Structure

```
student_management_system/
├── main.py        # FastAPI app, routes, JWT auth logic
├── models.py      # SQLAlchemy models (Student, User)
├── schemas.py     # Pydantic schemas (StudentCreate, StudentResponse, Token)
├── database.py    # Database engine, session, Base
└── student_management.db  # SQLite database (auto-created)
```

---

## Data Models

**Student**
- `id` — primary key
- `name` — string, required
- `email` — unique, required
- `course` — string, required
- `grade` — float, optional

**User**
- `id` — primary key
- `email` — unique
- `hashed_password` — bcrypt hashed

---

## Getting Started

### Install dependencies

```bash
pip install fastapi sqlalchemy passlib[bcrypt] python-jose uvicorn
```

### Run the API

```bash
uvicorn main:app --reload
```

### View interactive docs

Open your browser at:
```
http://127.0.0.1:8000/docs
```

---

## Status

In progress — core student CRUD and authentication implemented.

---

*Built with Python 3.12 · michellemutheu*

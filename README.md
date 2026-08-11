# Student Management API

A RESTful Student Management API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT authentication**.

This project provides secure CRUD operations for managing student records and includes user authentication with password hashing and JWT-based authorization.

## Features

- User signup and login
- Secure password hashing with bcrypt
- JWT-based authentication
- Protected API endpoints
- Create, read, update, and delete students
- PostgreSQL database integration
- SQLAlchemy ORM
- Automatic API documentation with Swagger UI
- Environment variable configuration
- Input validation using Pydantic

## Tech Stack

- **Python**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Pydantic**
- **JWT**
- **Passlib / bcrypt**
- **Uvicorn**
- **python-dotenv**

## Project Structure

```text
student_management_api/
│
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

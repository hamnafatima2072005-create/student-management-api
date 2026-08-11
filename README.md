# Student Management API

A RESTful Student Management API built with FastAPI, PostgreSQL, SQLAlchemy, and JWT authentication.

## Features

- User signup and login
- Secure password hashing with bcrypt
- JWT-based authentication
- Protected student endpoints
- Create, read, update, and delete student records
- PostgreSQL database integration
- SQLAlchemy ORM
- Pydantic data validation
- Swagger UI for API testing
- Environment variable configuration

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT
- Passlib
- bcrypt
- Uvicorn
- python-dotenv

## Project Structure

```text
student-management-api/
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
Authentication

The API uses JWT (JSON Web Tokens) for authentication and authorization.

The authentication flow is:

User Signup
     ↓
Password Hashing
     ↓
User Login
     ↓
Credentials Verification
     ↓
JWT Access Token
     ↓
Protected API Endpoints

Student management endpoints require a valid JWT Bearer token.

API Endpoints
Authentication
Method	Endpoint	Description
POST	/auth/signup	Register a new user
POST	/auth/login	Login and receive an access token
GET	/profile	Get the authenticated user's profile
Students
Method	Endpoint	Description
POST	/students	Create a student
GET	/students	Get all students
GET	/students/{student_id}	Get a student by ID
PUT	/students/{student_id}	Update a student
DELETE	/students/{student_id}	Delete a student

All student endpoints are protected and require authentication.

Database

PostgreSQL is used as the database and SQLAlchemy is used as the ORM.

Database configuration is stored in environment variables.

Example:

DATABASE_URL=postgresql://username:password@localhost:5432/student_db
JWT_SECRET_KEY=your_secret_key_here
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

Do not add real database credentials or JWT secrets to the repository.

Installation
1. Clone the repository
git clone https://github.com/hamnafatima2072005-create/student-management-api.git
cd student-management-api
2. Create a virtual environment
python -m venv venv
3. Activate the virtual environment

On Windows:

venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Configure environment variables

Create a .env file in the project root using .env.example as a reference.

Add your own PostgreSQL connection details and JWT secret.

6. Run the API
uvicorn app.main:app --reload
API Documentation

After starting the server, open:

http://127.0.0.1:8000/docs

Swagger UI can be used to test the API endpoints and authentication.

Example Student
{
  "name": "Marium",
  "age": 21,
  "city": "Mianwali"
}
Security
Passwords are stored using bcrypt hashing.
JWT is used to protect authenticated endpoints.
Sensitive configuration is stored in environment variables.
.env is excluded from Git using .gitignore.
The virtual environment is excluded from Git.
Learning Outcomes

This project demonstrates practical experience with:

REST API development
FastAPI
PostgreSQL
SQLAlchemy ORM
JWT authentication
Password hashing
CRUD operations
API testing with Swagger UI
Environment variables
Git and GitHub
License

This project is for educational and portfolio purposes.

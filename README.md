FastAPI Auth API

A small authentication API I built using FastAPI and PostgreSQL.

It has user registration, password hashing, JWT login, protected routes, and user deletion.

API Docs: https://git-project-fast-api-app--halaleloevershi.replit.app/api/docs

Features

- Register users
- Store users in PostgreSQL
- Hash passwords with bcrypt
- Login with JWT
- Protected routes
- Get users
- Get user by ID
- Delete users

Tech

- Python
- FastAPI
- PostgreSQL
- JWT
- Passlib / bcrypt
- Uvicorn
- Replit

Run locally

pip install -r requirements.txt
uvicorn main:app --reload
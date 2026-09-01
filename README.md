# FastAPI Auth API

A production-ready authentication API built with FastAPI and PostgreSQL. Live and deployed.

**Live API:** https://git-project-fast-api-app--halaleloevershi.replit.app
**Interactive Docs:**
https://git-project-fast-api-app--halaleloevershi.replit.app/api/docs


### Features
- Register users with validation
- PostgreSQL storage
- Bcrypt password hashing
- JWT login & authentication
- Protected routes
- Get all users / Get user by ID / Delete user

### Tech Stack
- Python, FastAPI, Uvicorn
- PostgreSQL, SQLAlchemy
- JWT, Passlib [bcrypt]
- Deployed on Replit

### Endpoints
- `POST /register` - Create account
- `POST /login` - Get access token
- `GET /users` - Protected
- `GET /user/{id}` - Protected
- `DELETE /delete/{id}` - Protected

### Run Locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
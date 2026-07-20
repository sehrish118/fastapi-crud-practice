# 📒 Contact Book API

A RESTful API built with **FastAPI** and **SQLite** for securely managing contacts, with JWT-based user authentication and protected CRUD operations.

## 🚀 Features

- JWT authentication (register/login)
- Password hashing with Passlib (bcrypt)
- Protected endpoints via Bearer Token
- Full CRUD for contacts — each user sees only their own
- Pydantic input validation
- Interactive docs via Swagger UI

## 📂 Project Structure

```
app/
├── routers/        # auth.py, contacts.py
├── schemas/        # user.py, contact.py
├── core/           # database.py
├── auth.py
├── dependencies.py
└── main.py
```

## 📌 API Endpoints

| Method | Endpoint          | Description             | Auth |
|--------|-------------------|--------------------------|------|
| POST   | `/auth/register`  | Register a new user     | ❌ |
| POST   | `/auth/login`      | Login, get JWT token    | ❌ |
| GET    | `/contacts`        | Get all contacts        | ✅ |
| GET    | `/contacts/{id}`   | Get a specific contact  | ✅ |
| POST   | `/contacts`        | Create a contact        | ✅ |
| PUT    | `/contacts/{id}`   | Update a contact        | ✅ |
| DELETE | `/contacts/{id}`   | Delete a contact        | ✅ |

## ⚙️ Setup

```bash
git clone https://github.com/sehrish118/contact-book-api.git
cd contact-book-api

python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt
```

Create a `.env` file:

```
DATABASE_NAME=contacts.db
SECRET_KEY=your_super_secret_random_hex_string
```

Generate a secret key: `python -c "import secrets; print(secrets.token_hex(32))"`

## ▶️ Run

```bash
uvicorn app.main:app --reload
```

App runs at `http://127.0.0.1:8000` · Docs at `/docs` (Swagger) and `/redoc` (ReDoc)

## 🛠️ Tech Stack

FastAPI · SQLite · Pydantic · Passlib (bcrypt) · python-jose (JWT) · Uvicorn · python-dotenv

## 🔒 Using Protected Routes (Postman)

1. Register → Login → copy `access_token` from response
2. On any protected endpoint: **Authorization** tab → **Bearer Token** → paste token
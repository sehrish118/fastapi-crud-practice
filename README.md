# Contact Book API

A simple REST API built with **FastAPI** and **SQLite** for managing contacts — supports Create, Read, Update, and Delete operations.

## Features

- Full CRUD for contacts
- Data persists in a SQLite database
- Input validation (email format, field length checks)
- Duplicate email prevention
- Config via environment variables
- Auto-creates the database on first run

## Project Structure

```
contact-book-api/
├── app/
│   ├── main.py            # Entry point
│   ├── database.py        # DB connection & setup
│   ├── models.py           # Pydantic schemas
│   └── routers/
│       └── contacts.py     # API endpoints
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd contact-book-api

# 2. Create & activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add a .env file
echo DATABASE_NAME=contacts.db > .env
```

## Running the API

```bash
uvicorn app.main:app --reload
```

Runs at `http://127.0.0.1:8000`. Interactive docs available at **`/docs`**.

## Endpoints

- `GET /contacts` — get all contacts
- `GET /contacts/{id}` — get one contact
- `POST /contacts` — add a contact *(201)*
- `PUT /contacts/{id}` — update a contact
- `DELETE /contacts/{id}` — delete a contact

## Example: Add a Contact

```bash
POST http://127.0.0.1:8000/contacts
Content-Type: application/json

{
    "name": "Hassan Raza",
    "phone": "03331234567",
    "email": "hassan@gmail.com",
    "group": "friends"
}
```

## Tech Stack

FastAPI · SQLite · Pydantic · Uvicorn · python-dotenv

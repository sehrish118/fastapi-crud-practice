# 📒 Contact Book API

A RESTful API built with **FastAPI** and **SQLite** (using raw SQL queries) for managing contacts securely. The application supports user authentication with JWT tokens and provides protected CRUD operations for contact management.

---

## 🚀 Features

- 🔐 User registration and login with JWT authentication
- 🔑 Secure password hashing using **Passlib (bcrypt)**
- 🛡️ Protected API endpoints using Bearer Token authentication
- 📇 Complete CRUD operations for contacts
- 👤 Each user can access only their own contacts
- 💾 SQLite database with raw SQL queries
- ✅ Input validation using Pydantic
- 📖 Interactive API documentation with Swagger UI

---

## 📂 Project Structure

```text
CONTACT_BOOK_API/
│
├── app/
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── contacts.py
│   │
│   ├── __init__.py
│   ├── auth.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── security.py
│
├── venv/
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 📌 API Endpoints

### Authentication (Public)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and receive a JWT access token |

### Contacts (Protected)

> All contact endpoints require a valid **Bearer Token**.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/contacts` | Retrieve all contacts |
| GET | `/contacts/{id}` | Retrieve a specific contact |
| POST | `/contacts` | Create a new contact |
| PUT | `/contacts/{id}` | Update an existing contact |
| DELETE | `/contacts/{id}` | Delete a contact |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sehrish118/contact-book-api.git
cd contact-book-api
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root and add the following:

```env
DATABASE_NAME=contacts.db
SECRET_KEY=your_super_secret_random_hex_string
```

Generate a secure secret key using:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

---

## ▶️ Run the Application

Start the FastAPI server using:

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically generates interactive documentation.

- **Swagger UI**
  ```
  http://127.0.0.1:8000/docs
  ```

- **ReDoc**
  ```
  http://127.0.0.1:8000/redoc
  ```

---

## 🛠️ Tech Stack

- FastAPI
- SQLite
- Raw SQL (`sqlite3`)
- Pydantic
- Passlib (bcrypt)
- JWT Authentication (`python-jose`)
- Uvicorn
- Python Dotenv
- Postman(testing)

---

## 🔒 Authentication Flow (Postman)

1. **Register a new user**
   - Send a `POST` request to:
     ```
     /auth/register
     ```
   - Provide the required user details in the request body.

2. **Login**
   - Send a `POST` request to:
     ```
     /auth/login
     ```
   - Enter your registered credentials.
   - A JWT access token will be returned in the response.

3. **Copy the Access Token**
   - Copy the `access_token` from the login response.

4. **Authorize Requests in Postman**
   - Open any protected endpoint (e.g., `GET /contacts`).
   - Go to the **Authorization** tab.
   - Select **Bearer Token** as the authentication type.
   - Paste the copied JWT access token into the **Token** field.


---

## 👩‍💻 Author

**Sehrish Fatima**

GitHub: **https://github.com/sehrish118**


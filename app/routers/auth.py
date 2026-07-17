from fastapi import APIRouter, HTTPException, Depends
import sqlite3

from app.database import get_db
from app.models import UserCreate, UserLogin, Token
from app.auth import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", status_code=201)
def register(user: UserCreate, conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username = ? OR email = ?",
        (user.username, user.email),
    )
    existing_user = cursor.fetchone()

    if existing_user:
        raise HTTPException(
            status_code=400, detail="Username or email already registered"
        )

    hashed_pw = hash_password(user.password)

    cursor.execute(
        "INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)",
        (user.username, user.email, hashed_pw),
    )
    conn.commit()

    return {"message": "User registered successfully"}


@router.post("/login", response_model=Token)
def login(user: UserLogin, conn: sqlite3.Connection = Depends(get_db)):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (user.username,))
    db_user = cursor.fetchone()

    if db_user is None or not verify_password(
        user.password, db_user["hashed_password"]
    ):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": db_user["username"]})

    return {"access_token": access_token, "token_type": "bearer"}

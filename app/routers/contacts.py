from fastapi import APIRouter, HTTPException, Depends
import sqlite3

from app.core.database import get_db
from app.schemas.contact import Contact
from app.schemas.user import UserOut
from app.dependencies import get_current_user

router = APIRouter()


@router.get("/contacts")
def get_contacts(
    conn: sqlite3.Connection = Depends(get_db),
    current_user: UserOut = Depends(get_current_user),
):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM contacts WHERE user_id=?",
        (current_user.id,),
    )
    rows = cursor.fetchall()
    return [dict(row) for row in rows]


@router.get("/contacts/{contact_id}")
def find_contact(
    contact_id: int,
    conn: sqlite3.Connection = Depends(get_db),
    current_user: UserOut = Depends(get_current_user),
):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM contacts WHERE id=? AND user_id=?",
        (contact_id, current_user.id),
    )
    row = cursor.fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Contact not found")

    return dict(row)


@router.post("/contacts", status_code=201)
def add_contact(
    contact: Contact,
    conn: sqlite3.Connection = Depends(get_db),
    current_user: UserOut = Depends(get_current_user),
):
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM contacts WHERE email=? AND user_id=?",
        (contact.email, current_user.id),
    )
    existing_email = cursor.fetchone()

    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists.")

    cursor.execute(
        """
        INSERT INTO contacts(user_id, name, phone, email, group_name)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            current_user.id,
            contact.name,
            contact.phone,
            contact.email,
            contact.group,
        ),
    )

    conn.commit()
    contact_id = cursor.lastrowid

    return {
        "id": contact_id,
        "user_id": current_user.id,
        "name": contact.name,
        "phone": contact.phone,
        "email": contact.email,
        "group": contact.group,
    }


@router.put("/contacts/{contact_id}")
def update_contact(
    contact_id: int,
    contact: Contact,
    conn: sqlite3.Connection = Depends(get_db),
    current_user: UserOut = Depends(get_current_user),
):
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE contacts
        SET name=?, phone=?, email=?, group_name=?
        WHERE id=? AND user_id=?
        """,
        (
            contact.name,
            contact.phone,
            contact.email,
            contact.group,
            contact_id,
            current_user.id,
        ),
    )

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Contact not found or you don't have permission to update it.",
        )

    conn.commit()

    return {
        "message": "Contact Updated Successfully.",
        "contact": {
            "id": contact_id,
            "user_id": current_user.id,
            "name": contact.name,
            "phone": contact.phone,
            "email": contact.email,
            "group": contact.group,
        },
    }


@router.delete("/contacts/{contact_id}")
def delete_contact(
    contact_id: int,
    conn: sqlite3.Connection = Depends(get_db),
    current_user: UserOut = Depends(get_current_user),
):
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM contacts WHERE id=? AND user_id=?",
        (contact_id, current_user.id),
    )

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="Contact not found or you don't have permission to delete it.",
        )

    conn.commit()

    return {"message": f"Contact with id {contact_id} deleted successfully."}

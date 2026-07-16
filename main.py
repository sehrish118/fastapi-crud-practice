# from fastapi import FastAPI, HTTPException

# from pydantic import BaseModel


# class Contact(BaseModel):
#     name: str
#     phone: str
#     email: str
#     group: str


# contactsData = [
#     {
#         "id": 1,
#         "name": "Ahmed Khan",
#         "phone": "03001234567",
#         "email": "ahmed@gmail.com",
#         "group": "family",
#     },
#     {
#         "id": 2,
#         "name": "Sara Ali",
#         "phone": "03211234567",
#         "email": "sara@gmail.com",
#         "group": "work",
#     },
#     {
#         "id": 3,
#         "name": "Bilal Sheikh",
#         "phone": "03451234567",
#         "email": "bilal@gmail.com",
#         "group": "friends",
#     },
# ]


# app = FastAPI()


# @app.get("/contacts")
# def contacts():
#     return contactsData


# @app.get("/contacts/{contact_id}")
# def findContact(contact_id: int):

#     for contact in contactsData:
#         if contact_id == contact["id"]:
#             return contact

#     raise HTTPException(status_code=404, detail="Contact not found.")


# @app.post("/contacts")
# def addContact(contact: Contact):
#     id = (contactsData[-1]["id"]) + 1 if contact else 1

#     contactDict = contact.model_dump()

#     contactDict["id"] = id

#     contactsData.append(contactDict)

#     return {"message": "New member is added Successfully!", "details": contactDict}


# @app.delete("/contacts/{contact_id}")
# def Delete(contact_id: int):
#     for contact in contactsData:
#         if contact_id == contact["id"]:
#             contactsData.remove(contact)
#             return {"message": "Contact Removed successfully"}

#     raise HTTPException(status_code=404, detail="Contact not found")


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()


# pyndamic model
class Contact(BaseModel):
    name: str
    phone: str
    email: str
    group: str


def get_db_connection():
    conn = sqlite3.connect("contacts.db")
    conn.row_factory = sqlite3.Row

    return conn


@app.get("/contacts")
def contact():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


@app.get("/contacts/{contact_id}")
def findContact(contact_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE id=?", (contact_id,))
    row = cursor.fetchone()

    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Contact not found")

    return dict(row)


@app.post("/contacts")
def addContact(contact: Contact):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO contacts(name, phone, email, group_name) 
        VALUES(?,?,?,?)
    """,
        (contact.name, contact.phone, contact.email, contact.group),
    )

    conn.commit()
    id = cursor.lastrowid
    conn.close()

    return {
        "message": "Contact added successfully",
        "contact": {
            "id": id,
            "name": contact.name,
            "phone": contact.phone,
            "email": contact.email,
            "group": contact.group,
        },
    }


@app.put("/contacts/{contact_id}")
def updateContact(contact_id: int, contact: Contact):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE contacts SET name=?, phone=?, email=?, group_name=? where id=?""",
        (contact.name, contact.phone, contact.email, contact.group, contact_id),
    )

    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="ID does not exist")

    conn.commit()
    conn.close()

    return {
        "message": "Contact Updated Successfully.",
        "contact": {
            "id": contact_id,
            "name": contact.name,
            "phone": contact.phone,
            "email": contact.email,
            "group": contact.group,
        },
    }


@app.delete("/contacts/{contact_id}")
def deleteContact(contact_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))

    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Id does not exist")

    conn.commit()
    conn.close()

    return {"message": f"Contact with id {contact_id} deleted successfully."}

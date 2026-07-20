from pydantic import BaseModel, EmailStr, Field


class Contact(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    phone: str = Field(..., max_length=13)
    email: EmailStr
    group: str = Field(..., min_length=2)

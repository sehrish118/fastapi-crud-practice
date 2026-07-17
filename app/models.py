from pydantic import BaseModel, EmailStr, Field


class Contact(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    phone: str = Field(..., max_length=13)
    email: EmailStr
    group: str = Field(..., min_length=2)


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(..., min_length=6)


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

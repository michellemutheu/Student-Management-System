from pydantic import BaseModel, EmailStr
from typing import Optional

class StudentCreate(BaseModel):
    name: str
    email: str
    course: str
    grade: Optional[float] = None

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    course: str
    grade: Optional[float] = None

    class Config:
        from_attributes = True

class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None

class Token(BaseModel):
    access_token: str
    token_type: str

class UserCreate(BaseModel):
    email: str
    password: str

class LoginSchema(BaseModel):
    email: EmailStr
    password: str
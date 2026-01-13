from pydantic import BaseModel, EmailStr
from enum import Enum

class UserRole(str, Enum):
    Admin = "Admin"
    Analyst = "Analyst"
    Manager = "Manager"

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: UserRole

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole

    class Config:
        orm_mode = True

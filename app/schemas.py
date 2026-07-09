Python
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    firstName: str
    lastName: str
    cpf: str
    email: EmailStr
    password: str
    confirmPassword: str

class Token(BaseModel):
    token: str
    token_type: str
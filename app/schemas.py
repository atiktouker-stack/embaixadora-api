from pydantic import BaseModel, EmailStr

# Esquema para o Cadastro de Usuário
class UserCreate(BaseModel):
    firstName: str
    lastName: str
    cpf: str
    phone: str
    email: EmailStr
    password: str
    confirmPassword: str
    street: str
    neighborhood: str
    city: str
    state: str

# Esquema para o Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Esquema de Reserva (quando o usuário escolhe os números)
class ReservaCreate(BaseModel):
    quantity: int
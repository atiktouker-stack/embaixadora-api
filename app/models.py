from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String)
    lastName = Column(String)
    cpf = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String) # Guardaremos o hash da senha, nunca a senha pura!

# Exemplo básico de tabela de reservas (para evoluirmos)
class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    number = Column(String, unique=True)
    status = Column(String, default="Pendente") # Pendente, Pago
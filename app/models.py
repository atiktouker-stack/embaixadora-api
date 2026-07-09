from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    cpf = Column(String, unique=True, index=True)
    phone = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    # Endereço
    street = Column(String)
    neighborhood = Column(String)
    city = Column(String)
    state = Column(String)

    reservas = relationship("Reserva", back_populates="owner")

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String, unique=True)
    quantity = Column(Integer)
    status = Column(String, default="Pendente") # Pendente, Pago
    user_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="reservas")

class Ganhador(Base):
    __tablename__ = "ganhadores"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    campaign_name = Column(String)
    winning_number = Column(String)
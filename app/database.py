import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# URL vinda do arquivo .env ou das Variáveis de Ambiente do Render
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Função para garantir que cada requisição tenha sua própria sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
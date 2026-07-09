import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# URL de conexão (deve estar no seu arquivo .env)
# Exemplo: DATABASE_URL=postgresql://usuario:senha@host:porta/nome_banco
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Cria o engine (motor de conexão)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Cria a fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os seus modelos (herde de Base no models.py)
Base = declarative_base()

# Dependência para usar nas rotas (para abrir/fechar a sessão)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
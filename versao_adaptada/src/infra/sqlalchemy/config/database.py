from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./db_vale_tenis.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#O engine do SQLAlchemy é responsável por estabelecer a conexão com o banco de dados, executar instruções SQL e gerenciar transações.

Base = declarative_base() #Definir Modelos de Dados 


def criar_bd():
    Base.metadata.create_all(bind=engine)


def get_db(): #Conexão Prinncipal
    db = SessionLocal()
    try:
        yield db     #faz com que a função se comporte como um gerador (objeto db sob demanda)
    finally:         
        db.close()   #Garantindo que o banco de dados seja fechado corretamente após o uso

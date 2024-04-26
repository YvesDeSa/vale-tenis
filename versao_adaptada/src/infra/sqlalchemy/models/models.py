from sqlalchemy import Column, Date, Integer, String, Float, Boolean
from src.infra.sqlalchemy.config.database import Base


class Produto(Base):#Define uma classe chamada Produto que herda da classe Base, 
                    #O que significa que Produto será um modelo de dados SQLAlchemy.

    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, index=True )
    nome = Column(String)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column (Boolean)


class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True )
    nome = Column(String)
    sobrenome = Column(String)
    sexo = Column(String)
    data_nascimento = Column(Date)
    cpf = Column(String)
    celular = Column(String)
    email = Column(String)
    senha = Column(String)

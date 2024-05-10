from sqlalchemy import Column, Integer, String, Date, Double, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column



class Produto(Base):#Define uma classe chamada Produto que herda da classe Base, 
                    #O que significa que Produto será um modelo de dados SQLAlchemy.

    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, index=True )
    marca = Column(String)
    modelo = Column(String)
    #preco = Column(Float)
    tipo_genero = Column(String) #adulto / infantil
    genero = Column(String) # Masculino / feminino / unisex 
    detalhe = Column (String)
    cor = Column(String)
    fornecedor_id = Column(Integer, ForeignKey('fornecedor.id'))
     
    fornecedor = relationship("Fornecedor", back_populates="produtos") 
    # Define o relacionamento com a tabela produto_tamanho
    tamanhos = relationship("ProdutoTamanho", back_populates="produto")




class ProdutoTamanho(Base):
    __tablename__ = "produto_tamanho"

    id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("produto.id"))  # Chave estrangeira referenciando a tabela produto
    quantidade = Column(Integer)
    tamanho = Column(Integer)
    preco = Column(Double)

    # Define o relacionamento com a tabela produto
    produto = relationship("Produto", back_populates="tamanhos")


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


class Fornecedor(Base):
    __tablename__ = "fornecedor"
    id = Column(Integer, primary_key=True, index=True )
    nome = Column(String)
    cnpj = Column(String)
    endereco = Column(String)
    celular = Column(String)
    email = Column(String)
    
    produtos = relationship("Produto", back_populates="fornecedor")
 
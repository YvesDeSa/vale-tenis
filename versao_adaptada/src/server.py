from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .schemas.schemas import Produto, ProdutoTamanho, Cliente

from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.produto_tamanho import RepositorioProdutoTamanho
from src.infra.sqlalchemy.repositorios.cliente import RepositorioCliente


criar_bd()


app = FastAPI()


@app.post("/produtos")
def criar_produto(produto: Produto, db:Session = Depends(get_db)):# Depends vem do FastAPI para injetar oque passamos
    produto_criado = RepositorioProduto(db).criar(produto)
    return{"MSG":"Produto Criado"}


@app.post("/produto-tamanho")
def criar_produto_tamanho(produto: ProdutoTamanho, db:Session = Depends(get_db)):# Depends vem do FastAPI para injetar oque passamos
    produto_criado = RepositorioProdutoTamanho(db).criar(produto)
    return{"MSG":"Produto Criado"}


@app.get("/produtos")
def listar_produtos():
    return {"MSG": "Lisatagem de Produtos"}

@app.post("/cliente")
def criar_cliente(cliente: Cliente, db:Session = Depends(get_db)):# Depends vem do FastAPI para injetar oque passamos
    cliente = RepositorioCliente(db).criar(cliente)
    return{"Cliente Cadastrado"}


@app.get("/clientes")
def listar_clientes(db:Session = Depends(get_db)):
    clientes = RepositorioCliente(db).listar()
    return clientes
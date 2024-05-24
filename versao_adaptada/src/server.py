from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .schemas.schemas import Fornecedor, Pedido, Produto, ProdutoTamanho, Cliente

from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.fornecedor import RepositorioFornecedor
from src.infra.sqlalchemy.repositorios.cliente import RepositorioCliente
from src.infra.sqlalchemy.repositorios.pedido import RepositorioPedido


criar_bd()


app = FastAPI()


# Rotas Produto 
@app.post("/produtos")
def criar_produto(produto: Produto, db:Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return{"MSG":"Produto Criado"}


@app.put("/produtos")
def criar_produto(produto: Produto, db:Session = Depends(get_db)):
    RepositorioProduto(db).update(produto)
    return{"MSG":"Produto Alterado"}


# @app.post("/produto-tamanho")
# def criar_produto_tamanho(produto: ProdutoTamanho, db:Session = Depends(get_db)):
#     produto_criado = RepositorioProdutoTamanho(db).criar(produto)
#     return{"MSG":"Produto Criado"}


@app.get("/produtos")
def listar_produtos(db:Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


@app.get("/produto/{produto_id}")
def obter_produto(produto_id:int, db:Session = Depends(get_db), ):
    produto = RepositorioProduto(db).obter(produto_id)
    return produto


@app.delete("/produto/{produto_id}")
def remover_produto(produto_id:int, db:Session = Depends(get_db), ):
    if RepositorioProduto(db).remover(produto_id):
        return{f"Produto {produto_id} removido com sucesso!"}
    else:
        return{f"Não foi possível remover o produto {produto_id}"}


# Rotas Cliente
@app.post("/cliente")
def criar_cliente(cliente: Cliente, db:Session = Depends(get_db)):
    cliente = RepositorioCliente(db).criar(cliente)
    return{"Cliente Cadastrado"}


@app.get("/clientes")
def listar_clientes(db:Session = Depends(get_db)):
    clientes = RepositorioCliente(db).listar()
    return clientes


@app.get("/cliente/{cliente_id}")
def obter_cliente(cliente_id:int, db:Session = Depends(get_db), ):
    cliente = RepositorioCliente(db).obter(cliente_id)
    return cliente


@app.delete("/cliente/{cliente_id}")
def remover_cliente(cliente_id:int, db:Session = Depends(get_db), ):
    if RepositorioCliente(db).remover(cliente_id):
        return{f"Cliente {cliente_id} removido com sucesso!"}
    else:
        return{f"Não foi possível remover o cliente {cliente_id}"}


@app.put("/cliente")
def atualizar_cliente(cliente:Cliente, db:Session = Depends(get_db), ):
    cliente = RepositorioCliente(db).editar(cliente)
    return {"Cliente editado"}
    

# Rotas Fornecedor
@app.post("/fornecedor")
def criar_fornecedor(fornecedor: Fornecedor, db:Session = Depends(get_db)):
    fornecedor = RepositorioFornecedor(db).criar(fornecedor)
    return{"Fornecedor Cadastrado"}


@app.put("/fornecedor")
def atualizar_fornecedor(fornecedor:Fornecedor, db:Session = Depends(get_db), ):
    fornecedor = RepositorioFornecedor(db).editar(fornecedor)
    return {"Fornecedor editado"}


@app.get("/fornecedores")
def listar_fornecedores(db:Session = Depends(get_db)):
    fornecedores = RepositorioFornecedor(db).listar()
    return fornecedores


@app.get("/fornecedores/{fornecedor_id}")
def obter_fornecedor(fornecedor_id: int, db:Session = Depends(get_db)):
    fornecedor = RepositorioFornecedor(db).obter(fornecedor_id)
    return fornecedor 


@app.delete("/fornecedores/{fornecedor_id}")
def deletar_fornecedor(fornecedor_id: int, db:Session = Depends(get_db)):
    fornecedor = RepositorioFornecedor(db).remover(fornecedor_id)
    return fornecedor 


# Rotas Pedido 
@app.post("/pedido")
def criar_pedido(pedido: Pedido, db:Session = Depends(get_db)):
    pedido = RepositorioPedido(db).criar(pedido)
    return{"Pedido Cadastrado"}


@app.get("/pedidos")
def listar_pedidos(db:Session = Depends(get_db)):
    pedidos = RepositorioPedido(db).listar()
    return pedidos


@app.get("/pedido/{pedido_id}")
def obter_pedido(pedido_id:int, db:Session = Depends(get_db)):
    pedido = RepositorioPedido(db).obter(pedido_id)
    return pedido


@app.delete("/pedido/{pedido_id}")
def remover_pedido(pedido_id:int, db:Session = Depends(get_db)):
    if RepositorioPedido(db).remover(pedido_id):
        return{f"Pedido {pedido_id} removido com sucesso!"}
    else:
        return{f"Não foi possível remover o pedido {pedido_id}"}

@app.put("/pedido")
def atualizar_pedido(pedido: Pedido, db:Session = Depends(get_db)):
    pedido = RepositorioPedido(db).update(pedido)
    return {"Pedido editado"}
    
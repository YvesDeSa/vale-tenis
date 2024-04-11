from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware #Permite que um servidor especifique quem pode acessar os recursos que ele fornece.
from fastapi import FastAPI
from pydantic import BaseModel 
from datetime import date

app = FastAPI()

origins = ['http://localhost:5501']  #Define a lista de origens permitidas para solicitações CORS.

# Permite que a aplicação aceite solicitações de diferentes origens
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

class Genero(BaseModel):
  adulto: Optional[str] = None
  infantil: Optional[str] = None

class Produto(BaseModel):
  id: Optional[int] = 0
  detalhe: str
  genero: Genero
  marca: str
  modelo: str
  tamanhos: List[int]

class Cliente(BaseModel):
  id: Optional[int] = 0
  nome: str
  sobrenome: str
  sexo: str
  dataNascimento: date
  cpf: str
  celular: str
  email: str
  senha: str


produtos: List[Produto] = []
clientes: List[Cliente] = []

idProdutoProx = 1  
idClienteProx = 1  

@app.get('/produtos')
def listProdutos():
  return produtos


@app.post('/produtos')
def postProduto(produto: Produto):
  if not produto:
    return {"mensagem": "O Produto não pode estar vazio!"}

  global idProdutoProx  
  produto.id = idProdutoProx  
  idProdutoProx += 1  

  produtos.append(produto)
  return {"mensagem":f"Produto { produto.modelo } cadastrado com sucesso!  "}


@app.get('/produtos/{produto_id}')
def getProduto(produto_id: int):
    for produto in produtos:
        if produto.id == produto_id:
            return produto
    return {"Erro": "Produto não localizado"}


@app.delete('/produtos/{produto_id}')
def deleteProduto(produto_id: int):
    for index, produto in enumerate(produtos):
        if produto.id == produto_id:
            produtos.pop(index)
            return {"mensagem":f"Produto { produto_id } removido com sucesso"}
    return {"Erro": "Produto não localizado"}


@app.get('/clientes')
def listClientes():
  return clientes


@app.post('/cliente')
def postCliente(cliente: Cliente):
  if not cliente:
    return {"mensagem": "O Cliente não pode estar vazio!"}

  for c in clientes:
    if c.cpf == cliente.cpf:
      return {"mensagem": "Cpf já cadastrado!"}

  global idClienteProx  
  cliente.id = idClienteProx  
  idClienteProx += 1  

  clientes.append(cliente)
  return{"mensagem":f"Cliente { cliente.nome } cadastrado com sucesso! "}


@app.get('/clientes/{cliente_id}')
def getCliente(cliente_id: int):
    for cliente in clientes:
        if cliente.id == cliente_id:
            return cliente
    return {"Erro": "Cliente não localizado"}


@app.delete('/clientes/{cliente_id}')
def deleteCliente(cliente_id: int):
    for index, cliente in enumerate(clientes):
        if cliente.id == cliente_id:
            clientes.pop(index)
            return {"mensagem":f"Cliente { cliente_id } removido com sucesso"}
    return {"Erro": "Cliente não localizado"}
from pydantic import BaseModel
from typing import Optional, List
from datetime import date



class ProdutoTamanho(BaseModel):
    id: Optional[int] = None
    produto_id: int
    quantidade: int
    tamanho: int
    preco: float

    
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


class Produto(BaseModel):
    id: Optional[int] = None
    marca: str
    detalhe: str
    modelo: str
    tipo_genero: str
    genero: str
    tamanhos: List[ProdutoTamanho]
    fornecedor_id:int

    class Config:
         orm_mode = True

class Fornecedor(BaseModel):
    id: Optional[int] = None
    nome: str
    cnpj: str
    endereco: str
    celular: str
    email: str
    
    class Config:
        orm_mode=True


class ItemPedido(BaseModel):
    id: Optional[str] = None
    preco_item: float
    quantidade: int
    pedido_id: int
    produto_id: int

    class Config:
        orm_mode=True
        
class Pedido(BaseModel):
    id: Optional[str] = None
    cliente_id: int
    data: date
    preco_total: float
    itens_pedido: List[ItemPedido]
    
    class Config:
        orm_mode=True


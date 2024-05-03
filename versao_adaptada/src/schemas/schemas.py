from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str


class ProdutoTamanho(BaseModel):
    id: Optional[int] = None
    produto_id: int
    quantidade: int
    tamanho: int

    
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

    # class Config:
    #     orm_mode = True


class Pedido(BaseModel):
    id: Optional[str] = None
    quantidade: int
    entrega: bool = False
    endereco: str
    observacoes: Optional[str] = "Sem Observações"


class Fornecedor(BaseModel):
    id : Optional[int] = None
    nome : str
    cnpj : str
    endereco : str
    celular : str
    email : str
    
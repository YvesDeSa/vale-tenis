from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str

class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

    class Config:
        orm_mode = True

class Pedido(BaseModel):
    id: Optional[str] = None
    quantidade: int
    entrega: bool = False
    endereco: str
    observacoes: Optional[str] = "Sem Observações"

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
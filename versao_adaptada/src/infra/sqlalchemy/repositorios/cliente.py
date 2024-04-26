from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioCliente():

    def __init__(self, db: Session):
        self.db = db
        


    def criar(self, cliente: schemas.Cliente):# Covertendo o Schema em um modelo
        db_cliente = models.Cliente(nome = cliente.nome,
                                    sobrenome = cliente.sobrenome,
                                    sexo = cliente.sexo,
                                    data_nascimento = cliente.dataNascimento,
                                    cpf = cliente.cpf,
                                    celular = cliente.celular,
                                    email = cliente.email,
                                    senha = cliente.senha)
        self.db.add(db_cliente)
        self.db.commit()
        self.db.refresh(db_cliente)
        return db_cliente


    def listar(self):
        clientes = self.db.query(models.Cliente).all()
        return  clientes

    def obter(self):
        pass

    def remover(self):
        pass
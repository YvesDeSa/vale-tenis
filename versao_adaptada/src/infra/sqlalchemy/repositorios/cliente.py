from sqlalchemy import update

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


    def editar(self, cliente: schemas.Cliente):
        update_stmt = update(models.Cliente).where(
            models.Cliente.id == cliente.id).values(
                                    nome = cliente.nome,
                                    sobrenome = cliente.sobrenome,
                                    sexo = cliente.sexo,
                                    data_nascimento = cliente.dataNascimento,
                                    cpf = cliente.cpf,
                                    celular = cliente.celular,
                                    email = cliente.email,
                                    senha = cliente.senha
                                    )
        self.db.execute(update_stmt)
        self.db.commit()
        
    def listar(self):
        clientes = self.db.query(models.Cliente).all()
        return  clientes

    def obter(self, cliente_id: int):
        cliente = self.db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
        return cliente
    

    def remover(self, cliente_id: int):
        cliente = self.db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
        if cliente:
            self.db.delete(cliente)
            self.db.commit()
            return True
        return False
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioFornecedor():

    def __init__(self, db: Session):
        self.db = db
        


    def criar(self, fornecedor: schemas.Fornecedor):# Covertendo o Schema em um modelo
        db_fornecedor = models.Fornecedor(nome = fornecedor.nome,
                                    celular = fornecedor.celular,
                                    email = fornecedor.email,
                                    cnpj = fornecedor.cnpj,
                                    endereco = fornecedor.endereco, 
                                    )
        self.db.add(db_fornecedor)
        self.db.commit()
        self.db.refresh(db_fornecedor)
        return db_fornecedor


    def listar(self):
        fornecedores = self.db.query(models.Fornecedor).all()
        return  fornecedores

    def obter(self, fornecedor_id: int):
        fornecedor = self.db.query(models.Fornecedor).filter(models.Fornecedor.id == fornecedor_id).first()
        return fornecedor


    def remover(self, fornecedor_id: int):
        fornecedor = self.obter(fornecedor_id)
        if fornecedor:
            self.db.delete(fornecedor)
            self.db.commit()
            return fornecedor
        return False
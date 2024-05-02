from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db
        


    def criar(self, produto: schemas.Produto):# Covertendo o Schema em um modelo
        db_produto = models.Produto(marca=produto.marca, 
                                    detalhe=produto.detalhe,
                                    modelo=produto.modelo,
                                    tipo_genero=produto.tipo_genero,
                                    genero=produto.genero,
                                    )
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto


    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return  produtos

    def obter(self):
        pass

    def remover(self):
        pass
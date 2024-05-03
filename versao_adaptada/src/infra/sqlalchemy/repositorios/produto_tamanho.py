from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioProdutoTamanho():

    def __init__(self, db: Session):
        self.db = db
        


    def criar(self, produto_tamanho: schemas.ProdutoTamanho):# Covertendo o Schema em um modelo
        db_produto = models.ProdutoTamanho(produto_id=produto_tamanho.id, 
                                    quantidade=produto_tamanho.quantidade,
                                    tamanho=produto_tamanho.tamanho
                                    )
        db_produto.id = 0
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto


    def listar(self):
        produtos = self.db.query(models.ProdutoTamanho).all()
        return  produtos

    def obter(self):
        pass

    def remover(self):
        pass
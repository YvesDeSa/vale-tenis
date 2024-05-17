from sqlalchemy.orm import Session, joinedload
from src.infra.sqlalchemy.repositorios.produto_tamanho import RepositorioProdutoTamanho
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioProduto():

    def __init__(self, db: Session):
        self.db = db
        

    
    def fornecedor_existe(self, fornecedor_id: int):
         return self.db.query(models.Fornecedor).filter(models.Fornecedor.id == fornecedor_id).first() is not None


    def criar(self, produto: schemas.Produto):# Covertendo o Schema em um modelo
        if not self.fornecedor_existe(produto.fornecedor_id):
            raise ValueError('Fornecedor não existe')
        
        db_produto = models.Produto(marca=produto.marca, 
                                    detalhe=produto.detalhe,
                                    modelo=produto.modelo,
                                    tipo_genero=produto.tipo_genero,
                                    genero=produto.genero,
                                    fornecedor_id=produto.fornecedor_id
                                    )

        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)

        # Criar os registros de tamanhos associados ao produto
        for tamanho in produto.tamanhos:
            db_produto_tamanho = models.ProdutoTamanho(
                produto_id=db_produto.id,
                quantidade=tamanho.quantidade,
                tamanho=tamanho.tamanho
            )
            self.db.add(db_produto_tamanho)

            # self.db.refresh(db_produto_tamanho)

        self.db.commit()

        return db_produto


    



    def listar(self):
        produtos = self.db.query(models.Produto).options(joinedload(models.Produto.tamanhos)).all()
        return produtos
    

    def obter(self, produto_id: int):
        produto = self.db.query(models.Produto).filter(models.Produto.id == produto_id).\
            options(joinedload(models.Produto.tamanhos)).first()
        return produto

    def remover(self, produto_id: int):
        produto = self.db.query(models.Produto).filter(models.Produto.id == produto_id).\
            options(joinedload(models.Produto.tamanhos)).first()
        if produto:
            for tamanho in produto.tamanhos:
                self.db.delete(tamanho)

            self.db.delete(produto)
            self.db.commit()
            return True
        return False
from sqlalchemy import update
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
            self.criarProdutoTamanho(tamanho, db_produto.id)

        self.db.commit()

        return db_produto


    def update(self, produto: schemas.Produto):
        if not self.fornecedor_existe(produto.fornecedor_id):
            raise ValueError('Fornecedor não existe')
        
        update_produto = update(models.Produto).where(
            models.Produto.id == produto.id).values(marca=produto.marca, 
                                                    detalhe=produto.detalhe,
                                                    modelo=produto.modelo,
                                                    tipo_genero=produto.tipo_genero,
                                                    genero=produto.genero,
                                                    fornecedor_id=produto.fornecedor_id)

        self.db.execute(update_produto)
        self.db.commit()

        for tamanho in produto.tamanhos:
            if tamanho.id == 0:
                self.criarProdutoTamanho(tamanho, produto.id)
            else:
                update_tamanho = update(models.ProdutoTamanho).where(models.ProdutoTamanho.id == tamanho.id).values(
                    produto_id=produto.id,
                    quantidade=tamanho.quantidade,
                    tamanho=tamanho.tamanho
                )
                self.db.execute(update_tamanho)
                self.db.commit()



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


    def criarProdutoTamanho(self, produto_tamanho: schemas.ProdutoTamanho, id_produto):
        db_produto_tamanho = models.ProdutoTamanho(
                produto_id=id_produto,
                quantidade=produto_tamanho.quantidade,
                tamanho=produto_tamanho.tamanho
            )
        self.db.add(db_produto_tamanho)
        self.db.commit()

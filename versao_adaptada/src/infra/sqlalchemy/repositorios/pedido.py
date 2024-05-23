from sqlalchemy import update
from sqlalchemy.orm import Session, joinedload
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class Pedido():

    def __init__(self, db: Session):
        self.db = db
    

    def criar(self, pedido: schemas.Pedido):

        db_pedido = models.Pedido(cliente_id = pedido.cliente_id,
                                  data = pedido.data,
                                  preco_total = pedido.preco_total)
        
        self.db.add(db_pedido)
        self.db.commit()
        self.db.refresh(db_pedido)

        for item in pedido.itens_pedido:
            self.criarItemPedido(item, db_pedido.id)

        self.db.commit()

        return db_pedido
    

    def update(self, pedido: schemas.Pedido):
        update_pedido = update(models.Pedido).where(models.Pedido.id == pedido.id).values(
                                  cliente_id = pedido.cliente_id,
                                  data = pedido.data,
                                  preco_total = pedido.preco_total)

        self.db.execute(update_pedido)
        self.db.commit()

        for item in pedido.itens_pedido:
            if item.id == 0:
                self.criarItemPedido(item, pedido.id)
            else:
                update_item = update(models.ItemPedido).where(
                    models.ItemPedido.id == item.id).values(preco_item=item.preco_item,
                                                            quantidade=item.quantidade,
                                                            produto_id=item.produto_id,
                                                            pedido_id=pedido.id)
                self.db.execute(update_item)
                self.db.commit()


    def listar(self):
        pedidos = self.db.query(models.Pedido).options(joinedload(models.Pedido.itens_pedido)).all()
        return pedidos
    

    def obter(self, pedido_id: int):
        pedido = self.db.query(models.Pedido).filter(models.Pedido.id == pedido_id).\
            options(joinedload(models.Pedido.itens_pedido)).first()
        return pedido


    def remover(self, pedido_id: int):
        pedido = self.db.query(models.Pedido).filter(models.Pedido.id == pedido_id).\
            options(joinedload(models.Pedido.itens_pedido)).first()
        if pedido:
            for item in pedido.itens_pedido:
                self.db.delete(item)

            self.db.delete(pedido)
            self.db.commit()
            return True
        return False


    def criarItemPedido(self, item: schemas.ItemPedido, id_pedido):
        db_item = models.ItemPedido(
                preco_item=item.preco_item,
                quantidade=item.quantidade,
                produto_id=item.produto_id,
                pedido_id=id_pedido
            )
        self.db.add(db_item)
        self.db.commit()
        print("CRIOU")
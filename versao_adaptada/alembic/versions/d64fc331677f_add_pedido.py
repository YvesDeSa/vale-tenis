"""Add Pedido

Revision ID: d64fc331677f
Revises: 6ac4ba1aa409
Create Date: 2024-05-24 12:53:59.996965

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd64fc331677f'
down_revision: Union[str, None] = '6ac4ba1aa409'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pedido',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.Column('data', sa.Date(), nullable=True),
    sa.Column('preco_total', sa.Double(), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['cliente.id'], name='fk_cliente'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('pedido', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_pedido_id'), ['id'], unique=False)

    op.create_table('item_tamanho',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('preco_item', sa.Double(), nullable=True),
    sa.Column('quantidade', sa.Integer(), nullable=True),
    sa.Column('pedido_id', sa.Integer(), nullable=True),
    sa.Column('produto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pedido_id'], ['pedido.id'], name='fk_pedido'),
    sa.ForeignKeyConstraint(['produto_id'], ['produto.id'], name='fk_produto'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('item_tamanho', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_item_tamanho_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item_tamanho', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_item_tamanho_id'))

    op.drop_table('item_tamanho')
    with op.batch_alter_table('pedido', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_pedido_id'))

    op.drop_table('pedido')
    # ### end Alembic commands ###
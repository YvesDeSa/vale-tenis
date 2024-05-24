"""correcao Pedido

Revision ID: e2cd9884dbb2
Revises: d64fc331677f
Create Date: 2024-05-24 13:05:14.244602

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2cd9884dbb2'
down_revision: Union[str, None] = 'd64fc331677f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item_tamanho', schema=None) as batch_op:
        batch_op.drop_index('ix_item_tamanho_id')

    op.drop_table('item_tamanho')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item_tamanho',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('preco_item', sa.DOUBLE(), nullable=True),
    sa.Column('quantidade', sa.INTEGER(), nullable=True),
    sa.Column('pedido_id', sa.INTEGER(), nullable=True),
    sa.Column('produto_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['pedido_id'], ['pedido.id'], name='fk_pedido'),
    sa.ForeignKeyConstraint(['produto_id'], ['produto.id'], name='fk_produto'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('item_tamanho', schema=None) as batch_op:
        batch_op.create_index('ix_item_tamanho_id', ['id'], unique=False)

    # ### end Alembic commands ###
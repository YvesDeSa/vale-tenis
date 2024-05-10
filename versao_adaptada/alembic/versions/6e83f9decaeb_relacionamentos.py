"""Relacionamentos

Revision ID: 6e83f9decaeb
Revises: ef62f31829b1
Create Date: 2024-05-10 15:22:20.553761

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6e83f9decaeb'
down_revision: Union[str, None] = 'ef62f31829b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produto', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cor', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('fornecedor_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_fornecedor', 'fornecedor', ['fornecedor_id'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produto', schema=None) as batch_op:
        batch_op.drop_constraint('fk_fornecedor', type_='foreignkey')
        batch_op.drop_column('fornecedor_id')
        batch_op.drop_column('cor')

    # ### end Alembic commands ###

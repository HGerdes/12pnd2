"""add inv table

Revision ID: 26d4b84c3ea0
Revises: b4ca3c344920
Create Date: 2023-10-24 00:29:16.734673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26d4b84c3ea0'
down_revision: Union[str, None] = 'b4ca3c344920'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inv_analysis_cups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cup_type', sa.String(length=50), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inv_analysis_cups')
    # ### end Alembic commands ###

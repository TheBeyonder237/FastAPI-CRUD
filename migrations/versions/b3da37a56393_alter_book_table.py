"""alter book table

Revision ID: b3da37a56393
Revises: b6207a4228f3
Create Date: 2024-11-02 20:24:49.708771

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b3da37a56393'
down_revision: Union[str, None] = 'b6207a4228f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('updated_at', postgresql.TIMESTAMP(), nullable=True))
    op.drop_column('books', 'update_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('update_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('books', 'updated_at')
    # ### end Alembic commands ###

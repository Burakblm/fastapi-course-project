"""add content column to post table

Revision ID: 76bf1b5342c5
Revises: b93b89d70fe5
Create Date: 2024-10-27 00:20:11.284101

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76bf1b5342c5'
down_revision: Union[str, None] = 'b93b89d70fe5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', 
                  sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

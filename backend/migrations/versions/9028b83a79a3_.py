"""empty message.

Revision ID: 9028b83a79a3
Revises: d53625a81ae4
Create Date: 2025-06-12 10:25:24.702209.
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9028b83a79a3'
down_revision: Union[str, None] = 'd53625a81ae4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_column("event", "state")
    op.add_column("event", sa.Column("state", sa.Boolean(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("event", "state")
    op.add_column("event", sa.Column("state", sa.String(), nullable=False))

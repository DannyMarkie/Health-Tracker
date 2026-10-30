"""seed units

Revision ID: 66add92e9815
Revises: 1ced2aa1f886
Create Date: 2026-10-19 20:42:22.184620

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import table, column


# revision identifiers, used by Alembic.
revision: str = "66add92e9815"
down_revision: Union[str, Sequence[str], None] = "1ced2aa1f886"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


units_table = table(
    "units",
    column("unit_code", sa.String),
    column("unit_display_name", sa.String),
)


def upgrade() -> None:
    """Upgrade schema."""
    op.bulk_insert(
        units_table,
        [
            {"unit_code": "g", "unit_display_name": "grams"},
            {"unit_code": "ml", "unit_display_name": "milliliter"},
            {"unit_code": "pcs", "unit_display_name": "pieces"},
        ],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute(
        units_table.delete().where(
            units_table.c.unit_code.in_(["g", "ml", "pcs"])
        )
    )

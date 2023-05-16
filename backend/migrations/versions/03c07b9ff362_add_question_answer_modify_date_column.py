"""Add Question & Answer modify_date column

Revision ID: 03c07b9ff362
Revises: 02325c8178c6
Create Date: 2023-05-03 18:31:11.158067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "03c07b9ff362"
down_revision = "02325c8178c6"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("answer", schema=None) as batch_op:
        batch_op.add_column(sa.Column("modify_date", sa.DateTime(), nullable=True))

    with op.batch_alter_table("question", schema=None) as batch_op:
        batch_op.add_column(sa.Column("modify_date", sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("question", schema=None) as batch_op:
        batch_op.drop_column("modify_date")

    with op.batch_alter_table("answer", schema=None) as batch_op:
        batch_op.drop_column("modify_date")

    # ### end Alembic commands ###

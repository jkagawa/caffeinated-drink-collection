"""empty message

Revision ID: 4cb1c70258a1
Revises: 2f49fc704726
Create Date: 2023-02-27 20:38:46.100978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cb1c70258a1'
down_revision = '2f49fc704726'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('drink', 'color',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('drink', 'description',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    op.alter_column('drink', 'image_url',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('drink', 'image_url',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('drink', 'description',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    op.alter_column('drink', 'color',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    # ### end Alembic commands ###

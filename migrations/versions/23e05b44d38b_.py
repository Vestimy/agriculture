"""empty message

Revision ID: 23e05b44d38b
Revises: 3cc9b010a20c
Create Date: 2021-02-03 18:58:09.960549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23e05b44d38b'
down_revision = '3cc9b010a20c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('note', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event', 'note')
    # ### end Alembic commands ###
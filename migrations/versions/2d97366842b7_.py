"""empty message

Revision ID: 2d97366842b7
Revises: 0aa9464f9e66
Create Date: 2021-02-04 15:39:32.969386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d97366842b7'
down_revision = '0aa9464f9e66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plant', sa.Column('packaging', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('plant', 'packaging')
    # ### end Alembic commands ###

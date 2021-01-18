"""empty message

Revision ID: e105b92b5c32
Revises: 
Create Date: 2021-01-18 11:02:51.775728

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e105b92b5c32'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company', sa.Column('address', sa.String(length=250), nullable=True))
    op.add_column('company', sa.Column('name', sa.String(length=250), nullable=True))
    op.add_column('company', sa.Column('phone', sa.String(length=250), nullable=True))
    op.drop_column('company', 'last_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company', sa.Column('last_name', mysql.VARCHAR(length=250), nullable=True))
    op.drop_column('company', 'phone')
    op.drop_column('company', 'name')
    op.drop_column('company', 'address')
    # ### end Alembic commands ###
"""empty message

Revision ID: 0aa9464f9e66
Revises: 23e05b44d38b
Create Date: 2021-02-04 15:36:09.009728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0aa9464f9e66'
down_revision = '23e05b44d38b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plant', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.add_column('plant', sa.Column('description', sa.String(length=500), nullable=True))
    op.add_column('plant', sa.Column('edit_time', sa.DateTime(), nullable=True))
    op.add_column('plant', sa.Column('firm_manufacturer', sa.String(length=250), nullable=True))
    op.add_column('plant', sa.Column('name', sa.String(length=250), nullable=True))
    op.add_column('plant', sa.Column('norm_making', sa.String(length=250), nullable=True))
    op.add_column('plant', sa.Column('price', sa.String(length=250), nullable=True))
    op.add_column('plant', sa.Column('protectionplants_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'plant', 'protectionplants', ['protectionplants_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'plant', type_='foreignkey')
    op.drop_column('plant', 'protectionplants_id')
    op.drop_column('plant', 'price')
    op.drop_column('plant', 'norm_making')
    op.drop_column('plant', 'name')
    op.drop_column('plant', 'firm_manufacturer')
    op.drop_column('plant', 'edit_time')
    op.drop_column('plant', 'description')
    op.drop_column('plant', 'create_time')
    # ### end Alembic commands ###

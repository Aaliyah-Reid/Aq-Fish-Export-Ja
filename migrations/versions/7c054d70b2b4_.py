"""empty message

Revision ID: 7c054d70b2b4
Revises: 
Create Date: 2024-04-10 10:59:54.986749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c054d70b2b4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fishes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('breed', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('availability', sa.String(length=80), nullable=True),
    sa.Column('photo_filename', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fishes')
    # ### end Alembic commands ###

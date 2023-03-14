"""create_category_table

Revision ID: 9616e84d1e5f
Revises: 66b9c0e031f4
Create Date: 2023-02-26 00:43:21.320879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9616e84d1e5f'
down_revision = '66b9c0e031f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('category_name', sa.String(length=255), nullable=False),
    sa.Column('id', sa.String(length=40), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categories')
    # ### end Alembic commands ###

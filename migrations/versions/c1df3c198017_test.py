"""test

Revision ID: c1df3c198017
Revises: 1b8beb68aa6f
Create Date: 2022-04-22 11:56:34.956891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1df3c198017'
down_revision = '1b8beb68aa6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'username2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username2', sa.VARCHAR(length=60), autoincrement=False, nullable=True))
    # ### end Alembic commands ###

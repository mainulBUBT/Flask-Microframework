"""empty message

Revision ID: 2f3038551599
Revises: 
Create Date: 2022-01-24 13:50:55.662795

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2f3038551599'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=254), nullable=True),
    sa.Column('role', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('deName', table_name='marchant')
    op.drop_table('marchant')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('marchant',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('deName', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('dePass', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('intake', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('course', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('att', mysql.VARCHAR(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('deName', 'marchant', ['deName'], unique=False)
    op.drop_table('user')
    # ### end Alembic commands ###

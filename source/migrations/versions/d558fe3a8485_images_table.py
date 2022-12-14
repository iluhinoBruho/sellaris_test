"""images table

Revision ID: d558fe3a8485
Revises: 234cbada4d68
Create Date: 2022-09-09 20:47:51.360159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd558fe3a8485'
down_revision = '234cbada4d68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(length=140), nullable=True),
    sa.Column('offer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['offer_id'], ['offer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image')
    # ### end Alembic commands ###

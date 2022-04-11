"""Added outcomes table

Revision ID: 903eb5b1dbe4
Revises: 
Create Date: 2022-04-11 12:25:04.993854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '903eb5b1dbe4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Outcomes',
    sa.Column('ship', sa.VARCHAR(length=50), nullable=False),
    sa.Column('battle', sa.VARCHAR(length=20), nullable=False),
    sa.Column('result', sa.VARCHAR(length=10), nullable=False),
    sa.PrimaryKeyConstraint('ship', 'battle')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Outcomes')
    # ### end Alembic commands ###

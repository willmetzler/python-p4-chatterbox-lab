"""your message

Revision ID: 8af691fec235
Revises: 3728a1ffb5d1
Create Date: 2024-05-15 15:55:25.321203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8af691fec235'
down_revision = '3728a1ffb5d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('username', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'username')
    # ### end Alembic commands ###

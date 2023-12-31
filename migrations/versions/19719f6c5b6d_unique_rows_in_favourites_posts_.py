"""unique rows in favourites_posts_association

Revision ID: 19719f6c5b6d
Revises: 5da016ee2ca9
Create Date: 2023-09-29 02:45:29.462817

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '19719f6c5b6d'
down_revision = '5da016ee2ca9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('picture')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('picture', postgresql.BYTEA(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###

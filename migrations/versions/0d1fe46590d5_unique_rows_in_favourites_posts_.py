"""unique rows in favourites_posts_association

Revision ID: 0d1fe46590d5
Revises: 19719f6c5b6d
Create Date: 2023-09-29 04:07:13.472733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d1fe46590d5'
down_revision = '19719f6c5b6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favourite_posts_association', schema=None) as batch_op:
        batch_op.drop_constraint('favourite_posts_association_post_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('favourite_posts_association_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'posts', ['post_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favourite_posts_association', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('favourite_posts_association_user_id_fkey', 'users', ['user_id'], ['id'])
        batch_op.create_foreign_key('favourite_posts_association_post_id_fkey', 'posts', ['post_id'], ['id'])

    # ### end Alembic commands ###

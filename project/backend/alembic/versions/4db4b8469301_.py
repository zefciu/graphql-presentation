"""empty message

Revision ID: 4db4b8469301
Revises: 
Create Date: 2019-09-12 16:50:18.587932

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4db4b8469301'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actor',
    sa.Column('actor_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=45), nullable=False),
    sa.Column('last_name', sa.String(length=45), nullable=False),
    sa.Column('last_update', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('actor_id')
    )
    op.create_index(op.f('ix_actor_last_name'), 'actor', ['last_name'], unique=False)
    op.create_table('category',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.Column('last_update', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('category_id')
    )
    op.create_table('language',
    sa.Column('language_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.CHAR(length=20), nullable=False),
    sa.Column('last_update', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('language_id')
    )
    op.create_table('film',
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('release_year', sa.Integer(), nullable=True),
    sa.Column('language_id', sa.Integer(), nullable=False),
    sa.Column('original_language_id', sa.Integer(), nullable=True),
    sa.Column('rental_duration', sa.SmallInteger(), server_default=sa.text('3'), nullable=False),
    sa.Column('rental_rate', sa.Numeric(precision=4, scale=2), server_default=sa.text('4.99'), nullable=False),
    sa.Column('length', sa.SmallInteger(), nullable=True),
    sa.Column('replacement_cost', sa.Numeric(precision=5, scale=2), server_default=sa.text('19.99'), nullable=False),
    sa.Column('rating', sa.Enum('G', 'PG', 'PG-13', 'R', 'NC-17', name='mpaa_rating'), server_default=sa.text("'G'::mpaa_rating"), nullable=True),
    sa.Column('last_update', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('special_features', sa.ARRAY(sa.Text()), nullable=True),
    sa.Column('fulltext', postgresql.TSVECTOR(), nullable=False),
    sa.ForeignKeyConstraint(['language_id'], ['language.language_id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['original_language_id'], ['language.language_id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('film_id')
    )
    op.create_index(op.f('ix_film_fulltext'), 'film', ['fulltext'], unique=False)
    op.create_index(op.f('ix_film_language_id'), 'film', ['language_id'], unique=False)
    op.create_index(op.f('ix_film_original_language_id'), 'film', ['original_language_id'], unique=False)
    op.create_index(op.f('ix_film_title'), 'film', ['title'], unique=False)
    op.create_table('film_actor',
    sa.Column('actor_id', sa.Integer(), nullable=False),
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['actor_id'], ['actor.actor_id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['film_id'], ['film.film_id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('actor_id', 'film_id')
    )
    op.create_table('film_category',
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('last_update', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.category_id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.ForeignKeyConstraint(['film_id'], ['film.film_id'], onupdate='CASCADE', ondelete='RESTRICT'),
    sa.PrimaryKeyConstraint('film_id', 'category_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('film_category')
    op.drop_table('film_actor')
    op.drop_index(op.f('ix_film_title'), table_name='film')
    op.drop_index(op.f('ix_film_original_language_id'), table_name='film')
    op.drop_index(op.f('ix_film_language_id'), table_name='film')
    op.drop_index(op.f('ix_film_fulltext'), table_name='film')
    op.drop_table('film')
    op.drop_table('language')
    op.drop_table('category')
    op.drop_index(op.f('ix_actor_last_name'), table_name='actor')
    op.drop_table('actor')
    # ### end Alembic commands ###

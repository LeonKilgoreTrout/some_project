"""Added following tables: menus, submenus, dishes

Revision ID: f1763c89f8e0
Revises: 
Create Date: 2023-01-18 03:39:52.468678

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f1763c89f8e0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table('menus',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_menus_description'), 'menus', ['description'], unique=False)
    op.create_index(op.f('ix_menus_title'), 'menus', ['title'], unique=True)
    op.create_table('submenus',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('menu_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['menu_id'], ['menus.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_submenus_description'), 'submenus', ['description'], unique=False)
    op.create_index(op.f('ix_submenus_title'), 'submenus', ['title'], unique=True)
    op.create_table('dishes',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('price', sa.String(), nullable=True),
    sa.Column('submenu_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['submenu_id'], ['submenus.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dishes_description'), 'dishes', ['description'], unique=False)
    op.create_index(op.f('ix_dishes_price'), 'dishes', ['price'], unique=False)
    op.create_index(op.f('ix_dishes_title'), 'dishes', ['title'], unique=True)


def downgrade() -> None:

    op.drop_index(op.f('ix_dishes_title'), table_name='dishes')
    op.drop_index(op.f('ix_dishes_price'), table_name='dishes')
    op.drop_index(op.f('ix_dishes_description'), table_name='dishes')
    op.drop_table('dishes')
    op.drop_index(op.f('ix_submenus_title'), table_name='submenus')
    op.drop_index(op.f('ix_submenus_description'), table_name='submenus')
    op.drop_table('submenus')
    op.drop_index(op.f('ix_menus_title'), table_name='menus')
    op.drop_index(op.f('ix_menus_description'), table_name='menus')
    op.drop_table('menus')

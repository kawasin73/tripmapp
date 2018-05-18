"""empty message

Revision ID: 88fcb422a51b
Revises: 
Create Date: 2018-05-19 01:11:07.313827

"""
from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry


# revision identifiers, used by Alembic.
revision = '88fcb422a51b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('places',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('clipped_count', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('geom', Geometry(geometry_type='POINT', srid=3857, spatial_index=True)),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clips',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('place_id', sa.String(), nullable=False),
    sa.Column('user', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['place_id'], ['places.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.UniqueConstraint('place_id', 'user', name='uix_clips_place_id_user'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clips')
    op.drop_table('places')
    # ### end Alembic commands ###

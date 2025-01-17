"""initial migration

Revision ID: 95daf945575a
Revises: 
Create Date: 2024-04-08 06:06:56.189103

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95daf945575a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False, comment='Unique identifier for the user'),
    sa.Column('username', sa.String(length=50), nullable=False, comment="User's username, must be unique"),
    sa.Column('email', sa.String(length=255), nullable=False, comment="User's email address, must be unique"),
    sa.Column('hashed_password', sa.String(length=255), nullable=False, comment="User's hashed password for security"),
    sa.Column('full_name', sa.String(length=100), nullable=True, comment="User's full name"),
    sa.Column('bio', sa.String(length=500), nullable=True, comment='Short biography or description about the user'),
    sa.Column('profile_picture_url', sa.String(length=255), nullable=True, comment="URL to the user's profile picture"),
    sa.Column('last_login_at', sa.DateTime(), nullable=True, comment="Timestamp of the user's last login"),
    sa.Column('failed_login_attempts', sa.Integer(), nullable=True, comment='Number of consecutive failed login attempts'),
    sa.Column('created_at', sa.DateTime(), nullable=False, comment='Timestamp when the user record was created'),
    sa.Column('updated_at', sa.DateTime(), nullable=False, comment='Timestamp when the user record was last updated'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###

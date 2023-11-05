from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'd0554c578304'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('users')
    op.alter_column('grades', 'grade',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('grades', 'grade_date',
               existing_type=sa.DATE(),
               nullable=True)


def downgrade() -> None:
    op.alter_column('grades', 'grade_date',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('grades', 'grade',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('age', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('phone', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.CheckConstraint('age > 18 AND age < 75', name='users_age_check'),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
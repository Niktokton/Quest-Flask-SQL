import sqlalchemy
from .db_session import SqlAlchemyBase


class result(SqlAlchemyBase):
    __tablename__ = 'results'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    timer = sqlalchemy.Column(sqlalchemy.String)

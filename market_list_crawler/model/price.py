import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Price(Base):
    __tablename__ = 'price'

    id = db.Column(db.Integer, primary_key=True)
    produto = db.Column(db.String(50), nullable=True)
    unidade = db.Column(db.String(5), nullable=True)
    maximo = db.Column(db.Numeric, nullable=True)
    frequente = db.Column(db.Numeric, nullable=True)
    minimo = db.Column(db.Numeric, nullable=True)
    data = db.Column(db.Date, nullable=False)
    origem = db.Column(db.String(25), nullable=False)
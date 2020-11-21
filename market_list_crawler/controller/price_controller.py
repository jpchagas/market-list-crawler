from ..model.price import Base, Price
from ..conf.db import DataBase
from ..utils import date_helper


class PriceController():
    def __init__(self):
        self.db = DataBase()
        self.engine, self.session = self.db.getConnection()
        Price.__table__.create(bind=self.engine, checkfirst=True)

    def getAll(self):
        '''
        TODO
        '''
        return self.session.query(Price).all()

    def getOne(self, id):
        '''
        TODO
        '''
        self.session.query(Price).filter_by(id=id)
        pass

    def insert(self, price):
        '''
        TODO
        '''
        new_price = Price(produto=price['produto'][0],
                          unidade=price['unidade'][0],
                          maximo=float(price['maximo'][0].replace(',', '.')),
                          frequente=float(price['frequente'][0].replace(',', '.')),
                          minimo=float(price['minimo'][0].replace(',', '.')),
                          data=date_helper.string_date(price['data'][0]),
                          origem=price['origem'][0])
        self.session.add(new_price)
        self.session.commit()

    def update(self):
        '''
        TODO
        '''
        pass

    def update(self):
        '''
        TODO
        '''
        pass
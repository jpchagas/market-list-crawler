from ..model.price import Base, Price
from ..conf.db import DataBase as db


class PriceController():
    def __init__(self):
        self.engine, self.session = db.getConnection()

    def getAll(self):
        '''
        TODO
        '''
        pass

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
        self.session.add(price)
        pass

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
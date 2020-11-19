import sqlalchemy as sqa
from ..model.price import Base, Price


class PriceController():
    def __init__(self):
        # self.engine = sqa.create_engine('mysql+mysqlconnector://qb9symwchjidt7m1:uu6j728z3a3x50ve@zf4nk2bcqjvif4in.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/fvjnhq96l08yqf6v', echo=True)
        self.engine = sqa.create_engine('mysql+mysqlconnector://dba:pegasos93@localhost:3306/marketlistdb', echo=True)

    def getAll(self):
        '''
        TODO
        '''
        pass

    def getOne(self):
        '''
        TODO
        '''
        pass

    def insert(self):
        '''
        TODO
        '''
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
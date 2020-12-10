from ..model.price import Price
from ..conf.db import DataBase
from ..utils import date_helper
from sqlalchemy import distinct
import json


class PriceRepository:
    def __init__(self):
        self.db = DataBase()
        self.engine, self.session = self.db.getConnection()
        Price.__table__.create(bind=self.engine, checkfirst=True)

    def get_all(self):
        '''
        TODO
        '''
        return self.session.query(Price).all()

    def get_one(self, queries):
        '''
        TODO
        '''
        q = self.session.query(Price)
        for attr, value in queries.items():
            q = q.filter(getattr(Price, attr).like("%%%s%%" % value))

        product_list = q.all()
        input_list = {}
        for i in product_list:
            input_list[i.id]= { "data":i.data.strftime("%d/%m/%Y"),
                                "frequente":float(i.frequente)}

        json_dump = json.dumps(input_list)
        json_object = json.loads(json_dump)
        return json_object


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

    def get_distinct_price(self):
        input_list = {}
        product_list = self.session.query(distinct(Price.produto)).all()
        aux_list = []
        for i in range(0, len(product_list)):
            aux_list.append(product_list[i][0])
        input_list["products"] = aux_list
        json_dump = json.dumps(input_list)
        json_object = json.loads(json_dump)

        return json_object
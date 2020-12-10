from market_list_crawler.model.price import Price
from market_list_crawler.conf.db import DataBase

db = DataBase()
engine_local, session_local = db.getConnection('mysql+mysqlconnector://dba:pegasos93@localhost:3306/marketlistdb')
engine_cloud, session_cloud = db.getConnection('mysql+mysqlconnector://solt48pli3nnfjs4:p4n3usqqol0vih7b@tj5iv8piornf713y.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/e7gividjbvo9w25z')

Price.__table__.create(bind=engine_cloud, checkfirst=True)

bulk = session_local.query(Price).all()

new_bulk = []
i = 1
for b in bulk:
    print(i)
    new_price = Price(produto=b.produto,
                      unidade=b.unidade,
                      maximo=b.maximo,
                      frequente=b.frequente,
                      minimo=b.minimo,
                      data=b.data,
                      origem=b.origem)
    session_cloud.add(new_price)
    session_cloud.commit()
    i+=1
    #new_bulk.append(new_price)

#session_cloud.add_all(new_bulk)
#session_cloud.commit()


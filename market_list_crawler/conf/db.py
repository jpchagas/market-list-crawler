import sqlalchemy as sqa


class DataBase:
    def __init__(self):
        pass

    def getConnection(self):
        #engine = sqa.create_engine('mysql+mysqlconnector://solt48pli3nnfjs4:p4n3usqqol0vih7b@tj5iv8piornf713y.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/e7gividjbvo9w25z')
        engine = sqa.create_engine('mysql+mysqlconnector://dba:pegasos93@localhost:3306/marketlistdb')
        # Create a session
        Session = sqa.orm.sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        return engine, session

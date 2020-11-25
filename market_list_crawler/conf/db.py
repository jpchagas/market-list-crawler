import sqlalchemy as sqa

class DataBase():
    def __init__(self):
        pass

    def getConnection(self):
        engine = sqa.create_engine('mysql+mysqlconnector://qb9symwchjidt7m1:uu6j728z3a3x50ve@zf4nk2bcqjvif4in.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/fvjnhq96l08yqf6v')
        #engine = sqa.create_engine('mysql+mysqlconnector://dba:pegasos93@localhost:3306/marketlistdb')
        # Create a session
        Session = sqa.orm.sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        return engine, session
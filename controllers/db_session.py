from controllers.database_setup import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///alquiler_bd.db', echo=True, connect_args={"check_same_thread": False})

class DBSession():

    Base.metadata.bind = engine
    DBSession = sessionmaker(bind = engine)

    def get_session(self):
        session = self.DBSession()
        return session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:///alquiler_bd.db',
    echo=True,
    connect_args={"check_same_thread": False})


class DBSession:

    def __init__(self) -> None:
        self.db_session = sessionmaker(bind=engine)

    def get_session(self):
        session = self.db_session()
        return session

from controllers.database_setup import Base, Client, Checkout, Checkout_detail

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///alquiler_bd.db', echo=True, connect_args={"check_same_thread": False})

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()


def show_checkouts_tb():
    checkouts = session.query(Checkout).all()
    return checkouts

def get_checkout_by_id_tb(id):
    checkout = session.query(Checkout).filter_by(id = id).one()
    return checkout

def new_checkout_tb(id, total, client_id, user_id, date):
    new_checkout = Checkout(id = id, total = total, client_id = client_id, user_id = user_id, date = date)
    session.add(new_checkout)
    session.commit()
    session.close()
    return True

def edit_checkout_details_tb(checkeouts):
    checkeouts
    return True




def edit_checkouts_tb(checkout):
    checkout = session

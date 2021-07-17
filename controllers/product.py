from controllers.database_setup import Base, Product, Category

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///alquiler_bd.db', echo=True, connect_args={"check_same_thread": False})

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

def show_products_tb():
    products = session.query(Product).all()
    return products

def new_product_tb(name, description, code, stock, c_stock, price, category_id, state):
    new_product = Product(name = name, description = description, code = code, current_stock = c_stock, stock = stock, price = price, category_id = category_id, state = state )
    session.add(new_product)
    session.commit()
    session.close()
    return True

def get_product_by_id_tb(id):
    product = session.query(Product).filter_by(id = id).one()
    return product

def edit_product_tb(product):
    session.add(product)
    session.commit()
    session.close()
    return True

def delete_product_tb(id):
    product = get_product_by_id_tb(id)
    session.delete(product)
    session.commit()
    session.close()
    return True
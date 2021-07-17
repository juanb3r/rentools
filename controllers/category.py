from controllers.database_setup import Base, Category

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///alquiler_bd.db', echo=True, connect_args={"check_same_thread": False})

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

def show_categories_tb():
    categories = session.query(Category).all()
    return categories

def get_category_by_id_tb(id):
    category = session.query(Category).filter_by(id = id).one()
    return category

def new_category_tb(name, description, state):
    new_category = Category(name = name, description = description, state = state)
    session.add(new_category)
    session.commit()
    session.close()
    return True

def edit_category_tb(category):
    session.add(category)
    session.commit()
    session.close()
    return True

def delete_category_tb(id):
    category = get_category_by_id_tb(id)
    session.delete(category)
    session.commit()
    session.close()
    return True
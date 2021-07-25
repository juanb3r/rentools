import sys, datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()


def _get_date():
    return datetime.datetime.now()


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    state = Column(Boolean)


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    code = Column(String(250), nullable=False)
    description = Column(String(250))
    stock = Column(Integer)
    current_stock = Column(Integer)
    price = Column(Integer)
    category_id = Column(Integer, ForeignKey('category.id'))
    state = Column(Boolean)
    date = Column(Date, default=_get_date)
    category = relationship(Category)


class Rol(Base):
    __tablename__ = 'rol'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    state = Column(Boolean)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    document = Column(String(25))
    phone = Column(String(15))
    email = Column(String(50))
    password = Column(String(50))
    adress = Column(String(250))
    rol_id = Column(Integer, ForeignKey('rol.id'))
    state = Column(Boolean)
    date = Column(Date, default=_get_date)
    rol = relationship(Rol)


class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    document = Column(String(25), nullable=False)
    phone = Column(String(15))
    email = Column(String(50))
    adress = Column(String(250))
    date = Column(Date, default=_get_date)


class Checkout(Base):
    __tablename__ = 'checkout'
    id = Column(Integer, primary_key=True)
    total = Column(Integer)
    client_id = Column(Integer, ForeignKey('client.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    date = Column(Date, default=_get_date)
    client = relationship(Client)
    user = relationship(User)


class Checkin(Base):
    __tablename__ = 'checkin'
    id = Column(Integer, primary_key=True)
    total = Column(Integer)
    client_id = Column(Integer, ForeignKey('client.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    checkout_id = Column(Integer, ForeignKey('checkout.id'))
    date = Column(Date, default=_get_date)
    client = relationship(Client)
    user = relationship(User)
    checkout = relationship(Checkout)


class Checkout_detail(Base):
    __tablename__ = 'checkout_detail'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    quantity_in = Column(Integer)
    checkout_id = Column(Integer, ForeignKey('checkout.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    price = Column(Integer)
    day = Column(Integer)
    date = Column(Date, default=_get_date)
    checkout = relationship(Checkout)
    product = relationship(Product)


class Checkin_detail(Base):
    __tablename__ = 'checkin_detail'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    checkin_id = Column(Integer, ForeignKey('checkin.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    price = Column(Integer)
    day = Column(Integer)
    date = Column(Date, default=_get_date)
    checkin = relationship(Checkin)
    product = relationship(Product)


# Engine = \
#   create_engine('mysql://jeltexbdUser:juan123..@localhost:3308/alquiler_bd')
# engine = create_engine("sqlite:///alquiler_bd.db")
# Base.metadata.create_all(engine)

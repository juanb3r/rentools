from controllers.database_setup import Product
from controllers.db_session import DBSession


session = DBSession()
session = session.get_session()


def show_products_tb() -> Product:
    products = session.query(Product).all()
    return products


def new_product_tb(
        name: str,
        description: str,
        code: str,
        stock: int,
        c_stock,
        price,
        category_id,
        state) -> bool:
    new_product = Product(
        name=name,
        description=description,
                          code=code, current_stock=c_stock, stock=stock,
                          price=price, category_id=category_id, state=state)
    session.add(new_product)
    session.commit()
    session.close()
    return True


def get_product_by_id_tb(id):
    product = session.query(Product).filter_by(id=id).one()
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

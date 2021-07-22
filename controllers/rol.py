from controllers.database_setup import Rol
from controllers.db_session import DBSession

session = DBSession()
session = session.get_session()


def show_roles_tb():
    roles = session.query(Rol).all()
    return roles


def get_rol_by_id(id):
    rol = session.query(Rol).filter_by(id=id).one()
    return rol


def new_rol_tb(name, description, state):
    new_rol = Rol(name=name, description=description, state=state)
    session.add(new_rol)
    session.commit()
    session.close()
    return True


def edit_rol_tb(rol):
    session.add(rol)
    session.commit()
    session.close()
    return True


def delete_rol_tb(id):
    rol = get_rol_by_id(id)
    session.delete(rol)
    session.commit()
    session.close()
    return True

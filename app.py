from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/inicio')
def home():
    return 'Inicio'


#CATEGORIES ROUTES
@app.route('/categorias')
def show_categories():
    return 'Categorias'

@app.route('/categorias/nuevo')
def new_category():
    return 'Crear nueva categoria'

@app.route('/categorias/<int:categoria_id>/editar')
def edit_category(categoria_id):
    return f'Editar categoria {categoria_id}'

@app.route('/categorias/<int:categoria_id>/eliminar')
def delete_category(categoria_id):
    return f'Eliminar categoria {categoria_id}'

#PRODUCTS ROUTES
@app.route('/productos')
def show_products():
    return 'Productos'

@app.route('/productos/nuevo')
def new_product():
    return 'Crear producto'

@app.route('/productos/<int:producto_id>/editar')
def edit_product(producto_id):
    return f'Editar producto {producto_id}'

@app.route('/productos/<int:producto_id>/eliminar')
def delete_product(producto_id):
    return f'Eliminar producto {producto_id}'

#CHECKOUTS ROUTES
@app.route('/salidas')
def show_checkouts():
    return 'Salidas'

@app.route('/salidas/nuevo')
def new_checkout():
    return 'Crear salida'

@app.route('/salidas/<int:salida_id>/detalles')
def show_checkout_details(salida_id):
    return f'Editar salida {salida_id}'

@app.route('/salidas/<int:salida_id>/editar')
def edit_checkout(salida_id):
    return f'Editar salida {salida_id}'

@app.route('/productos/<int:salida_id>/eliminar')
def delete_checkout(salida_id):
    return f'Eliminar salida {salida_id}'


#CHECKINS ROUTES
@app.route('/entradas')
def show_checkins():
    return 'Entradas'

@app.route('/entradas/nuevo')
def new_checkin():
    return 'Crear entrada'

@app.route('/entradas/<int:entrada_id>/detalles')
def show_checkin_details(entrada_id):
    return f'Editar entrada {entrada_id}'

@app.route('/entradas/<int:entrada_id>/editar')
def edit_checkin(entrada_id):
    return f'Editar entrada {entrada_id}'

@app.route('/entradas/<int:entrada_id>/eliminar')
def delete_checkin(entrada_id):
    return f'Eliminar entrada {entrada_id}'

#CLIENTS ROUTES
@app.route('/clientes')
def show_clients():
    return 'Clientes'

@app.route('/clientes/nuevo')
def new_client():
    return 'Crear cliente'

@app.route('/clientes/<int:clientes_id>/editar')
def edit_client(clientes_id):
    return f'Editar cliente {clientes_id}'

@app.route('/clientes/<int:clientes_id>/eliminar')
def delete_client(clientes_id):
    return f'Eliminar clientes {clientes_id}'

#USERS ROUTES
@app.route('/usuarios')
def show_users():
    return 'Usuarios'

@app.route('/usuarios/nuevo')
def new_user():
    return 'Crear usuario'

@app.route('/usuarios/<int:usuario_id>/editar')
def edit_user(usuario_id):
    return f'Editar usuario {usuario_id}'

@app.route('/usuarios/<int:usuario_id>/eliminar')
def delete_user(usuario_id):
    return f'Eliminar usuario {usuario_id}'

#ROLES ROUTES
@app.route('/roles')
def show_roles():
    return 'Roles'

@app.route('/roles/nuevo')
def new_rol():
    return 'Crear rol'

@app.route('/roles/<int:roles_id>/editar')
def edit_rol(roles_id):
    return f'Editar rol {roles_id}'

@app.route('/roles/<int:roles_id>/eliminar')
def delete_rol(roles_id):
    return f'Eliminar rol {roles_id}'



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port = 9001)
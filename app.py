from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/inicio')
def home():
    return render_template('home.html')


#CATEGORIES ROUTES
@app.route('/categorias')
@app.route('/categorias/')
def show_categories():
    return render_template('categories/categories.html')

@app.route('/categorias/nuevo')
def new_category():
    return render_template('categories/new_category.html')

@app.route('/categorias/<int:categoria_id>/editar')
def edit_category(categoria_id):
    return render_template('categories/edit_category.html', categoria_id = categoria_id)

@app.route('/categorias/<int:categoria_id>/eliminar')
def delete_category(categoria_id):
    return f'Eliminar categoria {categoria_id}'

#PRODUCTS ROUTES
@app.route('/productos')
@app.route('/productos/')
def show_products():
    return render_template('products/products.html')

@app.route('/productos/nuevo')
def new_product():
    return render_template('products/new_product.html')

@app.route('/productos/<int:producto_id>/editar')
def edit_product(producto_id):
    return render_template('products/edit_product.html', producto_id = producto_id)

@app.route('/productos/<int:producto_id>/eliminar')
def delete_product(producto_id):
    return f'Eliminar producto {producto_id}'

#CHECKOUTS ROUTES
@app.route('/salidas')
@app.route('/salidas/')
def show_checkouts():
    return render_template('checkouts/checkouts.html')


@app.route('/salidas/nuevo')
def new_checkout():
    return render_template('checkouts/new_checkout.html')

@app.route('/salidas/<int:salida_id>/detalles')
def show_checkout_details(salida_id):
    return render_template('checkouts/detailed_checkout.html', salida_id = salida_id)

@app.route('/salidas/<int:salida_id>/editar')
def edit_checkout(salida_id):
    return render_template('checkouts/edit_checkout.html')

@app.route('/productos/<int:salida_id>/eliminar')
def delete_checkout(salida_id):
    return f'Eliminar salida {salida_id}'


#CHECKINS ROUTES
@app.route('/entradas')
@app.route('/entradas/')
def show_checkins():
    return render_template('checkins/checkins.html')


@app.route('/entradas/nuevo')
def new_checkin():
    return render_template('checkins/new_checkin.html')

@app.route('/entradas/<int:entrada_id>/detalles')
def show_checkin_details(entrada_id):
    return render_template('checkins/detailed_checkin.html', entrada_id = entrada_id)

@app.route('/entradas/<int:entrada_id>/editar')
def edit_checkin(entrada_id):
    return render_template('checkins/edit_checkin.html')

@app.route('/entradas/<int:entrada_id>/eliminar')
def delete_checkin(entrada_id):
    return f'Eliminar entrada {entrada_id}'

#CLIENTS ROUTES
@app.route('/clientes')
@app.route('/clientes/')
def show_clients():
    return render_template('clients/clients.html')


@app.route('/clientes/nuevo')
def new_client():
    return render_template('clients/new_client.html')

@app.route('/clientes/<int:cliente_id>/editar')
def edit_client(cliente_id):
    return render_template('clients/edit_client.html', cliente_id = cliente_id)

@app.route('/clientes/<int:cliente_id>/eliminar')
def delete_client(cliente_id):
    return f'Eliminar clientes {cliente_id}'

#USERS ROUTES
@app.route('/usuarios')
@app.route('/usuarios/')
def show_users():
    return render_template('users/users.html')


@app.route('/usuarios/nuevo')
def new_user():
    return render_template('users/new_user.html')

@app.route('/usuarios/<int:usuario_id>/editar')
def edit_user(usuario_id):
    return render_template('users/edit_user.html', usuario_id)

@app.route('/usuarios/<int:usuario_id>/eliminar')
def delete_user(usuario_id):
    return f'Eliminar usuario {usuario_id}'

#ROLES ROUTES
@app.route('/roles')
@app.route('/roles/')
def show_roles():
    return render_template('roles/roles.html')


@app.route('/roles/nuevo')
def new_rol():
    return render_template('roles/new_rol.html')

@app.route('/roles/<int:roles_id>/editar')
def edit_rol(roles_id):
    return render_template('roles/edit_rol.html', roles_id = roles_id)

@app.route('/roles/<int:roles_id>/eliminar')
def delete_rol(roles_id):
    return f'Eliminar rol {roles_id}'



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port = 9001)
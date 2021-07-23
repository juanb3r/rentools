from flask import Flask, render_template, request, redirect, url_for, flash
import controllers.category as ctb
import controllers.product as ptb
import controllers.check_fields as chf
import controllers.rol as rtb

from controllers.form_checker import RegistrationForm

app = Flask(__name__)


def page_not_found(e):
    return render_template('404.html'), 404


app.register_error_handler(404, page_not_found)


@app.route('/')
@app.route('/inicio')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # user = User(form.username.data, form.email.data,
        #             form.password.data)
        # db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('show_categories'))
    return render_template('register.html', form=form)


# CATEGORIES ROUTES
@app.route('/categorias')
@app.route('/categorias/')
def show_categories():
    categories = ctb.show_categories_tb()
    return render_template(
            'categories/categories.html',
            categories=categories)


@app.route('/categorias/nuevo', methods=['GET', 'POST'])
def new_category():
    if request.method == 'POST':
        name = request.form['newNameCatText'].upper()
        description = request.form['newDescriptionCatText'].upper()
        state = request.form['newStateCatSelect']

        check = chf.check_fields(state, name, description)

        if check['status']:
            result = ctb.new_category_tb(name, description, check['state'])
            if result:
                flash('Nueva categoría creada')
                render = redirect(url_for('show_categories'))
            else:
                flash('No se pudo crear categoría')
                render = render_template('categories/new_category.html')
        else:
            flash(check['msg'])
            render = render_template('categories/new_category.html')
    else:
        render = render_template('categories/new_category.html')

    return render


@app.route('/categorias/<int:categoria_id>/editar', methods=['GET', 'POST'])
def edit_category(categoria_id):
    category = ctb.get_category_by_id_tb(categoria_id)

    if request.method == 'POST':
        name = request.form['editNameCatText'].upper()
        description = request.form['editDescriptionCatText'].upper()
        state = request.form['editStateCatSelect']
        check = chf.check_fields(state, name, description)

        if check['status']:
            category.name = name
            category.description = description
            category.state = check['state']
            result = ctb.edit_category_tb(category)
            if result:
                flash('Categoría editada con éxito')
                render = redirect(url_for('show_categories'))
            else:
                flash('No se pudo editar categoría')
                render = render_template(
                            'categories/edit_category.html',
                            categoria_id=categoria_id)
        else:
            flash(check['msg'])
            render = redirect(url_for(
                            'edit_category', categoria_id=categoria_id))
    else:
        render = render_template(
                        'categories/edit_category.html',
                        categoria_id=categoria_id, category=category)

    return render


@app.route('/categorias/<int:categoria_id>/eliminar', methods=['GET', 'POST'])
def delete_category(categoria_id):
    if request.method == 'POST':
        result = ctb.delete_category_tb(categoria_id)
        if result:
            flash('Categoría eliminada')
            render = redirect(url_for('show_categories'))
        else:
            flash('No se pudo eliminar categoría')
            render = redirect(url_for('show_categories'))

        return render


# PRODUCTS ROUTES
@app.route('/productos')
@app.route('/productos/')
def show_products():
    products = ptb.show_products_tb()
    return render_template('products/products.html', products=products)


@app.route('/productos/nuevo', methods=['GET', 'POST'])
def new_product():
    categories = ctb.show_categories_tb()
    if request.method == 'POST':
        name = request.form['newNameProductText'].upper()
        description = request.form['newDescriptionProductText'].upper()
        code = request.form['newCodeProductText'].upper()
        stock = request.form['newStockProductText']
        c_stock = request.form['newCurrentStockProductText']
        price = request.form['newPriceProductText']
        category_id = request.form['newCatProductSelect']
        state = request.form['newStateProductSelect']
        check = chf.check_product(
            name, description, code, stock, c_stock, price, category_id, state)
        if check['status']:
            result = ptb.new_product_tb(
                                    name, description, code, stock, c_stock,
                                    price, check['cat_id'], check['state'])
            if result:
                flash('Producto creado')
                render = redirect(url_for('show_products'))
            else:
                flash('No se pudo crear producto')
                render = render_template(
                            'products/new_product.html', categories=categories)
        else:
            flash(check['msg'])
            render = redirect(url_for('new_product'))

    else:
        render = render_template(
                        'products/new_product.html', categories=categories)

    return render


@app.route('/productos/<int:producto_id>/editar', methods=['GET', 'POST'])
def edit_product(producto_id):
    categories = ctb.show_categories_tb()
    product = ptb.get_product_by_id_tb(producto_id)
    if request.method == 'POST':
        name = request.form['editNameProductText'].upper()
        description = request.form['editDescriptionProductText'].upper()
        code = request.form['editCodeProductText'].upper()
        stock = request.form['editStockProductText']
        c_stock = request.form['editCurrentStockProductText']
        price = request.form['editPriceProductText']
        category_id = request.form['editCatProductSelect']
        state = request.form['editStateProductSelect']
        check = chf.check_product(
            name, description, code, stock, c_stock, price, category_id, state)

        if check['status']:
            product.name = name
            product.description = description
            product.code = code
            product.stock = check['stock']
            product.current_stock = check['c_stock']
            product.price = check['price']
            product.category_id = check['cat_id']
            product.state = check['state']
            result = ptb.edit_product_tb(product)
            if result:
                flash('Producto editado correctamente')
                render = redirect(url_for('show_products'))
            else:
                flash('No se pudo editar producto')
                render = render_template(
                        'products/edit_product.html', producto_id=producto_id,
                        product=product, categories=categories)
        else:
            flash(check['msg'])
            render = redirect(url_for('show_products'))

    else:
        render = render_template(
                        'products/edit_product.html', producto_id=producto_id,
                        product=product, categories=categories)

    return render


@app.route('/productos/<int:producto_id>/eliminar', methods=['GET', 'POST'])
def delete_product(producto_id):
    if request.method == 'POST':
        result = ptb.delete_product_tb(producto_id)
        if result:
            flash('Producto eliminado')
            render = redirect(url_for('show_products'))
        else:
            flash('No se pudo eliminar producto')
            render = redirect(url_for('show_products'))

        return render


# #CHECKOUTS ROUTES
# @app.route('/salidas')
# @app.route('/salidas/')
# def show_checkouts():
#     return render_template('checkouts/checkouts.html')


# @app.route('/salidas/nuevo')
# def new_checkout():
#     return render_template('checkouts/new_checkout.html')

# @app.route('/salidas/<int:salida_id>/detalles')
# def show_checkout_details(salida_id):
#     return render_template('checkouts/detailed_checkout.html', salida_id = salida_id)

# @app.route('/salidas/<int:salida_id>/editar')
# def edit_checkout(salida_id):
#     return render_template('checkouts/edit_checkout.html')

# @app.route('/productos/<int:salida_id>/eliminar')
# def delete_checkout(salida_id):
#     return f'Eliminar salida {salida_id}'


# #CHECKINS ROUTES
# @app.route('/entradas')
# @app.route('/entradas/')
# def show_checkins():
#     return render_template('checkins/checkins.html')


# @app.route('/entradas/nuevo')
# def new_checkin():
#     return render_template('checkins/new_checkin.html')

# @app.route('/entradas/<int:entrada_id>/detalles')
# def show_checkin_details(entrada_id):
#     return render_template('checkins/detailed_checkin.html', entrada_id = entrada_id)

# @app.route('/entradas/<int:entrada_id>/editar')
# def edit_checkin(entrada_id):
#     return render_template('checkins/edit_checkin.html')

# @app.route('/entradas/<int:entrada_id>/eliminar')
# def delete_checkin(entrada_id):
#     return f'Eliminar entrada {entrada_id}'

# #CLIENTS ROUTES
# @app.route('/clientes')
# @app.route('/clientes/')
# def show_clients():
#     return render_template('clients/clients.html')


# @app.route('/clientes/nuevo')
# def new_client():
#     return render_template('clients/new_client.html')

# @app.route('/clientes/<int:cliente_id>/editar')
# def edit_client(cliente_id):
#     return render_template('clients/edit_client.html', cliente_id = cliente_id)

# @app.route('/clientes/<int:cliente_id>/eliminar')
# def delete_client(cliente_id):
#     return f'Eliminar clientes {cliente_id}'

# USERS ROUTES
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


# ROLES ROUTES
@app.route('/roles')
@app.route('/roles/')
def show_roles():
    roles = rtb.show_roles_tb()
    return render_template('roles/roles.html', roles=roles)


@app.route('/roles/nuevo', methods=['GET', 'POST'])
def new_rol():
    if request.method == 'POST':
        name = request.form['newNameRolText'].upper()
        description = request.form['newDescriptionRolText'].upper()
        state = request.form['newStateRolSelect']

        check = chf.check_fields(state, name, description)

        if check['status']:
            result = rtb.new_rol_tb(name, description, check['state'])
            if result:
                flash('Nuevo rol creado')
                render = redirect(url_for('show_roles'))
            else:
                flash('No se pudo crear rol')
                render = render_template('roles/new_rol.html')
        else:
            flash(check['msg'])
            render = redirect(url_for('show_roles'))
    else:
        render = render_template('roles/new_rol.html')

    return render


@app.route('/roles/<int:rol_id>/editar' ,methods=['GET', 'POST'])
def edit_rol(rol_id):
    rol = rtb.get_rol_by_id(rol_id)
    if request.method == 'POST':
        name = request.form['editNameRolText'].upper()
        description = request.form['editDescriptionRolText'].upper()
        state = request.form['editStateRolSelect']

        check = chf.check_fields(state, name, description)

        if check['status']:
            rol.name = name
            rol.description = description
            rol.state = check['state']
            result = rtb.edit_rol_tb(rol)
            if result:
                flash('Rol editado con éxito')
                render = redirect(url_for('show_roles'))
            else:
                flash('No se pudo editar rol')
                render = redirect(url_for('edit_rol', rol_id=rol_id))
        else:
            flash(check['msg'])
            render = redirect(url_for('edit_rol', rol_id=rol_id))

    else:
        render = render_template('roles/edit_rol.html', rol_id=rol_id, rol=rol)

    return render


@app.route('/roles/<int:rol_id>/eliminar', methods=['GET', 'POST'])
def delete_rol(rol_id):
    if request.method == 'POST':
        result = rtb.delete_rol_tb(rol_id)
        if result:
            flash('Rol eliminado')
            render = redirect(url_for('show_roles'))
        else:
            flash('No se pudo eliminar rol')
            render = redirect(url_for('show_roles'))

        return render


if __name__ == '__main__':
    app.secret_key = 'Super-secret-key'
    app.debug = True
    app.run(host='0.0.0.0', port=9001)
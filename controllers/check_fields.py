def check_fields(state, name, desc):
    check = {}
    try:
        check['state'] = int(state)
        if check['state'] < 2:
            if name and desc:
                check['status'] = True
                check['msg'] = ''
            else:
                check['status'] = False
                check['msg'] = 'Al menos uno de los campos de texto está vacío'
        else:
            check['status'] = False
            check['msg'] = 'Estado fuera de rango, no corresponde a un valor aceptado'
    except ValueError:
        check['status'] = False
        check['msg'] = 'Estado de categoría inválido, no es un número'

    return check


def check_product(name, desc, code, stock, c_stock, price, cat_id, state):
    check = {}
    try:
        check['state'] = int(state)
        check['cat_id'] = int(cat_id)
        check['price'] = int(price)
        check['stock'] = int(stock)
        check['c_stock'] = int(c_stock)

        if check['state'] < 2:
            if name and desc and code:
                check['status'] = True
                check['msg'] = 'Testeado'
            else:
                check['status'] = False
                check['msg'] = 'Al menos uno de los campos de texto está vacío'

    except ValueError:
        check['status'] = False
        status = True
        while status:
            if not check.get('state'):
                check['msg'] = 'Dato inválido, el estado no es un número'
                status = False
            elif not check.get('cat_id'):
                check['msg'] = 'Dato inválido, la categoría no es un número'
                status = False
            elif not check.get('price'):
                check['msg'] = 'Dato inválido, el precio no es un número'
                status = False
            elif not check.get('stock'):
                check['msg'] = 'Dato inválido, la cantidad no es un número'
                status = False
            elif not check.get('c_stock'):
                check['msg'] = 'Dato inválid,la cantidad en bodeg no es un num'
                status = False

    return check

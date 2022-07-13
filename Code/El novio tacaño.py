def producto_mas_barato(catalogo:dict)->str:

    maximo = 0

    productos = []

    for i in catalogo.values():
        if int(i) > maximo:
            maximo = i

    menor = maximo

    for l in catalogo.values():
        if int(l) < menor:
            menor = l

    if menor > 10000:
        productos = None

    elif catalogo == {}:
        productos =  "No hay productos para escoger"

    else:

        for y in catalogo:
            if catalogo[y] == menor:
                productos.append(y)

        productos = sorted(productos)
        productos = productos[0]

    return productos
def comprar_jugador(jugadores:list, monedas:int)->str:

    # Inicializacion de variables
    posibles_jugadores = []
    precios = []
    jugador = ""
    prueba_precio = []
    media_max = []

    # Busqueda de precios maximos y minimos
    for i in jugadores:
        prueba_precio.append(i["precio"])
    precio_minimo = min(prueba_precio)
    precio_maximo = max(prueba_precio)

    #Verififacion de que si se puedan comprar jugadores
    if precio_minimo < monedas:

        # Recoleccion de los jugadores que se puedan pagar
        for i in jugadores:
            if i["precio"] <= monedas:
                posibles_jugadores.append(i["nombre"])

        for i in jugadores:

            # Busqueda de precio minimo
            if i["nombre"] in posibles_jugadores:
                precios.append(i["precio"])

            # Busqueda de media maxima
            if i["nombre"] in posibles_jugadores:
                media_max.append(i["media"])

        precio_minimo = min(precios)
        media_max = max(media_max)

        # Formateo de variable para rehuso
        posibles_jugadores = []

        # Busqueda de jugadores con la media maxima
        for i in jugadores:
            if i["media"] == media_max:
                posibles_jugadores.append(i["nombre"])

        # Declaracion de variable
        diferencia_precio = precio_maximo

        # Busqueda del jugador con las siguientes condiciones: que se pueda pagar, que el precio sea el mas bajo y que la media sea la mas alta.
        for i in jugadores:
            if i["nombre"] in posibles_jugadores and ((i["precio"]) - precio_minimo) < diferencia_precio:
                diferencia_precio= i["precio"] - precio_minimo
                jugador = i["nombre"]

    else:
        jugador = None

    return jugador
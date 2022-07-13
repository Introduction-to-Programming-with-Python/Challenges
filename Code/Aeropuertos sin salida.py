def listar_aeropuertos_sin_salida(vuelos:dict)->list:
  
    salieron_de = []
    no_salieron_de = []

    for i in vuelos:
        origen = vuelos[i]["origen"]
        salieron_de.append(origen)

    for i in vuelos:
        oriigen = vuelos[i]["destino"]
        if oriigen not in salieron_de:
            no_salieron_de.append(oriigen)

    sin_repetidos = []

    for r in no_salieron_de:
        if r not in sin_repetidos:
            sin_repetidos.append(r)

    return sin_repetidos
def letra_mas_comun(cadena:str)->str:

    cadena = cadena.replace(".","")
    cadena = cadena.replace(" ","")
    cadena = cadena.replace(",","")
    cadena = cadena.lower()

    datos = {}

    for i in cadena:
        if i not in datos:
            datos[i] = 1
        if i in datos and datos[i]>0:
            datos[i] += 1

    maximo = list(datos.values())
    maximo = max(maximo)

    llaves = list(datos.keys())

    for i in llaves:
        if datos[i] < maximo:
            del datos[i]

    datos = list(datos.keys())

    abecedario = list("abcdefghijklmnopqrstuvwxyz")
    avance = 0

    frecuente = None

    while avance <= (len(datos)-1):
        for i in abecedario:
            if i == datos[avance]:
               frecuente = datos[avance]
        avance += 1


    return frecuente.upper()
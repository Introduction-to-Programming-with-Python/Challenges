def conversion(tiempo:int)->int:

    horas = tiempo // 100
    minutos = tiempo - horas*100

    return minutos + horas*60

def buscar_vuelos_escala(vuelos:dict, origen:str, destino:str)->list:

    # Vuelos directos
    vuelos_directos = {}

    # Vuelos con el mismo destino
    segundo_vuelo_escala = {}

    # Lista de origenes de los vuelos de escala
    origenes_segundos_vuelos = []

    # Primeros vuelos que se podrian tomar para hacer escala
    primer_vuelo_escala = {}

    # Retorno
    lista = []
    vuelos_finales = []

    for i in vuelos:
        dic_vuelo = vuelos[i]
        dic_vuelo_destino = dic_vuelo["destino"]
        if dic_vuelo_destino == destino:
            segundo_vuelo_escala[i] = dic_vuelo

    for i in segundo_vuelo_escala:
        dic_vuelo = vuelos[i]
        dic_vuelo_origen = dic_vuelo["origen"]
        if dic_vuelo_origen == origen:
            vuelos_directos[i] = dic_vuelo

    for i in segundo_vuelo_escala:
        dic_vuelo = vuelos[i]
        dic_vuelo_origen = dic_vuelo["origen"]
        origenes_segundos_vuelos.append(dic_vuelo_origen)

    for i in vuelos:
        vuello = vuelos[i]
        oriigen = vuello["origen"]
        destiino = vuello["destino"]
        if oriigen == origen and destiino in origenes_segundos_vuelos:
            primer_vuelo_escala[i] = vuello
    
    for i in vuelos_directos.keys():
        lista.append(i)
        vuelos_finales.append(lista)
        lista = []

    for i in primer_vuelo_escala:
        dic_vuelo_origen = primer_vuelo_escala[i]
        dic_vuelo_origen_destino = dic_vuelo_origen["destino"]
        salida_origen = conversion(int(dic_vuelo_origen["salida"]))
        duracion_origen = int(dic_vuelo_origen["duracion"]) + int(dic_vuelo_origen["retraso"])
        llegada_origen = salida_origen + duracion_origen

        for l in segundo_vuelo_escala:
            dic_vuelo_escala = segundo_vuelo_escala[l]
            dic_vuelo_escala_origen = dic_vuelo_escala["origen"]
            salida_escala = conversion(int(dic_vuelo_escala["salida"]))

            if dic_vuelo_escala_origen == dic_vuelo_origen_destino and llegada_origen < salida_escala:
                lista = [i, l]
                vuelos_finales.append(lista)
                lista = []

    return vuelos_finales
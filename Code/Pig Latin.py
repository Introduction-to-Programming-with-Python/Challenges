def traducir_a_pig_latin(texto:str)->str:

    texto = texto.split()

    consonantes = "bcdfghjklmnpqrstvwxyz"
    vocales = "aeiou"
    traduccion = ""
    conteo = 0
    lista = []
    eliminadas = ""

    for i in texto:
        palabra = i
        for l in palabra:
            if l in vocales:
                conteo += 1
        if conteo == 0:
            lista.append(palabra)

    for i in texto:
        palabra = i
        if palabra in lista:
            traduccion += palabra+" "
        elif palabra[0] in consonantes:
            while palabra[0] in consonantes:
                eliminadas += palabra[0]
                palabra = palabra.lstrip(palabra[0])
            palabra = palabra+eliminadas+"ay "
            eliminadas = ""
            traduccion += palabra
        elif palabra[0] in vocales:
            palabra = palabra+"way "
            traduccion += palabra
        else:
            traduccion += palabra+" "

    traduccion = traduccion[0:-1] 

    return traduccion
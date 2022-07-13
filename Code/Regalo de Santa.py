def clasificar_regalo(id:int)->bool:

    #Palindromo

    id_1 = id // 100
    id_2 = id % 10

    #Impar

    sobrante=int(id)%2

    if id_1==id_2 and sobrante!=0:
        respuesta="girl"

    elif id_1==id_2 and sobrante==0:
        respuesta = "boy"

    elif id_1!=id_2 and sobrante==0:
        respuesta = "man"

    elif id_1!=id_2 and sobrante!=0:
        respuesta = "woman"

    return respuesta
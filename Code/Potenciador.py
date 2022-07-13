def potenciador(x: int, n:int) -> bool:

    if n==1 or n<=0:
        respuesta = False

    else:

        x = x**(1/n)
        redondeado = round(x)
        resta = x - redondeado

        if resta == 0:
            respuesta = True

        else: 
            respuesta = False

    return respuesta
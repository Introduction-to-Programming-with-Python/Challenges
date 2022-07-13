def verificar_nit(NIT:int, digito:int)->bool:

    #Descomposicion del numero

    NIT1 = NIT % 10
    NIT = NIT // 10
    NIT2 = NIT % 10
    NIT = NIT // 10
    NIT3 = NIT % 10
    NIT = NIT // 10
    NIT4 = NIT % 10
    NIT = NIT // 10
    NIT5 = NIT % 10
    NIT = NIT // 10
    NIT6 = NIT % 10
    NIT = NIT // 10
    NIT7 = NIT % 10
    NIT = NIT // 10
    NIT8 = NIT % 10
    NIT = NIT // 10
    #NIT=int(str(NIT) + str(NIT8) + str(NIT7) + str(NIT6) + str(NIT5) + str(NIT4) + str(NIT3) + str(NIT2) + str(NIT1))

    #Calculo del digito de verificacion

    NITc=NIT*41
    NIT8c=NIT8*37
    NIT7c=NIT7*29
    NIT6c=NIT6*23
    NIT5c=NIT5*19
    NIT4c=NIT4*17
    NIT3c=NIT3*13
    NIT2c=NIT2*7
    NIT1c=NIT1*3

    suma=NIT8c+NIT7c+NIT6c+NIT5c+NIT4c+NIT3c+NIT2c+NIT1c+NITc
    codigo=suma%11
    alternativa=11-codigo

    if codigo==0 or codigo==1:
        codigo=codigo
    else:
        codigo=alternativa

    if codigo==digito:
        respuesta=True
    else:
        respuesta =False

    return respuesta
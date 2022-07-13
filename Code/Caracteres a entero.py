def caracteres_a_entero(centenas: str, decenas: str, unidades: str)->int:
    """ Caracteres a entero
    Parámetros:
      centenas (str): Caracter que denota las centenas del número a formar
      decenas (str): Caracter que denota las decenas del número a formar
      unidades (str): Caracter que denota las unidades del número a formar
    Retorno:
      int: Número entero formado por los caracteres recibidos como parámetro
    """
    
    numero_cadena = centenas + decenas + unidades
    numero = int(numero_cadena)
    
    return numero
def sucesion_fibonacci(iteraciones:int):

    contador = 1
    numero = 1
    base = 0
    
    lista = []
    
    while(contador <= iteraciones):
      lista.append(base)
      numero_siguiente = numero + base
      base = numero
      numero = numero_siguiente
      contador += 1
      
    sucesion = ""

    for i in lista:
        sucesion += str(i) + ","

    
    return sucesion[0:-1]
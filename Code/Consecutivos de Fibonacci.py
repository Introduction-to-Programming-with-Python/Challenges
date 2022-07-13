def secuencia_de_fibonacci(fib_1:int, fib_2:int, fib_3:int, fib_4:int) -> str:

    if fib_1 + fib_2 == fib_3 and fib_2 + fib_3 == fib_4:
        respuesta = "Fibofacil"

    else:
        respuesta = "Fibofalsa"

    return respuesta
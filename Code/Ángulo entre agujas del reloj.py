def angulo_entre_agujas_reloj(hora:int, minutos:int)->float:
    
    ang_hora=30*hora+minutos*0.5
    ang_minuto=6*minutos
    alfa=ang_hora-ang_minuto
    alfa=abs(alfa)
    beta=360-alfa
    respuesta=min(alfa, beta)
    
    return respuesta
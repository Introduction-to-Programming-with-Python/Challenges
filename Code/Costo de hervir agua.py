def costo_hervir_agua(masa_agua:float)->float:

    m=masa_agua
    temperatura_inicial=20
    temperatura_final=100
    delta_t=temperatura_final-temperatura_inicial
    c=4.186
    q=m*c*delta_t
    watt=q/3600
    kilowatt=watt/1000
    costo=kilowatt*0.089
    
    return float(round(costo,4))
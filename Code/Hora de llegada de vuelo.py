def calcular_horario_llegada(hora_salida: int, minuto_salida: int, segundo_salida: int, duracion_horas: int, duracion_minutos: int, duracion_segundos: int)->str:
    
    x1=hora_salida*3600
    y1=minuto_salida*60
    total1=x1+y1+segundo_salida
    
    x2=duracion_horas*3600
    y2=duracion_minutos*60
    total2=x2+y2+duracion_segundos
    
    total=total1+total2
    
    hora_exacta=total//3600
    hora=hora_exacta%24
    
    minuto_sobrante=total%3600
    minuto=minuto_sobrante//60
    
    segundo=minuto_sobrante%60
    
    return str(hora) + ":" +str(minuto)+ ":" +str(segundo)
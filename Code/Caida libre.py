def vel_en_caida_libre(altura:float)->float:
    
    vi=0
    a=9.8
    velocidad=pow((pow(vi,2)+(2*a*altura)),1/2)
    
    return round(velocidad,2)
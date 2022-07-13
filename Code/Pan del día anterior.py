def calcular_total_pan_comprado(frescos:int, viejos:int)->int:
    
    frescos=frescos
    viejos=viejos
    
    pfrescos=450
    pviejos=pfrescos*0.4
    
    total=pfrescos*frescos + pviejos*viejos
    
    return total
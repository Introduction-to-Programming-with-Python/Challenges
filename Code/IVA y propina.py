def calcular_iva_propina_total_factura(costo_factura:int)->str:

    iva=0.19
    propina=0.10
    iva=costo_factura*iva
    propina=costo_factura*propina
    total=costo_factura+iva+propina
    x=iva
    y=propina
    z=total
    costo_factura=str(round(x))+","+str(round(y))+","+str(round(z))
    
    return costo_factura
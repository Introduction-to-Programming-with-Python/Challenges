def mejor_del_curso(estudiante1:dict, estudiante2:dict, estudiante3:dict, estudiante4:dict, estudiante5:dict, curso:str) -> str:

    # Extraer nombres

    nombre_estudiante_1 = estudiante1["nombre"]
    nombre_estudiante_1 = nombre_estudiante_1.lower()

    nombre_estudiante_2 = estudiante2["nombre"]
    nombre_estudiante_2 = nombre_estudiante_2.lower()

    nombre_estudiante_3 = estudiante3["nombre"]
    nombre_estudiante_3 = nombre_estudiante_3.lower()

    nombre_estudiante_4 = estudiante4["nombre"]
    nombre_estudiante_4 = nombre_estudiante_4.lower()

    nombre_estudiante_5 = estudiante5["nombre"]
    nombre_estudiante_5 = nombre_estudiante_5.lower()



    # Para casos de empates

    empates = {"1": nombre_estudiante_1, "2": nombre_estudiante_2, "3": nombre_estudiante_3, 
                "4": nombre_estudiante_4, "5": nombre_estudiante_5}

    if curso == "matematicas":

        # Extraer notas

        estudiante_1 = estudiante1["matematicas"]
        estudiante_2 = estudiante2["matematicas"]
        estudiante_3 = estudiante3["matematicas"]
        estudiante_4 = estudiante4["matematicas"]
        estudiante_5 = estudiante5["matematicas"]

        mejor = max(estudiante_1, estudiante_2, estudiante_3, estudiante_4, estudiante_5)

        if mejor != estudiante_1:
            del empates["1"]

        if mejor != estudiante_2:
            del empates["2"]    

        if mejor != estudiante_3:
            del empates["3"]   

        if mejor != estudiante_4:
            del empates["4"]  

        if mejor != estudiante_5:
            del empates["5"]

        lista = []
    
        if "1" in empates:
            lista += [nombre_estudiante_1]
    
        if "2" in empates:
            lista += [nombre_estudiante_2]
    
        if "3" in empates:
            lista += [nombre_estudiante_3]
    
        if "4" in empates:
            lista += [nombre_estudiante_4]
    
        if "5" in empates:
            lista += [nombre_estudiante_5]
    
        estudiante = min(lista)

    elif curso == "español":

        # Extraer notas

        estudiante_1 = estudiante1["español"]
        estudiante_2 = estudiante2["español"]
        estudiante_3 = estudiante3["español"]
        estudiante_4 = estudiante4["español"]
        estudiante_5 = estudiante5["español"]

        mejor = max(estudiante_1, estudiante_2, estudiante_3, estudiante_4, estudiante_5)

        if mejor != estudiante_1:
            del empates["1"]

        if mejor != estudiante_2:
            del empates["2"]    

        if mejor != estudiante_3:
            del empates["3"]   

        if mejor != estudiante_4:
            del empates["4"]  

        if mejor != estudiante_5:
            del empates["5"]

        lista = []
    
        if "1" in empates:
            lista += [nombre_estudiante_1]
    
        if "2" in empates:
            lista += [nombre_estudiante_2]
    
        if "3" in empates:
            lista += [nombre_estudiante_3]
    
        if "4" in empates:
            lista += [nombre_estudiante_4]
    
        if "5" in empates:
            lista += [nombre_estudiante_5]
    
        estudiante = min(lista)

    elif curso == "ciencias":

        # Extraer notas

        estudiante_1 = estudiante1["ciencias"]
        estudiante_2 = estudiante2["ciencias"]
        estudiante_3 = estudiante3["ciencias"]
        estudiante_4 = estudiante4["ciencias"]
        estudiante_5 = estudiante5["ciencias"]

        mejor = max(estudiante_1, estudiante_2, estudiante_3, estudiante_4, estudiante_5)

        if mejor != estudiante_1:
            del empates["1"]

        if mejor != estudiante_2:
            del empates["2"]    

        if mejor != estudiante_3:
            del empates["3"]   

        if mejor != estudiante_4:
            del empates["4"]  

        if mejor != estudiante_5:
            del empates["5"]

        lista = []
    
        if "1" in empates:
            lista += [nombre_estudiante_1]
    
        if "2" in empates:
            lista += [nombre_estudiante_2]
    
        if "3" in empates:
            lista += [nombre_estudiante_3]
    
        if "4" in empates:
            lista += [nombre_estudiante_4]
    
        if "5" in empates:
            lista += [nombre_estudiante_5]
    
        estudiante = min(lista)

    elif curso == "literatura":

        # Extraer notas

        estudiante_1 = estudiante1["literatura"]
        estudiante_2 = estudiante2["literatura"]
        estudiante_3 = estudiante3["literatura"]
        estudiante_4 = estudiante4["literatura"]
        estudiante_5 = estudiante5["literatura"]

        mejor = max(estudiante_1, estudiante_2, estudiante_3, estudiante_4, estudiante_5)

        if mejor != estudiante_1:
            del empates["1"]

        if mejor != estudiante_2:
            del empates["2"]    

        if mejor != estudiante_3:
            del empates["3"]   

        if mejor != estudiante_4:
            del empates["4"]  

        if mejor != estudiante_5:
            del empates["5"]

        lista = []
    
        if "1" in empates:
            lista += [nombre_estudiante_1]
    
        if "2" in empates:
            lista += [nombre_estudiante_2]
    
        if "3" in empates:
            lista += [nombre_estudiante_3]
    
        if "4" in empates:
            lista += [nombre_estudiante_4]
    
        if "5" in empates:
            lista += [nombre_estudiante_5]
    
        estudiante = min(lista)

    elif curso == "arte":

        # Extraer notas

        estudiante_1 = estudiante1["arte"]
        estudiante_2 = estudiante2["arte"]
        estudiante_3 = estudiante3["arte"]
        estudiante_4 = estudiante4["arte"]
        estudiante_5 = estudiante5["arte"]

        mejor = max(estudiante_1, estudiante_2, estudiante_3, estudiante_4, estudiante_5)

        if mejor != estudiante_1:
            del empates["1"]

        if mejor != estudiante_2:
            del empates["2"]    

        if mejor != estudiante_3:
            del empates["3"]   

        if mejor != estudiante_4:
            del empates["4"]  

        if mejor != estudiante_5:
            del empates["5"]

        lista = []
    
        if "1" in empates:
            lista += [nombre_estudiante_1]
    
        if "2" in empates:
            lista += [nombre_estudiante_2]
    
        if "3" in empates:
            lista += [nombre_estudiante_3]
    
        if "4" in empates:
            lista += [nombre_estudiante_4]
    
        if "5" in empates:
            lista += [nombre_estudiante_5]
    
        estudiante = min(lista)

    else:
        estudiante = "El curso insertado no es dictado."


    return estudiante
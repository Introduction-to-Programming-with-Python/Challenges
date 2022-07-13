def conteo_de_materias(nombre_materia_1, nombre_materia_2, nombre_materia_3) -> int:
    
    interes_1 = "programacion"
    interes_2 = "matematica"
    interes_3 = "filosofia"
    interes_4 = "literatura"
    
    n_materias = 0
    
    if (interes_1 in nombre_materia_1):
        n_materias += 1
        
    if (interes_2 in nombre_materia_1):
        n_materias += 1
        
    if (interes_3 in nombre_materia_1):
        n_materias += 1
        
    if (interes_4 in nombre_materia_1):
        n_materias += 1
        
    if (interes_1 in nombre_materia_2):
        n_materias += 1
        
    if (interes_2 in nombre_materia_2):
        n_materias += 1
        
    if (interes_3 in nombre_materia_2):
        n_materias += 1
        
    if (interes_4 in nombre_materia_2):
        n_materias += 1
        
    if (interes_1 in nombre_materia_3):
        n_materias += 1
        
    if (interes_2 in nombre_materia_3):
        n_materias += 1
        
    if (interes_3 in nombre_materia_3):
        n_materias += 1
        
    if (interes_4 in nombre_materia_3):
        n_materias += 1
        
    return n_materias
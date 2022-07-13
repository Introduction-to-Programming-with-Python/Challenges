def tiempo_a_segundos(dias:int, horas:int, mins:int, seg:int)->int:
    """
    

    Parameters
    ----------
    dias : int
        DESCRIPTION.
    horas : int
        DESCRIPTION.
    mins : int
        DESCRIPTION.
    seg : int
        DESCRIPTION.

    Returns
    -------
    int
        DESCRIPTION.

    """
    total=seg
    total=total+(mins*60)
    total=total+(horas*60*60)
    
    total=seg
    total=total+(mins*60)
    total=total+(horas*60*60)
    total= total + (dias*24*60*60)
    
    return total
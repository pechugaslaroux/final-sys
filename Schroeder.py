import numpy as np

def schroeder(audio):
    """Funcion que realiza la integral de Schoreder

    Args:
        audio (array): Array de datos 

    Returns:
        array: Devuelve valores luego de integrar
    """
    sch = np.cumsum(audio**2)[::-1]
    return sch
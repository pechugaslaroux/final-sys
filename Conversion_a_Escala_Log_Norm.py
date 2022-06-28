import numpy as np

def func_Conver_log_norm(señal):
    """funcion que convierte a escala logaritmica normalizada

    Args:
        señal (array): Numpy array de los datos de un audio

    Returns:
        array: array de datos con conversion logaritmica normalizada
    """
    
    if 0 in señal:
        minimum = min(i for i in señal if i > 0)
        señal[señal == 0] = minimum
            

    logNorm = 10 * np.log10((señal/max(señal))**2) 
   
    return logNorm

"""
señal = [0, 1, 2 ,3 ,5, 6, 2,-2, 0]

a = func_Conver_log_norm(señal)
print(a)
"""
import numpy as np

def func_Conver_log_norm(señal):
    """funcion que convierte a escala logaritmica normalizada

    Args:
        señal (array): Numpy array de los datos de un audio

    Returns:
        array: array de datos con conversion logaritmica normalizada
    """
    
    señal2 = np.array(señal)
    señal_max = np.max(señal2)
    min_nonzero = np.min(señal2[np.nonzero(señal2)])
    señal2[señal2 == 0] = min_nonzero
    señal_norm = (10.0*np.log10((señal2/señal_max)**2))
    return señal_norm

"""
señal = [0, 1, 2 ,3 ,5, 6, 2,-2, 0]

a = func_Conver_log_norm(señal)
print(a)
"""
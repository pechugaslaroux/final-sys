import numpy as np

def func_Conver_log_norm(señal):
    """funcion que convierte a escala logaritmica normalizada

    Args:
        señal (array): Numpy array de los datos de un audio

    Returns:
        array: array de datos con conversion logaritmica normalizada
    """
    señal_max = np.max(señal)
    señal_norm = (10.0*np.log10((señal/señal_max)**2))
    return señal_norm
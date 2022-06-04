import numpy as np

def suave_filt_med_mov(array, w):
    """Funcion de suavizado por filtro de promedio movil

    Args:
        array (array): Señal que ingresa
        w (int): Tamaño de la ventana

    Returns:
        array: Array de datos de la señal suavizada
    """
    suave = np.zeros(len(array)-w)
    for i in range(0, len(suave)):
        suave[i] = np.mean(array[i:i+w])
        # Agregamos ceros para compensar el delay
    suave = np.hstack([np.zeros(w//2), suave, np.zeros(w//2)])
    return suave
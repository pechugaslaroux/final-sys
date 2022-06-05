import numpy as np
from scipy.signal import hilbert, medfilt

def suavizado(audio, metodo = 'hilbert', ventana = 11):
    """función que suaviza la señal ingresada.

    Args:
        audio (array): numpy array del audio a analizar.
        metodo (str, optional): metodo por el cual realizar el suavizado. Default 'hilbert'.
        ventana (int, optional): ancho de la ventana. Default 10.

    Returns:
        array: numpy array de la señal suavizada.
    """
    if metodo == 'hilbert':
        suave_audio = np.abs(hilbert(audio))
        
    if metodo == 'median':
        suave_audio = medfilt(audio, ventana)
  

    return suave_audio


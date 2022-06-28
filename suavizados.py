import numpy as np
from scipy.signal import hilbert

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
        suave = np.abs(hilbert(audio))
        
    if metodo == 'median':
        suave_audio = np.zeros(len(audio)-ventana)
        for i in range(0, len(suave_audio)):
            suave_audio[i] = np.mean(audio[i:i+ventana])
            # Agregamos ceros para compensar el delay
        suave = np.hstack([np.zeros(ventana//2), suave_audio, np.zeros(ventana//2)])
  
  

    return suave


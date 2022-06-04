import numpy as np
from scipy.signal import hilbert, medfilt

def suavizado(audio, metodo = 'hilbert', ventana = 7):
    '''
    Docstring goes Here.
    '''
    if metodo == 'hilbert':
        suave_audio = np.abs(hilbert(audio))
        
    if metodo == 'median':
        suave_audio = medfilt(audio, ventana)
  

    return suave_audio


import numpy as np

def edt(recta, fs = 44100):
   
    
    edt = len(recta[recta>=-10])/fs
    
    return edt

def t60(recta, fs = 44100, metodo = 't30'):
    
    if metodo == 't10':
        
        t10 = len(recta[recta>=-10])/fs
        t60 = t10*6
        
    elif metodo == 't20':
       
        t20 = len(recta[recta>=-20])/fs
        t60 = t20*3

    elif metodo == 't30':
        
        t30 = len(recta[recta>=-30])/fs
        t60 = t30*2
      
    return t60

def d50(impulso, fs):
    """función que calcula el D50 de una señal

    Args:
        impulso (array): numpy array del audio a analizar.
        fs (int, optional): frecuencia de muestreo. Default 44100.

    Returns:
        list: los parametros de D50 por banda de octava.
    """

    t = round(0.050 * fs)
    d50 = 100 * (np.sum(impulso[:t]) / np.sum(impulso))
    
    return d50

def c80(impulso, fs):
    """función que calcula el C80 de una señal

    Args:
        impulso (array): numpy array del audio a analizar.
        fs (int, optional): frecuencia de muestreo. Default 44100.

    Returns:
        list: los parametros de C80 por banda de octava.
    """

    t = round(0.080 * fs)
    c80 = 10 * np.log10(np.sum(impulso[:t]) / np.sum(impulso[t:]))
    
    return c80

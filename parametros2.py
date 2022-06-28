from re import A
import numpy as np


def edt(impulso2, fs = 44100):
    impulso = np.array(impulso2)
    edt = len(impulso[impulso>=-10])/fs
    
    return edt

def t60(impulso2, fs = 44100, metodo = 't30'):
    impulso = np.array(impulso2)
       
    if metodo == 't10':
        t10 = len(impulso[impulso>=-10])/fs
        t60 = t10*6
        
    elif metodo == 't20':

        t20 = len(impulso[impulso>=-20])/fs
        t60 = t20*3

    elif metodo == 't30':
       
        t30 = len(impulso[impulso>=-30])/fs
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
    #t = 0.050
    a = (np.sum((impulso[:t])**2))
    b = (np.sum((impulso[t:])**2))
    d50 =  (a / b)
    
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
    c80 = 10 * np.log10(np.sum((impulso[:t])**2) / np.sum((impulso[t:])**2))
    
    return c80


import numpy as np


def edt(impulso, fs = 44100):
    """Función que ajusta por cuadrados minimos y calcula el early decay de la señal ingresada filtrada en bandas de octava. 

    Args:
        impulso (array): numpy array del audio a analizar.
        fs (int, optional): frecuencia de muestreo. Default 44100.

    Returns:
        list: los parametros de edt por banda de octava.
    """
    
    t = np.arange(len(impulso))/fs 
    index_edt = np.where(((impulso <= -1) & (impulso >= -10)))
    coeff_edt = np.polyfit(t[index_edt[0]],
                       impulso[index_edt[0]], 1)
    
    fit_edt = coeff_edt[0]*t + coeff_edt[1]
    edt = len(fit_edt[fit_edt>=-10])/fs
    
    return edt

def t60(impulso, fs = 44100, metodo = 't30'):
    """función que calcula el T60 de una señal a partir de otros parametros acústicos 

    Args:
        impulso (array): numpy array del audio a analizar.
        fs (int, optional): frecuencia de muestreo. Default 44100.
        metodo (str, optional): parámetro acústico. Default 't30'.

    Returns:
        list: los parametros de T60 por banda de octava.
    """

    t = np.arange(len(impulso))/fs 
    
    if metodo == 't10':
        index_t10 = np.where(((impulso <= -5) & (impulso >= -15)))
        coeff_t10 = np.polyfit(t[index_t10[0]], impulso[index_t10[0]], 1)
        fit_t10 = coeff_t10[0]*t + coeff_t10[1]
        t10 = len(fit_t10[fit_t10>=-10])/fs
        t60 = t10*6
        
    elif metodo == 't20':
        index_t20 = np.where(((impulso <= -5) & (impulso >= -25)))
        coeff_t20 = np.polyfit(t[index_t20[0]], impulso[index_t20[0]], 1)
        fit_t20 = coeff_t20[0]*t + coeff_t20[1]
        t20 = len(fit_t20[fit_t20>=-20])/fs
        t60 = t20*3

    elif metodo == 't30':
        index_t30 = np.where(((impulso <= -5) & (impulso >= -35)))
        coeff_t30 = np.polyfit(t[index_t30[0]], impulso[index_t30[0]], 1)
        fit_t30 = coeff_t30[0]*t + coeff_t30[1]
        t30 = len(fit_t30[fit_t30>=-30])/fs
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


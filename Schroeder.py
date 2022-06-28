import numpy as np

def schroeder(audio, t = 0.45, fs = 44100):
    """Funcion que realiza la integral de Schoreder

    Args:
        audio (array): Array de datos 

    Returns:
        array: Devuelve valores luego de integrar
    """
    #sch = np.cumsum(audio**2)[::-1]
    short_impulse = audio[0:round(t*fs)]
    integrate_sch = np.cumsum(short_impulse[::-1])/np.sum(audio)
    int_sch = integrate_sch[::-1]
    if 0 in int_sch:
        minimum = min(i for i in int_sch if i > 0)
        int_sch[int_sch == 0] = minimum
          
    sch = 10 * np.log10((int_sch/max(int_sch))**2) 
    return sch
   #return sch
import numpy as np
import soundfile as sf
from graficar import graficar

def sint_RI(T60 , fs = 44100, fi = [31.25 , 62.5 , 152 , 250 , 500 , 1000 , 2000 , 4000 , 8000 , 16000]):
    """función de sintetización de RI 

    Args:
        T60 (list): los T60 de la medición
        fi (list, optional): las frecuencias centrales. Default [31.25 , 62.5 , 152 , 250 , 500 , 1000 , 2000 , 4000 , 8000 , 16000].

    Returns:
        array: la sumatoria de las frecuencas de la RI correspondiente
    """
    
    
    T60 = np.array(T60)
    T60_max = max(T60)
    to = T60_max*fs
    yi = np.zeros_like(to)
    t = np.linspace(0, int(T60_max), int(to))
    tau = (np.log(10 ** -3))/T60
    acumulador = 0
    for i in range(len(fi)):
        ri = lambda t:  (np.exp(tau[i] * t)) * (np.cos(2 * np.pi * fi[i] * t))
        acumulador = acumulador + (yi + ri(t))

    

    yi_max = max(abs(max(acumulador)), abs(min(acumulador)))
    yi_total_normalizado = acumulador/yi_max
    sf.write('./audio_generate/impulso_sintetizado.wav', yi_total_normalizado, 44100)
    return yi_total_normalizado


"""Test 
T_60 = [2.44, 1.87, 1.88, 2.14, 2.52, 2.55, 2.16, 1.61, 0.88, 0.65]

a = sint_RI(T_60,44100)
print(a)
graficar(a)
"""
import numpy as np
import soundfile as sf

def sint_RI(T60 , fs, fi = [31.25 , 62.5 , 152 , 250 , 500 , 1000 , 2000 , 4000 , 8000 , 16000]):
    """función de sintetización de RI 

    Args:
        T60 (list): los T60 de la medición
        fi (list, optional): las frecuencias centrales. Default [31.25 , 62.5 , 152 , 250 , 500 , 1000 , 2000 , 4000 , 8000 , 16000].

    Returns:
        array: la sumatoria de las frecuencas de la RI correspondiente
    """
    pisublist = []
    yilist = []
    to = max(T60)*fs
    t = np.linspace(0,int(max(T60)),int(to))
    suma = 0
    for n,m in zip(T60, fi):
        yi_temp = []
        for o in t:
            pisubi = ((-1)*np.log(10**(-3)))/n
            pisublist.append(pisubi)
            yi = np.exp(pisubi * o) * np.cos(2*np.pi * m * o)
            yi_temp.append(yi)
        yilist.append(yi_temp)
    yi_total =  []
    for i in range(int(t.size)):
        acumulador = 0
        for n in range(len(fi)):
            array_temp = yilist[n]
            #acumulador = acumulador + array_temp[i]
            acumulador = np.cumsum(array_temp[i])
        yi_total.append(acumulador)
    yi_total = np.array(yi_total)
    yi_total = yi_total[::-1]

    yi_max = max(abs(max(yi_total)), abs(min(yi_total)))
    yi_total_normalizado = yi_total/yi_max
    sf.write('impulso_sintetizado.wav', yi_total_normalizado, 44100)
    return yi_total_normalizado

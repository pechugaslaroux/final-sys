import numpy as np

def restric(audio, metodo):
    if metodo == "edt":
        index = np.where(((audio <= -1) & (audio >= -10)))
        return index
    elif metodo == "T10":
        index = np.where(((audio <= -5) & (audio >= -15)))
        return index
    elif metodo == "T20":
        index = np.where(((audio <= -5) & (audio >= -25)))
        return index
    elif metodo == "T30":
        index = np.where(((audio <= -5) & (audio >= -35)))
        return index



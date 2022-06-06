import numpy as np
import pandas as pd
import librosa


def de_wav_a_df(f):
    """función que recibe un archivo .wav y lo tranforma en un data frame.

    Args:
        f (str): la ruta del archivo .wav a transformar. de la forma: C:/Users/Documents/xxx/xxx/nombre_del_archivo.wav

    Returns:
        data frame: el data frame del archivo .wav
    """
    x=[]
    y,sr = librosa.load(f, sr=None)
    for i in y:
        x.append(y[i])
    return x

meme= de_wav_a_df("C:/Users/nacho/Desktop/spokane_womans_club_ir.wav")
print(meme)

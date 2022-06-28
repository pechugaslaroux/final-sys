import numpy as np
import soundfile as sf
from graficar import graficar


def de_wav_a_array(audio):
    """funcion que devuelve el array de un archivo de audio .wav

    Args:
        audio (str): ruta del archivo de audio .wav

    Returns:
        array: numpy array del audio.
    """
    a = sf.read(audio)
    x = np.array(a[0],dtype=float)
    f_s = a[1]

    x_max = max(abs(x))
    x_normal = x / x_max
    return {
        'arr': x_normal,
        "fs": f_s
    }

if __name__ == '__main__':
  a = de_wav_a_array('./Audios Descargados RI/spokane_womans_club_ir.wav')
  b = a['arr']
  print(b)
  graficar(b)

import numpy as np
import soundfile as sf


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



import numpy as np
import soundfile as sf
import scipy.signal as sig
from graficar import graficar



def sfilt(T, fs = 44100, f1 = 20, f2 = 20000):
    """ funcion que genera un sine sweep logarítmico y filtro inverso

    Args:
        T (int): duración del sine sweep (en segundos)
        fs (int, optional): frecuencia de sampleo. Default 44100.
        f1 (int, optional): frecuencia inferior. Default 20.
        f2 (int, optional): frecuencia superior. Default 22050.
    """

    w1=2*np.pi*f1
    w2=2*np.pi*f2
    t = np.arange(0, T*fs)/fs
    R=np.log(w2/w1)
    K=(T*w1)/R
    L=T/R
    # Sine Sweep
    f= np.sin(K*((np.e**(t/L))-1))
    # normalizar datos
    fmax = max(abs(max(f)), abs(min(f)))
    fnorm = f/fmax
    # Filtro inverso
    j=np.e**(t*R/T)
    x=fnorm[::-1]/j
    # Convolucion
    conv = sig.fftconvolve(fnorm, x, mode='same')
    # normalizar datos
    conv_max = max(abs(max(conv)), abs(min(conv)))
    conv_norm = conv/conv_max
    #genera los audios
    sf.write('./audio_generate/sinesweep.wav', fnorm, fs)
    
    sf.write('./audio_generate/invfiltro.wav', x, fs)

    sf.write('./audio_generate/convolucion.wav', conv_norm, fs)

    return {
        'sine': fnorm,
        "filtro": x,
        "conv": conv_norm
    }

if __name__ == '__main__':
  a = sfilt(10)

  b = a['sine']

  c = a['filtro']

  d = a['conv']

  graficar(b)

  graficar(c)

  graficar(d)

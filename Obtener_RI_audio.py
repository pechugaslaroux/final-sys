from scipy import signal
import soundfile as sf
import numpy as np


def respuesta_impulso(file_y, file_x):
    """funcion para obtener respuesta al impulso en formato de audio (a partir de un sinesweep logarítmico y su filtro inverso)

    Args:
        file_y (wav): Respuesta de la sala al sinesweep
        file_x (wav): Filtro inverso

    Returns:
        array: Datos del audio
    """
    #carga de cada archivo .wav
    resp_sinesweep,fs1 = sf.read(file_y)
    filtro_inverso,fs2= sf.read(file_x)
    
    #convolución
    h = signal.fftconvolve(resp_sinesweep,filtro_inverso)
    
    hmax = np.max(np.absolute(h))
    h_norm=h/hmax
    # Crea el .wav
    sf.write("./audio_generate/RespImpulso.wav", h_norm, 44100)
    
    return h_norm

if __name__ == '__main__':
  a1 = "audio_generate/impulso_sintetizado.wav"
  a2 = "audio_generate/convolucion.wav"
  a3 = respuesta_impulso(a1, a2)
  print(a3)

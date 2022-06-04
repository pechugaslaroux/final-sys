import numpy as np
from matplotlib import pyplot as plt
import simpleaudio as sa

def repro(audio):
    """ función para reproducir un archivo de audio .wav

    Args:
        audio (str): El nombre del archivo de audio. Escribirlo como sigue: "./nombre.wav"
    """
   
    wave_obj = sa.WaveObject.from_wave_file(audio)
    play_obj = wave_obj.play()
    play_obj.wait_done()
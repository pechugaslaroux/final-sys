import numpy as np
from scipy.signal import iirfilter, sosfilt
import soundfile as sf
from de_wav_a_array import de_wav_a_array



def FiltrodeOctava(audio_RI, fs = 44100):

    """funcion filtro de octava según Norma IEC61260

    Args:
        audio_RI (array): array de la señal a la que se le aplicará el filtro

    Returns:
        array: Informacion del filtro
    """
    user_fs = fs    
    
    
    fi = [31.25, 62.5, 125, 250, 500, 1000, 2000, 4000, 8000]
    banda_octava = []
    filtaudio_octava = []


    for fc in fi:
        
        sos = iirfilter(7, [fc / (2**(1/2)), fc * (2**(1/2))],
                        rs=60, btype='band', analog=False,
                        ftype='butter', fs=user_fs, output='sos')
        banda_octava.append(sos)
        filtaudio_octava.append(sosfilt(sos, audio_RI))
          
    for index, fs in enumerate(fi):
        sf.write("./audio_generate/prueba_" + str(fs) + ".wav",filtaudio_octava[index],44100)     
    return filtaudio_octava

if __name__ == '__main__':
  a = de_wav_a_array("./Audios Descargados RI/whitenoise.wav")
  b = a['arr']
  c = FiltrodeOctava(b)
  print(c)

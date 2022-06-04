import numpy as np
import pandas as pd
from scipy import signal
import librosa
import soundfile as sf


def FiltrodeOctava(audio_RI, sr = 44100):
    """funcion filtro de octava según Norma IEC61260

    Args:
        audiofile_RI (wav): Archivo al que se le aplicará el filtro

    Returns:
        array: Informacion del filtro
    """
    #Octava - G = 1.0/2.0 
    G = 1.0/2.0
    #freacuencias centrales norma IEC61260
    fi = [31.5,63,125,250,500,1000,2000,4000,8000,16000]
    factor = np.power(2, G)
    
    #transforma en data frame el archivo .wav
    #y,sr = librosa.load(audiofile_RI, sr=None)

    df = pd.DataFrame(audio_RI)

    df.index = [(1/sr)*i for i in range(len(df.index))]

    data_frame_file = df.sum(axis=1)

    filt = []

    for centerFrequency_Hz in fi:
        #Calculo los extremos de la banda a partir de la frecuencia central
        lowerCutoffFrequency_Hz=centerFrequency_Hz/factor;
        upperCutoffFrequency_Hz=centerFrequency_Hz*factor;

        #print('Frecuencia de corte inferior: ', round(lowerCutoffFrequency_Hz), 'Hz')
        #print('Frecuencia de corte superior: ', round(upperCutoffFrequency_Hz), 'Hz')

        # Extraemos los coeficientes del filtro 
        b,a = signal.iirfilter(4, [2*np.pi*lowerCutoffFrequency_Hz,2*np.pi*upperCutoffFrequency_Hz],
                                    rs=60, btype='band', analog=True,
                                    ftype='butter') 

        # para aplicar el filtro es más óptimo
        sos = signal.iirfilter(4, [lowerCutoffFrequency_Hz,upperCutoffFrequency_Hz],
                                    rs=60, btype='band', analog=False,
                                    ftype='butter', fs=96000, output='sos')
        w, h = signal.freqs(b,a)

        # aplicando filtro al audio
        filt.append(signal.sosfilt(sos, data_frame_file))
    #crea los .wav
    for index, fs in enumerate(fi):
        sf.write("./audio_generate/prueba_" + str(fs) + ".wav",filt[index],44100)
    return filt
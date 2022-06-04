import simpleaudio as sa
import sounddevice as sd
from scipy.io.wavfile import write


def playrec(t, audio_sn, fs = 44100):
    """funcion para reproducir un audio de sine sweep logarítmico y grabar de forma simultanea

    Args:
        t (int): tiempo de ka grabación (en segundos)
        audio_sn (str): el nombre del archivo de audio del sine sweep "./nombre"
        fs (int, optional): frecuencia de sampleo. Default 44100.
    """
    a = sd.query_devices()  
    print(a)
    disp = int(input("el nombre del dispositivo para reproducir"))
    sd.default.device = disp
    wave_obj = sa.WaveObject.from_wave_file(audio_sn)
    play_obj = wave_obj.play()
    disp = int(input("el nombre del dispositivo para grabar"))
    sd.default.device = disp
    
    myrecording = sd.rec(int(t * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)  # Save as WAV file
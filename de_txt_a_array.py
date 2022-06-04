import numpy as np
def de_txt_a_array(archivo):
    """Funcion para convertir un txt de datos de audio a un array

    Args:
        archivo (str): ruta del archivo a convertir

    Returns:
        array: array de Numpy con datos de audio
    """
    converter = lambda x:float(x.replace(',', '.'))
    val_txt = np.genfromtxt(archivo, skip_header=0,delimiter='	',names=True,converters={'Frecuencia_Hz':converter,'Nivel_dB':converter},encoding=None)
    val_array = np.array(list(zip(*val_txt)))
    return val_array
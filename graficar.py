import numpy as np
from matplotlib import pyplot as plt



def graficar(signal, x_label = 'x', y_label = 'y', title = '', fs = 44100, x_scale = 'linear', y_scale = 'linear'):
    """ 
    Función para graficar. 

    Args:
        signal (array): señal a graficar
        x_label (str): título del eje x
        y_label (str): título del eje y
        title (str): título del gráfico
        fs (int, optional): Frecuencia de sampleo. Default 44100.
        x_scale (str, optional): tipo de escala del eje x. Default 'linear'.
        y_scale (str, optional): tipo de escala del eje y. Default 'linear'.
    """
    time = np.linspace(0,len(signal)/fs,num=len(signal))
    plt.xscale(x_scale)
    plt.yscale(y_scale)
    plt.plot(time, signal)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


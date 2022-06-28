import numpy as np
import matplotlib.pyplot as plt

def func_Conver_log_norm(señal):
    """funcion que convierte a escala logaritmica normalizada

    Args:
        señal (array): Numpy array de los datos de un audio

    Returns:
        array: array de datos con conversion logaritmica normalizada
    """
    
    if 0 in señal:
        minimum = min(i for i in señal if i > 0)
        señal[señal == 0] = minimum
            

    logNorm = 10 * np.log10((señal/max(señal))**2) 
   
    return logNorm

if __name__ == '__main__':
  señal = [1, 2 ,3 ,4, 5, 6 , 7, 8, 9, 10]
  señal = np.array(señal)
  a = func_Conver_log_norm(señal)
  print(a)
  u = len(señal)
  t = np.linspace(0,u,u)
  plt.plot(t,señal, c='g')
  plt.plot(t,a, 'r')
  plt.grid()
  plt.axis('equal')
  plt.xlabel('Tiempo')
  plt.ylabel('Amplitud')
  plt.title('Conversion Esc. Log')
  plt.show()
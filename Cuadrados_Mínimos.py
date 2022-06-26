import numpy as np
import matplotlib.pyplot as plt

def Cuadrados_Minimos(lista):

    array = np.array(lista, dtype=np.float64)

    n = len(array)
    #print("n:", n)

    Sy = np.sum(array)
    #print("Sy:", Sy)

    yy = (array)**2
    Syy = np.sum(yy)
    #print("Syy:", Syy)

    algo = []
    acumula = 0
    for i in array:
        acumula = acumula + 1
        algo.append(acumula)
    algo2 = np.array(algo, dtype=np.float64)
    Sx = np.sum(algo2)
    #print("Sx:", Sx)

    xy = algo2 * array
    Sxy = np.sum(xy)
    #print("Sxy:", Sxy)


    xx = (algo2)** 2
    Sxx = np.sum(xx)
    #print("Sxx:", Sxx)



    Ao = ((Sxx*Sy) - (Sx*Sxy)) / ((n*Sxx)-(Sx*Sx))

    A1 = ((n*Sxy) - (Sx*Sy)) / ((n*Sxx)-(Sx*Sx))
    


    E = []
    for l,m in zip(algo2,array):
        h = (m-(Ao + A1 * l))**2
        E.append(h)
    EC2 = np.array(E)
    Sr2 = np.sum(EC2)
    #print("Sr2:", Sr2)


    #Var_Ao = ((Sxx*Sr2)/(((n*Sxx)-(Sx*Sx))*(n-2)))
    #Sigma_Ao = np.sqrt(Var_Ao)
    #Var_A1 = ((n*Sr2)/(((n*Sxx)-(Sx*Sx))*(n-2)))
    #Sigma_A1 = np.sqrt(Var_A1)


    #print("Término independiente (Ao):", Ao, ". Desviación: ", Sigma_Ao, ". Varianza: ", Var_Ao)
    #print("Pendiente (A1):", A1, ". Desviación: ", Sigma_A1, ". Varianza: ", Var_A1)

    recta = []
    for w in algo2:
        y_xi = Ao + A1 * w
        recta.append(y_xi)
    recta2 = np.array(recta)

    #R = ((n*Sxy)-(Sx*Sy))/((np.sqrt((n*Sxx)-(Sx*Sx)))*(np.sqrt((n*Syy)-(Sy*Sy))))
    #print("Coeficiente Correlación Lineal (R):", R)
    return recta2


"""# TESTING

lista = [1.3, 3.5, 4.2, 5.0, 7.0, 8.8, 10.1, 12.5, 13.0, 15.6]
u = len(lista)
t = np.linspace(0,10,u)

pepe = Cuadrados_Minimos(lista)


plt.scatter(t,lista, c='g')
plt.plot(t,pepe, 'r')
plt.grid()
plt.axis('equal')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.title('Ajuste Cuadrados Minimos')
plt.show()
"""
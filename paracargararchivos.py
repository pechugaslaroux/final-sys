
def cargar_rutas():
    """funcion que guarda las rutas de archivos para luego ser utilizados.
    Cuando se ingrse poner como ejemplo: C:/Users/Documents/xxx/xxx/nombre_del_archivo.wav

    Returns:
        list: contiene las rutas a los archivos a utilizar y otra con los nombres
    """
    rutas = []
    nombres = []
    cant_aud = int(input("ingrese la cantidad de audios que quiera cargar "))

    for i in range(cant_aud):
        b = input("ingrese el nombre del archivo ")
        nombres.append(b)
        a = input("ingrese la ruta del archivo ")
        rutas.append(a)

    return {
        'rutas': rutas,
        "nombres": nombres
    }

# Forma de traerlo:
#data = cargar_rutas()
#nombre = data['nombres']
#files = data['rutas']




def cargar_archivos(*archivos_a_cargar):
    """función recibe los nombres de los archivos que desea cargar y los mapea con la ruta ingresada por el usuario.
    Cuando se ingrese una ruta debe ser absoluta. Ejemplo: C:/Users/Documents/xxx/xxx/nombre_del_archivo.wav

    Returns:
        dict: contiene las rutas a los archivos a utilizar
    """
    rutas = {}
    
    for archivo in archivos_a_cargar:
      ruta = input('Ingrese la ruta del archivo ' + archivo + ':\n')
      rutas[archivo] = ruta

    return rutas


if __name__ == '__main__':
  archivo_output_nombre = 'Output.wav'
  archivo_fi_nombre = 'Filtro inverso'
  archivo_ri_nombre = 'RI descargado'
  rutas = cargar_archivos(archivo_output_nombre, archivo_fi_nombre, archivo_ri_nombre)
  print(rutas)
  print(rutas[archivo_output_nombre])
  print(rutas[archivo_fi_nombre])
  print(rutas[archivo_ri_nombre])


import numpy as np
from RuidoRosa import ruidoRosa_voss
from graficar import graficar
from de_wav_a_array import de_wav_a_array
from sinesweep_filter_conv import sfilt
from play_rec import playrec
from paracargararchivos import cargar_archivos
from Func_Sint_RI import sint_RI
from Obtener_RI_audio import respuesta_impulso
from Conversion_a_Escala_Log_Norm import func_Conver_log_norm
from Filtro_de_Octava import FiltrodeOctava
from suavizados import suavizado
from parametros2 import edt, t60, d50, c80
from Schroeder import schroeder
from Cuadrados_Mínimos import Cuadrados_Minimos
from Restricciones import restric


# Variables a usar
T60 = [2.44, 1.87, 1.88, 2.14, 2.52, 2.55, 2.16, 1.61, 0.88]

# se generan los audios ruido rosa, sine sweep y filtro inverso
ruido_rosa = ruidoRosa_voss(10)

sinesweep_data = sfilt(10)

# adquisicion y reproduccion
playrec(12, './audio_generate/sinesweep.wav')

#Se cargan los audios
archivo_output_nombre = 'Output.wav'
archivo_fi_nombre = 'Filtro inverso'
archivo_ri_nombre = 'RI descargado'
rutas = cargar_archivos(archivo_output_nombre, archivo_fi_nombre, archivo_ri_nombre)

archivo_ri_nombre = 'RI descargado'
rutas = cargar_archivos(archivo_ri_nombre)

# se sintetiza el RI a partir del t60
ri_sint = sint_RI(T60, 44100)

# se genera el array del RI descargado 
ri_desc_data = de_wav_a_array(rutas[archivo_ri_nombre])

# array del RI descargado
ri_desc = ri_desc_data['arr']

# frecuencia de muestreo del RI descargado
ri_desc_fs = ri_desc_data['fs']

# se sintetiza el RI a partir del del output (generados por playrec) y el filtro inverso 
h_norm = respuesta_impulso(rutas[archivo_output_nombre], rutas[archivo_fi_nombre])

# se pasan a escala logaritmica
respuesta_i_norm = func_Conver_log_norm(h_norm)

ri_sint_norm = func_Conver_log_norm(ri_sint)


ri_desc_norm = func_Conver_log_norm(ri_desc)


# Se filtran las señales
respuesta_i_filt = FiltrodeOctava(respuesta_i_norm)

ri_sint_filt = FiltrodeOctava(ri_sint_norm)

ri_desc_filt = FiltrodeOctava(ri_desc_norm)


# Se calculan e imprimen los parametros del RI sintetizado
rta_edt_sint = [ ]
rta_T60_sint = [ ]
rta_D50_sint = [ ]
rta_C80_sint = [ ]


for data1 in ri_sint_filt:
    

    respuesta_i_suave_sint = suavizado(data1)
    sch =schroeder(respuesta_i_suave_sint)
    sch_a = Cuadrados_Minimos(sch)
    sch_b = restric(sch_a, "edt")
    sch_c = restric(sch_a, "T30")
    
    rta_edt_sint.append(edt(sch_b, 44100))
    rta_T60_sint.append(t60(sch_c, 44100))
    rta_D50_sint.append(d50(sch, 44100))
    rta_C80_sint.append(c80(sch, 44100))
    
    
    


print("RI Sintetizado")
print("edt: ", rta_edt_sint)
print("T60: ", rta_T60_sint)
print("D50: ", rta_D50_sint)
print("C80: ", rta_C80_sint)


# Se calculan e imprimen los parametros del RI grabado
rta_edt_ri = [ ]
rta_T60_ri = [ ]
rta_D50_ri = [ ]
rta_C80_ri = [ ]


for data1 in respuesta_i_filt:
    respuesta_i_suave_filt = suavizado(data1)
    sch =schroeder(respuesta_i_suave_filt)
    sch_a = Cuadrados_Minimos(sch)
    sch_b = restric(sch_a, "edt")
    sch_c = restric(sch_a, "T30")
    
    rta_edt_ri.append(edt(sch_b, 44100))
    rta_T60_ri.append(t60(sch_c, 44100))
    rta_D50_ri.append(d50(sch, 44100))
    rta_C80_ri.append(c80(sch, 44100))

print("RI grabado")
print("edt: ", rta_edt_ri)
print("T60: ", rta_T60_ri)
print("D50: ", rta_D50_ri)
print("C80: ", rta_C80_ri)



# Se calculan e imprimen los parametros del RI descargado 

rta_edt_desc = [ ]
rta_T60_desc = [ ]
rta_D50_desc = [ ]
rta_C80_desc = [ ]


for data1 in ri_desc_filt:
    
    respuesta_i_suave_sint = suavizado(data1)
    
    sch =schroeder(respuesta_i_suave_sint)
    sch_a = Cuadrados_Minimos(sch)
    sch_b = restric(sch_a, "edt")
    sch_c = restric(sch_a, "T30")
    
    rta_edt_desc.append(edt(sch_b, ri_desc_fs))
    rta_T60_desc.append(t60(sch_c, ri_desc_fs))
    rta_D50_desc.append(d50(sch, ri_desc_fs))
    rta_C80_desc.append(c80(sch, ri_desc_fs))


print("RI Descargado")
print("edt: ", rta_edt_desc)
print("T60: ", rta_T60_desc)
print("D50: ", rta_D50_desc)
print("C80: ", rta_C80_desc)

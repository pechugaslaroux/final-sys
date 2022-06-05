import numpy as np
from matplotlib import pyplot as plt
from RuidoRosa import ruidoRosa_voss
from graficar import graficar
from sinesweep_filter_conv import sfilt
from play_rec import playrec
from paracargararchivos import cargar_rutas
from Func_Sint_RI import sint_RI
from Obtener_RI_audio import respuesta_impulso
from Conversion_a_Escala_Log_Norm import func_Conver_log_norm
from Filtro_de_Octava import FiltrodeOctava
from suavizados import suavizado
from parameters import edt, t60, d50, c80

# Variables a usar
T60 = [2.44, 1.87, 1.88, 2.14, 2.52, 2.55, 2.16, 1.61, 0.88, 0.65]


ruido_rosa = ruidoRosa_voss(10)

sinesweep_data = sfilt(10)

playrec(12, './audio_generate/sinesweep.wav')

#poner primero el audio generado "output.wav" y después el audio generado "invfiltro.wav"
archivos_data = cargar_rutas()

ri_sint = sint_RI(T60, 44100)


h_norm = respuesta_impulso(archivos_data['rutas'][0], archivos_data['rutas'][1])

respuesta_i_norm = func_Conver_log_norm(h_norm)

ri_sint_norm = func_Conver_log_norm(ri_sint)

respuesta_i_filt = FiltrodeOctava(respuesta_i_norm)

ri_sint_filt = FiltrodeOctava(ri_sint_norm)

rta_edt_sint = [ ]
rta_T60_sint = [ ]
rta_D50_sint = [ ]
rta_C80_sint = [ ]

for data1 in ri_sint_filt:
    respuesta_i_suave_sint = suavizado(data1)
    sch = np.cumsum(respuesta_i_suave_sint**2)[::-1]
    sch_norm = func_Conver_log_norm(sch)
    rta_edt_sint.append(edt(sch_norm))
    rta_T60_sint.append(t60(sch_norm, 44100))
    rta_D50_sint.append(d50(sch_norm, 44100))
    rta_C80_sint.append(c80(sch_norm, 44100))

print("RI Sintetizado")
print("edt: ", rta_edt_sint)
print("T60: ", rta_T60_sint)
print("D50: ", rta_D50_sint)
print("C80: ", rta_C80_sint)

rta_edt_ri = [ ]
rta_T60_ri = [ ]
rta_D50_ri = [ ]
rta_C80_ri = [ ]

for data1 in respuesta_i_filt:
    respuesta_i_suave_filt = suavizado(data1)
    sch = np.cumsum(respuesta_i_suave_filt**2)[::-1]
    sch_norm = func_Conver_log_norm(sch)
    rta_edt_ri.append(edt(sch_norm))
    rta_T60_ri.append(t60(sch_norm, 44100))
    rta_D50_ri.append(d50(sch_norm, 44100))
    rta_C80_ri.append(c80(sch_norm, 44100))

print("RI grabado")
print("edt: ", rta_edt_ri)
print("T60: ", rta_T60_ri)
print("D50: ", rta_D50_ri)
print("C80: ", rta_C80_ri)



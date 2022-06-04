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
#from suave_filt_prom_movil import suave_filt_med_mov
from suavizados import suavizado
from de_wav_a_array import de_wav_a_array
from parameters import edt, t60, d50, c80
# Variables a usar
T60 = [2.44, 1.87, 1.88, 2.14, 2.52, 2.55, 2.16, 1.61, 0.88, 0.65]

#ruido_rosa = ruidoRosa_voss(10)

#sinesweep_data = sfilt(10)

#playrec(12, './audio_generate/sinesweep.wav')

#archivos_data = cargar_rutas()

ri_sint = sint_RI(T60, 44100)


#ri_dataset = de_wav_a_array("C:/Users/paula/Documents/projects/final/spokane_womans_club_ir.wav")

#h_norm = respuesta_impulso(archivos_data['rutas'][0], archivos_data['rutas'][1])

#respuesta_i_norm = func_Conver_log_norm(h_norm)

#ri_dataset_norm = func_Conver_log_norm(ri_dataset)

ri_sint_norm = func_Conver_log_norm(ri_sint)

#respuesta_i_filt = FiltrodeOctava(respuesta_i_norm)

ri_sint_filt = FiltrodeOctava(ri_sint_norm)

#ri_dataset_filt = FiltrodeOctava(ri_dataset_norm)
rta_edt = [ ]
rta_T60 = [ ]
rta_D50 = [ ]
rta_C80 = [ ]

for data1 in ri_sint_filt:
    respuesta_i_suave_sint = suavizado(data1)
    sch = np.cumsum(respuesta_i_suave_sint**2)[::-1]
    sch_norm = func_Conver_log_norm(sch)
    #pala = np.linspace(0,len(sch_norm)/44100,num=len(sch_norm))
    #ere = np.polyfit(pala,sch_norm,1)
    #ajustada = np.polyval(ere, pala)
    rta_edt.append(edt(sch_norm))
    rta_T60.append(t60(sch_norm, 44100, "t30"))
    rta_D50.append(d50(sch_norm, 44100))
    rta_C80.append(c80(sch_norm, 44100))

print(rta_edt)
print(rta_T60)
print(rta_D50)
print(rta_C80)



#ri_sint_suave = smoothing(ri_sint_filt, 44100)
#ri_sint_suave = suave_filt_med_mov(ri_sint_filt, 10)


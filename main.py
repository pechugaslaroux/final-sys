from RuidoRosa import ruidoRosa_voss
from graficar import graficar
from sinesweep_filter_conv import sfilt
from play_rec import playrec
from paracargararchivos import cargar_rutas
from Func_Sint_RI import sint_RI
from Obtener_RI_audio import respuesta_impulso
from Conversion_a_Escala_Log_Norm import func_Conver_log_norm

# Variables a usar
T60 = [2.44, 1.87, 1.88, 2.14, 2.52, 2.55, 2.16, 1.61, 0.88, 0.65]

ruido_rosa = ruidoRosa_voss(10)

sinesweep_data = sfilt(10)

playrec(10, './audio_generate/sinesweep.wav')

archivos_data = cargar_rutas()

ri_sint = sint_RI(T60)

h_norm = respuesta_impulso(archivos_data['rutas'][0], archivos_data['rutas'][1])

respuesta_i_norm = func_Conver_log_norm(h_norm)

ri_sint_norm = func_Conver_log_norm(ri_sint)


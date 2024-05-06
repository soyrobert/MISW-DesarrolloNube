#este script esta diseñado para correr la funcion procesar video
#dentro del contenedor de docker
print("inicio")
from moviepy.editor import *
import os
import numpy as np
from funciones_procesar_video import procesar_video


ruta_video_prueba='../src/uploads/videos_sin_editar/video_test.mp4'
ruta_logo='../src/uploads/videos_sin_editar/sample_jpg_image.jpg'
ruta_salida='../src/uploads/videos_editados/video_test_editado.mp4'

procesar_video(ruta_video_prueba,ruta_logo,ruta_salida)
print("fin")
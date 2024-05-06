#este script esta diseñado para correr la funcion por fuera de docker en windows

from moviepy.editor import *
import os
import numpy as np
from funciones_procesar_video import procesar_video

ruta_video_prueba='C:/Proyectos/MISO/MISW-DesarrolloNube/resources/tests/videos/video_test.mp4'
ruta_logo='C:/Proyectos/MISO/MISW-DesarrolloNube/resources/sample_jpg_image.jpg'
ruta_salida='C:/Proyectos/MISO/MISW-DesarrolloNube/resources/tests/videos/video_test_procesado.mp4'

procesar_video(ruta_video_prueba,ruta_logo,ruta_salida)
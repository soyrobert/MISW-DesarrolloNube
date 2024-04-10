from moviepy.editor import *
import os


ruta_video_prueba='C:/Proyectos/MISO/MISW-DesarrolloNube/resources/tests/videos/video_test.mp4'

#check if ruta_video_prueba exists
if not os.path.isfile(ruta_video_prueba):
    print(f"El video de prueba no existe en la ruta especificada: {ruta_video_prueba}")
else:
    print(f"El video de prueba existe en la ruta especificada: {ruta_video_prueba}")

clip=VideoFileClip(ruta_video_prueba).rotate(90)
#save the clip
clip.write_videofile('resources/tests/videos/video_test_rotado.mp4')

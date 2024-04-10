from moviepy.editor import *
import os


ruta_video_prueba='C:/Proyectos/MISO/MISW-DesarrolloNube/resources/tests/videos/video_test.mp4'

#check if ruta_video_prueba exists
if not os.path.isfile(ruta_video_prueba):
    print(f"El video de prueba no existe en la ruta especificada: {ruta_video_prueba}")
else:
    print(f"El video de prueba existe en la ruta especificada: {ruta_video_prueba}")

clip=VideoFileClip(ruta_video_prueba)

# Calculate the width and height for the new aspect ratio of 16:9
new_width = clip.w
new_height = int(new_width * 9 / 16)

# Resize the video clip to the new aspect ratio
resized_clip = clip.resize((new_width, new_height))

#save the clip
clip.write_videofile('resources/tests/videos/video_test_rotado.mp4')

#este escript se puede correr de manera independiente
# para correrlo se deben actualizar las rutas de la seccion de inputs y correr el script desde el cmd

from moviepy.editor import *
import os
import numpy as np

#inputs
ruta_video_prueba='C:/Proyectos/MISO/MISW-DesarrolloNube/resources/tests/videos/video_test.mp4'
ruta_logo='C:/Proyectos/MISO/MISW-DesarrolloNube/resources/sample_jpg_image.jpg'
ruta_salida='C:/Proyectos/MISO/MISW-DesarrolloNube/resources/tests/videos/video_test_procesado.mp4'

#check if ruta_video_prueba exists
def procesar_video(ruta_video_prueba,ruta_logo,ruta_salida):
    '''
    funcion que toma la ruta de un video y del logo y 
    genera el video procesado con las especificaciones del enunciado
    '''
    if not os.path.isfile(ruta_video_prueba):
        return (f"El video de prueba no existe en la ruta especificada: {ruta_video_prueba}")
 
    clip=VideoFileClip(ruta_video_prueba)

    # Calculate the width and height for the new aspect ratio of 16:9
    new_width = clip.w
    new_height = int(new_width * 9 / 16)

    # Resize the video clip to the new aspect ratio
    resized_clip = clip.resize((new_width, new_height))

    image = ImageClip(ruta_logo)

    # Define a function to generate a video frame
    make_frame = lambda t: np.array(image.get_frame(t))

    # Create the video clip
    duracion_imagen = 2
    video_clip_image = VideoClip(make_frame, duration=duracion_imagen)
    
    resized_clip=resized_clip.subclip(0, 20-2*duracion_imagen)

    #join resized_clip and video_clip_image
    final_clip = concatenate_videoclips([video_clip_image, resized_clip,video_clip_image], "compose", bg_color=None, padding=0)

 

    #save the clip
    final_clip.write_videofile(ruta_salida,fps=24)

    return 'el video ha sido procesado correctamente'

if __name__ == "__main__":
    procesar_video(ruta_video_prueba,ruta_logo,ruta_salida)
from moviepy.editor import *
import os
import numpy as np
from conexion_gcp import upload_to_bucket
from google.cloud import storage

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

    #save the clip in gcp
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "idlr-miso-2024-ff17c98a513a.json"
    storage_client = storage.Client()
    blob_name=ruta_salida
    bucket_name='misw4204-202412-drones-equipo5'

    if ruta_salida[0]=="/":
        blob_name=ruta_salida[1:]

    upload_to_bucket(blob_name,ruta_salida,bucket_name,storage_client)

    return 'el video ha sido procesado correctamente'


from moviepy.editor import *
import os
import numpy as np
from fun_interaccion_gcp import upload_to_bucket
from fun_interaccion_gcp import download_from_bucket
from google.cloud import storage

def procesar_video(ruta_video_sin_editar,ruta_logo,ruta_video_editado,storage_client):
    '''
    funcion que toma la ruta de un video y del logo y 
    genera el video procesado con las especificaciones del enunciado
    '''    
    
    #se descarga el video de gcp

    blob_name=ruta_video_sin_editar

    if ruta_video_sin_editar[0]=="/":
        blob_name=ruta_video_sin_editar[1:]

    bucket_name='misw4204-202412-drones-equipo5-entregafinal'
    directory = os.path.dirname(ruta_video_sin_editar)

    if not os.path.exists(directory):os.makedirs(directory)
    
    download_from_bucket(blob_name,ruta_video_sin_editar, 'misw4204-202412-drones-equipo5-entregafinal',storage_client)

    if not os.path.isfile(ruta_video_sin_editar):
        return (f"El video de prueba no existe en la ruta especificada: {ruta_video_sin_editar}")
 
    clip=VideoFileClip(ruta_video_sin_editar)

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
    final_clip.write_videofile(ruta_video_editado,fps=24)

    #close all the clips so that the files can be deleted
    final_clip.close()
    resized_clip.close()
    clip.close()


    #save the clip in gcp
    blob_name=ruta_video_editado
    bucket_name='misw4204-202412-drones-equipo5-entregafinal'

    if ruta_video_editado[0]=="/":
        blob_name=ruta_video_editado[1:]

    resultado_bucket=upload_to_bucket(blob_name,ruta_video_editado,bucket_name,storage_client)

    #erase the local videos
    if os.path.isfile(ruta_video_sin_editar):
        os.remove(ruta_video_sin_editar)
    if os.path.isfile(ruta_video_editado):
        os.remove(ruta_video_editado)

    if resultado_bucket:
        print('el video ha sido procesado correctamente')
    else:
        print('el video no ha sido procesado correctamente')


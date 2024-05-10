#!/usr/bin/env python
import pika, sys, os
import time
import json
from funciones_procesar_video import procesar_video
from google.cloud import pubsub_v1
from sqlalchemy import create_engine

# set parameters
database_ip = os.environ['DATABASE_IP']
#database_ip='34.70.72.147'

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "idlr-miso-2024-ff17c98a513a.json"
topic_name='projects/idlr-miso-2024/topics/tareas_videos'
subscription_name='projects/idlr-miso-2024/subscriptions/tareas_videos-sub'

#conexion a bd
engine = create_engine('postgresql://admin:admin@' + database_ip + ':5432/idlr_db')
conn = engine.connect()


def ejecutar_tarea(message):
    '''
    - funcion que procesa los videos una vez que se recibe un mensaje en la cola task_queue
    - en body debe venir el nombre del video a procesar ubicado en la carpeta de videos sin editar
    - en caso de encontrar el video en la ruta especificada lo procesa y lo guarda en la carpeta de videos editados
    - imprime en consola el nombre del video que se esta procesando
    '''
    message.ack()

    mensaje = message.data

    print(f" [x] Se ha recibido el siguiente mensaje: {mensaje}")
    ruta_video_sin_editar=message.attributes.get('file_path')
    print("ruta video a editar: " + ruta_video_sin_editar)

    
    id_task=message.attributes.get("id_task")

    ruta_logo='sample_jpg_image.jpg'
    ruta_video_editado=ruta_video_sin_editar.replace("videos_sin_editar","videos_editados")
    ruta_video_editado_sinarchivo=ruta_video_editado.replace(ruta_video_editado.split("/")[-1],"")

    if not os.path.exists(ruta_video_editado_sinarchivo):
        os.makedirs(ruta_video_editado_sinarchivo)

    procesar_video(ruta_video_sin_editar,ruta_logo,ruta_video_editado)

    query_actualizar = "UPDATE tasks SET status='processed' WHERE id=" + str(id_task)
    conn.execute(query_actualizar)

    print(" [x] Done")


with pubsub_v1.SubscriberClient() as subscriber:
    
    continuar = True
    while continuar:
        try:
            print('esperando mensajes de la cola')
            future = subscriber.subscribe(subscription_name, ejecutar_tarea)
            future.result(timeout=120)
            
        except Exception as e:
            if type(e).__name__ == 'TimeoutError':
                print('No hubo mensajes timout, se intentará volver a recibir')
                continuar = True
            else:
                print('Error desconocido')
                continuar = False
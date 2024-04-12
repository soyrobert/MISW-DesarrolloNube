#!/usr/bin/env python
import pika, sys, os
import time
from funciones_procesar_video import procesar_video
# read rabbitmq connection url from environment variable
amqp_url = os.environ['AMQP_URL']
url_params = pika.URLParameters(amqp_url)


connection = pika.BlockingConnection(url_params)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for tasks. To exit press CTRL+C')


def ejecutar_tarea(ch, method, properties, body):
    '''
    - funcion que procesa los videos una vez que se recibe un mensaje en la cola task_queue
    - en body debe venir el nombre del video a procesar ubicado en la carpeta de videos sin editar
    - en caso de encontrar el video en la ruta especificada lo procesa y lo guarda en la carpeta de videos editados
    - imprime en consola el nombre del video que se esta procesando
    '''
    print(f" [x] Se ha recibido para procesar el video: {body.decode()}")
    
    ruta_video_sin_editar=body.decode()
    ruta_logo='../src/resources/logo/sample_jpg_image.jpg'
    ruta_video_editado=ruta_video_sin_editar.replace("videos_sin_editar","videos_editados")
    ruta_video_editado_sinarchivo=ruta_video_editado.replace(ruta_video_editado.split("/")[-1],"")

    if not os.path.exists(ruta_video_editado_sinarchivo):
        os.makedirs(ruta_video_editado_sinarchivo)

    procesar_video(ruta_video_sin_editar,ruta_logo,ruta_video_editado)

    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=ejecutar_tarea)

channel.start_consuming()
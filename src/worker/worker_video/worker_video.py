#!/usr/bin/env python
import pika, sys, os
import time
# read rabbitmq connection url from environment variable
amqp_url = os.environ['AMQP_URL']
url_params = pika.URLParameters(amqp_url)


connection = pika.BlockingConnection(url_params)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def procesar_video(ch, method, properties, body):
    '''
    - funcion que procesa los videos una vez que se recibe un mensaje en la cola task_queue
    - en body debe venir el nombre del video a procesar ubicado en la carpeta de videos sin editar
    - en caso de encontrar el video en la ruta especificada lo procesa y lo guarda en la carpeta de videos editados
    - imprime en consola el nombre del video que se esta procesando
    '''
    print(f" [x] Se ha recibido para procesar el video: {body.decode()}")
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=procesar_video)

channel.start_consuming()
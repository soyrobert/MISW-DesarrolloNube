
import os
from google.cloud import pubsub_v1

os.chdir('src/worker/worker_video')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "idlr-miso-2024-ff17c98a513a.json"

topic_name='projects/idlr-miso-2024/topics/tareas_videos'
subscription_name='projects/idlr-miso-2024/subscriptions/tareas_videos-sub'

def callback(message):
    print(message.data)
    message.ack()

with pubsub_v1.SubscriberClient() as subscriber:
    
    continuar = True
    while continuar:
        try:
            print('esperando mensajes')
            future = subscriber.subscribe(subscription_name, callback)
            future.result(timeout=15)
            print('esperando mensajes')
        except Exception as e:
            if type(e).__name__ == 'TimeoutError':
                print('No hay mensajes')
                continuar = True
            else:
                print('Error desconocido')
                continuar = False

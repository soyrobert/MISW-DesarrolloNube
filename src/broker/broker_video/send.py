import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue',durable=True)

channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body='video_test.mp4')
print(" [x] Sent 'video_test.mp4'")

connection.close()
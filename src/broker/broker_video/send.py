import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue',durable=True)

channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body='Hello World2!')
print(" [x] Sent 'Hello World2!'")

connection.close()
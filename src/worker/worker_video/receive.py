#!/usr/bin/env python
import pika, sys, os
# read rabbitmq connection url from environment variable
amqp_url = os.environ['AMQP_URL']
url_params = pika.URLParameters(amqp_url)

def main():
    connection = pika.BlockingConnection(url_params)
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        sys.stdout.write(f" [x] Received {body}\n")
        sys.stdout.flush()  # Ensures the message is flushed immediately

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    sys.stdout.write(' [*] Waiting for messages. To exit press CTRL+C\n')
    sys.stdout.flush()  # Ensures the message is flushed immediately

    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write('Interrupted\n')
        sys.stdout.flush()  # Ensures the message is flushed immediately
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

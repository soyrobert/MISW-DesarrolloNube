# Broker Video

El dockerfile corresponde a la imagen oficial de rabbit encontrada en 

https://github.com/docker-library/rabbitmq/blob/f83b6d92a99e5bc967fcac201ee6439f1a4849c2/3.13/ubuntu/Dockerfile

y descrita en 

https://hub.docker.com/_/rabbitmq

Una vez se tiene corriendo esta imagen en el docker instalandola desde local o con:

docker pull rabbitmq:3-management

se corre el contendedor con

docker run --rm -it -p 15672:15672 -p 5672:5672 --name some-rabbitmq rabbitmq:3-management

la consola se puede acceder con 

http://localhost:15672/ 

y el usuario default guest y contraseña default guest

# Ejemplo de uso con python

Los archivos send.py y receive.py son un ejemplo sencillo de como se puede usar el broker para enviar y recibir un mensaje. Primer se corre el archivo receive con python receive.py y luego el otro archivo con python send.py.

Este ejemplo se encuentra en https://www.rabbitmq.com/tutorials/tutorial-one-python
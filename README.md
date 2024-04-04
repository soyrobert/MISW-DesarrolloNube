# MISW-DesarrolloNube
Repositorio Desarrollo de Software en la nube - MISW 4204

# Stack tecnológico

1. Python 3.10 o superior.
2. Flask Framework: Micro framework web.
3. Flask SQLAlchemy: Una extensión de Flask que agrega soporte para el ORM SQLAlchemy, un 
mapeador relacional de objetos que simplifica la interacción con una base de datos SQL.
4. Flask RESTful: Una extensión de Flask para desarrollar API REST con un patrón de diseño 
orientado a objetos.
5. Flask Marshmallow: Una extensión de Flask que se integra con Marshmallow, una biblioteca de 
Python para la serialización de objetos.
6. Celery: Es una biblioteca de Python para gestionar colas de tareas distribuidas, es decir, nos 
permite trabajar con diferentes tareas y distribuirlas en procesos. 
7. Redis o RabbitMQ: Servicios de mensajería que actúan como intermediarios; los brokers 
enrutan, agregan y permiten crear servicios de publicación/subscripción, comúnmente 
llamados servicios pub/sub.
8. Kafka: Si es de su preferencia puede reemplazar Celery por Kafka. Es importante resaltar que 
esta decisión impacta la arquitectura de solución, pasando de un sistema de cola de mensajes y 
workers a una arquitectura Pub/Sub.
9. Flask JWT Extended: Agrega soporte en el uso de JSON Web Tokens (JWT) a Flask para proteger 
las vistas, la actualización de tokens, entre otras funciones. 
10. Werkzeug: Biblioteca completa de aplicaciones web WSGI. 
11. PostgreSQL: Motor Open Source de base de datos SQL.
12. Gunicorn: Servidor HTTP WSGI para Python y ambientes Unix. 
13. Nginx: Servidor web HTTP de código abierto. Ofrece servicios como proxy inverso, balanceador 
de carga HTTP y proxy de correo electrónico para IMAP, POP3 y SMTP. Se utiliza en conjunto 
con Gunicorn para desplegar en producción aplicaciones web en Flask. 

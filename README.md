# MISW-DesarrolloNube
Repositorio Desarrollo de Software en la nube - MISW 4204

## Stack tecnológico

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


## Estructura de carpetas

* backend: contenedor donde se implementan los servicios con flask
* broker: contenedor con servicio de broker de mensajes para manejar la cola de tareas
* database: contenedor con base de datos postgreSQL
* worker: contenedor de codigo que escucha las tareas y ejecuta el trabajo de procesamiento de video
* nginx: api gateway de los microservicios anteriores


## Instrucciones de ejecución.

### Clonar el repostorio
Para clonar el repositorio:

1. Abra una terminal en un directorio de su preferencia.
2. Ejecute el siguiente comando:
```bash
git clone https://github.com/soyrobert/MISW-DesarrolloNube.git
```

### Ejecutar toda la plataforma:
Para ejecutar toda la plataforma, ubiquese en la raiz del proyecto/repositorio y ejecute los siguientes:

```bash
docker-compose down --rmi all
```

```bash
docker-compose up -d
```
Lo anterior, levantará todos los servicios (_Backend API, BD, Cola de mensajeria, Workers_) necesarios para empezar a consumnirlos.

### Ejecutar y monitorear contenedores individuales

#### Backend API
Para ejecutar el backend API siga las siguientes instrucciones:

1. Abra una terminal bash.
2. Ubiquese en la ruta del backend que es la siguiente: "/MISW-DesarrolloNube/src/backend"
3. Ejecute el comando:

```bash
python3 app.py
```


#### Base de Datos
Para levantar el servicio de BD, siga las instruicciones ubicadas en el readme:

```bash
src/database/README.md
```

Si desea conectarse a la BD para realizar consultas directamente lo puede hacer con los siguientes comandos:

Conectarse al contenedor donde corre la BD con dockder exec
```bash
docker exec -it idlr_db bash
```

Una vez dentro del container conectarse a la BD
```bash
psql -U admin -d idlr_db
```

Realizar las consultas necesarias, por ejemplo ver la tabla de tasks
```bash
idlr_db=# select * from tasks;
 id | user_id |         file_path         |         timestamp          |  status
----+---------+---------------------------+----------------------------+-----------
  1 |       2 | 2024/04/14/videotest2.mp4 | 2024-04-14 01:37:00.114754 | processed
  2 |       2 | 2024/04/14/videotest2.mp4 | 2024-04-14 01:38:58.510803 | processed
  3 |       2 | 2024/04/14/videotest2.mp4 | 2024-04-14 01:43:35.416322 | processed
  4 |       2 | 2024/04/14/videotest2.mp4 | 2024-04-14 01:44:29.038956 | processed
```

### Consumir servicios

#### Registro
Para registrarse como usuario, importe el siguiente request (Curl) en su cliente HTTP preferido:

```curl
curl --location 'http://localhost:8000/api/auth/signup' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "jpuentes",
    "password1": "123abc456",
    "password2": "123abc456",
    "email": "jpuentes@gmail.com"
}'
```

Deberá una respuesta como esta:

```curl
{
    "message": "Usuario creado"
}
```

#### Login
Para loguerse como usuario, importe el siguiente request (Curl) en su cliente HTTP preferido:

```curl
curl --location 'http://localhost:8000/api/auth/login' \
--header 'Content-Type: application/json' \
--data '{
    "username": "jpuentes",
    "password": "123abc456"
}'
```

### Consultar tareas
Para consultar las tareas de procesamientos, importe el siguiente request (Curl) en su cliente HTTP preferido:

**Nota:**  _Debe estar logueado para consumir este servicio._

```curl
curl --location --request GET 'http://localhost:8000/api/tasks' \
--header 'Authorization: Bearer {TOKEN}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "jpuentes",
    "password1": "123abc456",
    "password2": "123abc456",
    "email": "jpuentes@gmail.com"
}'
```



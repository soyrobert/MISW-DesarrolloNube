# MISW-DesarrolloNube
Repositorio Desarrollo de Software en la nube - MISW 4204 del equipo 5 conformado por:

* Maria del Mar Alas Escalante
* Jhon Puentes
* Robert Castro
* Daniel Gamez

## Estructura de carpetas

* backend: contenedor donde se implementan los servicios con flask
* broker: contenedor con servicio de broker de mensajes para manejar la cola de tareas
* database: contenedor con base de datos postgreSQL
* worker: contenedor de codigo que escucha las tareas y ejecuta el trabajo de procesamiento de video
* nginx: api gateway de los microservicios anteriores


## Instrucciones de ejecución.

### Clonar el repositorio
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



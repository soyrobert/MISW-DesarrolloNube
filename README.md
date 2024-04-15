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
La aplicación está principalmente diseñada para correr en Docker por lo que debe tener instalada esta herramienta en su equipo. Para ejecutar toda la plataforma, corra Docker en el aplicativo de escritorio o en la línea de comandos. Una vez Docker esté corriendo ubiquese en la raiz del proyecto/repositorio donde se encuentra el archivo "docker-compose.yaml" y ejecute los siguientes comandos:

```bash
docker-compose down --rmi all
```

```bash
docker-compose up -d
```
Lo anterior, levantará todos los servicios (_Backend API, BD, Cola de mensajeria, Workers_) necesarios para empezar a consumnirlos. Por ejemplo en el aplicativo de escritorio en windows se ve de la siguiente forma una vez corre:

![image](https://github.com/soyrobert/MISW-DesarrolloNube/assets/17055234/82049003-d766-45bf-ad71-224d4849647c)

Si necesita por alguna razon volver a correr la plataforma. Lo recomendado es borrar los contenidos de la carpeta "postgres-data" en la carpeta database y volver a correr los comandos:

```bash
docker-compose down --rmi all
```

```bash
docker-compose up -d
```

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

El consumo de servicios se encuntra documentado en postman:
* [Documentacion Postman](https://documenter.getpostman.com/view/1812580/2sA3Bj7tn4) 
* [Espacio Trabajo Postman](https://www.postman.com/bold-star-394127/workspace/2024-2-ing-soft-nube)

igualmente a continuación los explicamos.

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



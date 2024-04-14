# Worker Video

prerequisito: correr el contenedor de la carpeta "broker_video" con  network="host". Es preferible correr todo el proyecto desde el Docker compose en la raiz del proyecto.


El docker image corre el script de python "worker_video.py", este se conecta al contenedor "broker_video" suponiendo que este ya está corriendo y escucha cuando se genera una tarea de procesamiento de video en la cola "tasks" de Rabbit.Se puede construir el docker image con el comando:

"docker build -t worker_video ."

se corre el docker con el comando:

"docker run --network=host --rm --name worker_video worker_video"

como prerequisito rabbit debe estar corriendo en network="host" de acuerdo con las instrucciones en la carpeta "broker_video".

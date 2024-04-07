prerequisito: correr el contenedor de la carpeta "broker_video" con  network="host".


El docker image corre el script ejemplo de python "receive.py", este se conecta al contenedor "broker_video" suponiendo que este ya está corriendo y escucha cuando se corre el mensaje "Hello World" con el script "send.py". Este "send.py" se puede probar corriendo directamente en la consola de este contender.

se construye el docker image con el comando:

"docker build -t worker_video ."

se corre el docker con el comando:

"docker run --network=host --rm --name worker_video worker_video"

como prerequisito rabbit debe estar corriendo en network="host" de acuerdo con las instrucciones en la carpeta "broker_video"
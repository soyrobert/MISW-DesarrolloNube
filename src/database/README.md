# Contenedor con la BD

En este folder se encuentra un archivo llamado `Dockerfile`, asi mismo un archivo llamado `init.sql` que contiene la BD.

El `Dockerfile` creara una imagen usando de referencia la imagen oficial de PostgressSQL de Docker Hub, copiara el archivo `init.sql` a la imagen del contenedor, y expondra el puerto `5432`

Si la imagen no se ha creado anteriormente, la puede crear con este comando: `docker build -t idlr_db .`

En este caso, el nombre de la imagen sera `idlr_db`.

Puede verificar que la imagen se haya creado con el comando: `docker images`

El output deberia ser algo asi:

```
maria@Marias-MacBook-Pro database % docker images
REPOSITORY          TAG       IMAGE ID       CREATED         SIZE
idlr_db             latest    08ba40f5dbb3   7 seconds ago   417MB
```

Para crear un contenedor nuevo con la imagen descargada, ejecutar el siguiente comando: `docker run -p 5432:5432 -d --name idlr_db_container idlr_db`

En este caso el nombre del contenedor sera `idlr_db_container`, status deberia decir UP, como el siguiente output

Verificar que el contenedor este efectivamente corriendo
```
maria@Marias-MacBook-Pro database % docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS      NAMES
7fec64be31fe   idlr_db   "docker-entrypoint.s…"   8 seconds ago   Up 7 seconds   5432/tcp   idlr_db_container
```

Si quiere acceder a la BD puede crear otro contenedor para eso, ingrese al folder acceso_db Ahora con el archivo Dockerfile se va a crear un contenedor para establecer conexion con la BD

Cree la imagen: `docker build -t connection_db .`

Y corrala con el comando `docker run -p 5050:80 -d --name connection_db_container connection_db`

Verificar que este UP

```
maria@Marias-MacBook-Pro database % docker ps -a
CONTAINER ID   IMAGE           COMMAND                  CREATED         STATUS         PORTS             NAMES
479bd5f031a7   connection_db   "/entrypoint.sh"         9 seconds ago   Up 7 seconds   80/tcp, 443/tcp   connection_db_container
7fec64be31fe   idlr_db         "docker-entrypoint.s…"   9 minutes ago   Up 9 minutes   5432/tcp          idlr_db_container
```

Ingrese a un browser y coloque la direccion `0.0.0.0:5050`
Ingrese con las credenciles `user@domain.com` y contrseña `SuperSecret` (esta en el Dockerfile)
Verifique la IP local de su computador
Cree una conexion nueva al servidor con la ip de su computador y el puerto `5432`

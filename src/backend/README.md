# Contenedor de la aplicación Python/Flask

Iniciar servicio desde la raiz del proyecto 

```bash
   docker-compose build
   docker-compose up
```

Salida esperada de inicio de aplicación

```bash
  * Serving Flask app 'app'
  misw-desarrollonube-backend  |  * Debug mode: on
  misw-desarrollonube-backend  |  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
  misw-desarrollonube-backend  |  * Running on all addresses (0.0.0.0)
  misw-desarrollonube-backend  |  * Running on http://127.0.0.1:8000
```


# Desplegar en cloud run
Ubiquese en el backend
```bash
cd src/backend
```
Construya la imagen y dele un nombre al container
```bash
docker build --tag backend-api .
```

Revise los parametros, cambie el nombre del tag y desplegue ejecutando.
```bash
gcloud run deploy backend-api --source=$(pwd) --platform=managed --region=us-central1 --allow-unauthenticated --max-instances=2 --no-traffic --tag=testv13 --env-vars-file=env.yml
```
import os
import logging
import base64
from flask import Flask,request,jsonify
from google.cloud import storage
from funciones_procesar_video import procesar_video
import json
from sqlalchemy import create_engine,text

bucket_name='misw4204-202412-drones-equipo5-entregafinal'

# Configure logging
logging.basicConfig(level=logging.INFO)

try:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.environ["APIKEYCLOUDSTORAGE"]
except KeyError as e:
    logging.error(" error al iniciar el worker, APIKEYCLOUDSTORAGE no definida")
    logging.error(e)
    exit(1)

try:
    storage_client = storage.Client()
except Exception as e:
    logging.error(" error al iniciar el worker, no se pudo conectar a cloud storage")
    logging.error(e)
    exit(1)

try:
    DB_NAME = os.environ.get('DB_NAME')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DATABASE_IP = os.environ.get('DATABASE_IP')
    conexion= f'postgresql://{DB_USER}:{DB_PASSWORD}@{DATABASE_IP}:5432/{DB_NAME}'
    engine = create_engine(conexion)
    conn = engine.connect()
    logging.info("conexion a la base de datos exitosa")

except Exception as e:
    logging.error(f'error al conectar a la base de datos: {conexion}')
    logging.error(e)


def actualizar_estado_procesado(id_task):
    '''
    - funcion que actualiza el estado de una tarea a procesado
    - recibe el id de la tarea
    - actualiza el estado de la tarea en la base de datos
    '''
    try:
        
        query_actualizar = text(f'UPDATE "public"."tasks" SET status=\'processed\' WHERE id={id_task}')
        conn.execute(query_actualizar) 
        conn.commit()
        
    except Exception as e:
        logging.error(f'error al actualizar el estado de la tarea en la base de datos: {query_actualizar}')
        logging.error(e)
        


def ejecutar_tarea(ruta_video_sin_editar,id_task):
    '''
    - funcion que procesa los videos una vez que se recibe un mensaje en la cola task_queue
    - en body debe venir el nombre del video a procesar ubicado en la carpeta de videos sin editar
    - en caso de encontrar el video en la ruta especificada lo procesa y lo guarda en la carpeta de videos editados
    - imprime en consola el nombre del video que se esta procesando
    '''

    ruta_logo='sample_jpg_image.jpg'
    ruta_video_editado=ruta_video_sin_editar.replace("videos_sin_editar","videos_editados")
    ruta_video_editado_sinarchivo=ruta_video_editado.replace(ruta_video_editado.split("/")[-1],"")

    if not os.path.exists(ruta_video_editado_sinarchivo):
        os.makedirs(ruta_video_editado_sinarchivo)

    procesar_video(ruta_video_sin_editar=ruta_video_sin_editar,
                   ruta_logo=ruta_logo,
                   ruta_video_editado=ruta_video_editado,
                   storage_client=storage_client)

    actualizar_estado_procesado(id_task)

    print(" [x] Done")

def verificar_obtener_parametros(envelope):
    '''
    - funcion que verifica y obtiene los parametros de la solicitud
    - verifica que el mensaje tenga los atributos correctos
    - retorna los datos del mensaje
    '''
    if "message" not in envelope.keys():
        logging.error("error en la solicitud")
        return jsonify({"error": "Request must specify the message"}), 400

    message = envelope['message']

    if "data" not in message.keys() or "attributes" not in message.keys():
        logging.error("error en la solicitud")
        return jsonify({"error": "Message must contain data and attributes"}), 400

    data= message['data']
    data = base64.b64decode(data).decode('utf-8').strip()
    attributes=message['attributes']

    if "file_path" not in attributes.keys() or "id_task" not in attributes.keys():
        logging.error("error en la solicitud")
        return jsonify({"error": "Attributes must contain file_path and id_task"}), 400

    file_path=attributes['file_path']
    id_task=attributes['id_task']

    return data, file_path, id_task

app = Flask(__name__)

@app.route("/",methods=['POST'])
def handle_post():

    envelope = request.get_json()

    if envelope:

        data, file_path, id_task = verificar_obtener_parametros(envelope)
        
        ejecutar_tarea(ruta_video_sin_editar=file_path,id_task=id_task)

        response = {
            "message": "Received data successfully",
            "data": data,
            "file_path": file_path,
            "id_task": id_task
        }
        app.logger.info("mensaje recibido exitosamente, data: " + data)
        return jsonify(response), 200
    else:
        app.logger.error("error en la solicitud")
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

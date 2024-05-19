import os
import logging
import base64
from flask import Flask,request,jsonify
from google.cloud import storage
import json


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "secrets/miso-nube-entregafinal-42b89456bcf3.json"

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/",methods=['POST'])
def handle_post():

    storage_client = storage.Client()
    bucket_name='misw4204-202412-drones-equipo5-entregafinal'

    blobs = storage_client.list_blobs(bucket_name)
    for blob in blobs:
        app.logger.info("conexion exitosa a bucket , archivo: " + blob.name)

    envelope = request.get_json()
    if envelope:
        message = envelope['message']
        data= message['data']
        data = base64.b64decode(data).decode('utf-8').strip()
        response = {
            "message": "Received data successfully",
            "data": data
        }
        app.logger.info("mensaje recibido exitosamente, data: " + data)
        return jsonify(response), 200
    else:
        app.logger.error("error en la solicitud")
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

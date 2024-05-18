import os
import logging
import base64
from flask import Flask,request,jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/",methods=['POST'])
def handle_post():
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

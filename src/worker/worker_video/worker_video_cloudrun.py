import os
import logging

from flask import Flask,request,jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/",methods=['POST'])
def handle_post():
    if request.is_json:
        data = request.get_json()
        response = {
            "message": "Received data successfully",
            "data": data
        }
        app.logger.info("mensaje recibido exitosamente, data: " + str(data))
        return jsonify(response), 200
    else:
        app.logger.error("error en la solicitud")
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

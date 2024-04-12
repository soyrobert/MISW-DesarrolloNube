from flask import Blueprint, request, current_app, jsonify
from werkzeug.utils import secure_filename
from application.models.models import db, Task
import os
from datetime import datetime
import pika

video_blueprint = Blueprint('video', __name__)

amqp_url = os.environ['AMQP_URL']  #variable de entorno desde docker compose
url_params = pika.URLParameters(amqp_url)

def enviar_tarea_worker_video(nombre_video):
    '''
    funcion que se encarga de enviarle el nombre del video como tarea a rabbit
    nombre_video: nombre del video a enviar a rabbit ej: 'video.mp4'
    '''
    connection = pika.BlockingConnection(url_params)
    channel = connection.channel()

    channel.queue_declare(queue='task_queue',durable=True)

    channel.basic_publish(exchange='',
                        routing_key='task_queue',
                        body=nombre_video)
    print(" [x] Sent " + nombre_video)

    connection.close()

@video_blueprint.route('/tasks', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    
    now = datetime.now()
    year, month, day = now.strftime("%Y"), now.strftime("%m"), now.strftime("%d")
    
    project_root = current_app.root_path
    directory_path = os.path.join(project_root, current_app.config['UPLOAD_FOLDER'], year, month, day)
    
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    filepath = os.path.join(directory_path, filename)
    file.save(filepath)
    
    user_id = 1

    new_task = Task(user_id=user_id, status='uploaded')
    db.session.add(new_task)
    db.session.commit()

    enviar_tarea_worker_video(filepath)

    return jsonify({'message': f'Video {os.path.join(directory_path, filename)} uploaded', 'task_id': new_task.id}), 201


@video_blueprint.route('/tasks', methods=['GET'])
def get_tasks():
    print("get tasks")
    # Query users from the database using SQLAlchemy
    tasks = Task.query.all()
    # Serialize users to JSON
    if not tasks:
        return jsonify({'data': "no entries"}), 200

    tasks_list = [{'id': task.id, 'status': task.status} for task in tasks]
    return jsonify({'data': tasks_list}), 200



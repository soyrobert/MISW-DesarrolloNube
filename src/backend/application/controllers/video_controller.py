from flask import Blueprint, request, current_app, jsonify
from werkzeug.utils import secure_filename
from application.models.models import db, Task
import os
from datetime import datetime
import pika
from flask_jwt_extended import jwt_required, get_jwt_identity
import json
from application.models.models import  User

video_blueprint = Blueprint('video', __name__)
amqp_url = os.environ['AMQP_URL']
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
@jwt_required()
def upload_video():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    
    now = datetime.now()
    year, month, day = now.strftime("%Y"), now.strftime("%m"), now.strftime("%d")
    
    project_root = current_app.root_path
    directory_path = os.path.join(project_root, current_app.config['UPLOAD_FOLDER'], year, month, day)
    video_path = os.path.join(year, month, day, filename)
    
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


    user_identity = get_jwt_identity()
    user = User.query.filter_by(username=user_identity).first()

    new_task = Task(user_id=user.id, status='uploaded', file_path=video_path)
    db.session.add(new_task)
    db.session.commit()

    id_task = new_task.id

    video_path2 = os.path.join(year, month, day, str(id_task) + "_" + filename)
    new_task.file_path = video_path2
    db.session.commit()

    filepath = os.path.join(directory_path, str(id_task) + "_" + filename)
    file.save(filepath)

    parametros_tarea_worker={"filepath":filepath,"id_task":id_task}
    
    parametros_tarea_worker_str = json.dumps(parametros_tarea_worker)

    enviar_tarea_worker_video(parametros_tarea_worker_str)

    return jsonify({'message': f'Video {filepath} uploaded', 'task_id': new_task.id}), 201


@video_blueprint.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    """
    Permite recuperar todas las tareas de edición de un usuario autorizado en la aplicación.
    max (int). Parámetro opcional que filtra la cantidad de resultados de una consulta.
    order (int). Especifica si los resultados se ordenan de forma ascendente
    (0) o de forma descendente (1) según el ID de la tarea.
    """
    max = request.args.get('max', default=None)
    order = request.args.get('order', default=None)

    user_identity = get_jwt_identity()
    user = User.query.filter_by(username=user_identity).first()
    print(f"USER ID IS {user.id}")

    tasks = Task.query.filter_by(user_id=user.id)

    if order == '0':
        tasks = tasks.order_by(Task.id.asc())
    elif order == '1':
        tasks = tasks.order_by(Task.id.desc())

    if max:
        tasks = tasks.limit(max)

    # Serialize users to JSON
    if not tasks:
        return jsonify({'data': "no entries"}), 200

    tasks_list = [{'id': task.id, 'status': task.status} for task in tasks]
    return jsonify({'data': tasks_list}), 200

@video_blueprint.route('/tasks/<int:task_id>', methods=['GET'])
@jwt_required()
def get_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    if task.status == "processed":
        file_path = f"/usr/src/app/uploads/videos_editados/{task.file_path}"
    else:
        file_path = ""
    return jsonify({
        'task_id': task.id,
        'timestamp': task.timestamp,
        'status': task.status,
        'file_path': file_path,
        'download': f'http://35.209.73.204:8000/api/video/download/{task.file_path}',
    })


@video_blueprint.route('/tasks/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404

    file_path = task.file_path
    
    project_root = current_app.root_path
    video_sin_editar = os.path.join(project_root, current_app.config['UPLOAD_FOLDER'], file_path)
    video_editado = os.path.join(project_root, current_app.config['UPLOAD_FOLDER_EDIT'], file_path)
    
    if os.path.exists(video_sin_editar):
        os.remove(video_sin_editar)
    if os.path.exists(video_editado):
        os.remove(video_editado)

    db.session.delete(task)
    db.session.commit()

    return jsonify({'message': 'Eliminado', 'file': f'{file_path}', 'Task': task_id}), 200

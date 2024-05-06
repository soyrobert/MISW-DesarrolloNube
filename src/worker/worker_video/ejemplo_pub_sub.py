
import os
from google.cloud import pubsub_v1
os.chdir('src/worker/worker_video')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "idlr-miso-2024-ff17c98a513a.json"

publisher = pubsub_v1.PublisherClient()

#se hace listado de topics
project_id='idlr-miso-2024'
project_path = f"projects/{project_id}"
for topic in publisher.list_topics(request={"project": project_path}):
    print(topic)


topic_name='projects/idlr-miso-2024/topics/tareas_videos'
message='Hola mundo'
data=message.encode('utf-8')
future = publisher.publish(topic_name, data)
future.result()
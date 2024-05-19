from google.cloud import storage
import os
#os.set working directory
#os.chdir('src//worker//worker_video')

#key_path = "secrets/SERVICE_ACCOUNT_KEY"
#set APIKEYCLOUDSTORAGE=C:\Proyectos\MISO\MISW-DesarrolloNube\src\worker\worker_video\secrets\miso-nube-entregafinal-42b89456bcf3.json
# os set environment variable APIKEYCLOUDSTORAGE
#os.environ["APIKEYCLOUDSTORAGE"] = "C:\Proyectos\MISO\MISW-DesarrolloNube\src\worker\worker_video\secrets\miso-nube-entregafinal-42b89456bcf3.json"
#check /secrets/SERVICE_ACCOUNT_KEY exists
#os.path.exists(key_path)

#os print environment variable APIKEYCLOUDSTORAGE
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.environ["APIKEYCLOUDSTORAGE"]

storage_client = storage.Client()
bucket_name='misw4204-202412-drones-equipo5-entregafinal'

#list files in bucket
blobs = storage_client.list_blobs(bucket_name)
for blob in blobs:
    print(blob.name)


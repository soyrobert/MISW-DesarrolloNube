#este es un script de prueba para correr la funcionalidad de conexion a gcp
#se debe guardar en la carpeta src/worker/worker_video las credenciales de gcp

import os



from google.cloud import storage

def upload_to_bucket(blob_name, file_path,bucket_name,storage_client):
    """
    Sube un archivo a un bucket de google cloud storage
    :param blob_name: nombre del archivo en el bucket
    :param file_path: ruta del archivo a subir
    :param bucket_name: nombre del bucket
    :param storage_client: cliente de google cloud storage
    """
    try:
        bucket=storage_client.get_bucket(bucket_name)
        blob=bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    #ejemplo de uso
    os.chdir('src/worker/worker_video')
    os.getcwd()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "idlr-miso-2024-ff17c98a513a.json"
    storage_client = storage.Client()
    file_path=r'C:\Proyectos\MISO\MISW-DesarrolloNube\resources\tests\videos\video_test_1_480_270.mp4'
    blob_name='videos_editados/video_test_1_480_270.mp4'
    bucket_name='misw4204-202412-drones-equipo5'
    upload_to_bucket(blob_name,file_path,bucket_name,storage_client)




#build this with "docker build -t worker_video_cloudrun ."
#run this with "docker run --network="host" --rm worker_video_cloudrun"
# docker run -d -p 8000:8000 --name worker_video_cloudrun -e PORT=8000 worker_video_cloudrun
# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 backend_cloudrun:app

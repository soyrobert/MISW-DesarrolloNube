#build this with "docker build -t worker_video ."
#run this with "docker run --network="host" --rm worker_video"
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

# Run receiver.py when the container launches
CMD ["python", "worker_video_gcp.py"]

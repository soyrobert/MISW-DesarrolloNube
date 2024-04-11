FROM python:3.10-bullseye
WORKDIR /usr/src/app
RUN python -m venv venv
COPY requirements.txt .
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["./venv/bin/python", "app.py"]

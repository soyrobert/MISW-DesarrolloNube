FROM python:3.10

WORKDIR /usr/src/app

RUN python -m venv venv
COPY requirements.txt /usr/src/app/
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

CMD ["venv/bin/python", "app.py"]

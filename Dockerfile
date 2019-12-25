FROM python:3.6

RUN apt-get update

RUN pip install opencv-python numpy

COPY . /app

WORKDIR /app

ENTRYPOINT ["python", "main.py"]

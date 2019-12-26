FROM python:3.6

RUN apt-get update

RUN pip install opencv-python numpy streamlit

COPY . /app

WORKDIR /app

CMD ["streamlit", "run", "app.py"]

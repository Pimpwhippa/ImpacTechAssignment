FROM jupyter/tensorflow-notebook:latest

WORKDIR /flask_jupyter_iris
ADD . /flask_jupyter_iris
RUN pip install -r requirements.txt

#RUN ["apt-get", "update"]
#RUN ["apt-get", "install", "-y", "nano"]
ENV TERM xterm
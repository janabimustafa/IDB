FROM python:3.5-slim
RUN apt-get update && apt-get -y install curl
RUN mkdir /config
COPY ./config/requirements.txt /config/
RUN pip install -r /config/requirements.txt
CMD sh flask-launcher.sh
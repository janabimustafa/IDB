FROM python:3.5-slim
RUN apt-get update && apt-get -y install curl
RUN mkdir /config
ADD ./config/requirements.txt /config/
RUN pip install -r /config/requirements.txt
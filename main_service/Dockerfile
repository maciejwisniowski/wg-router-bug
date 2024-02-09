FROM python:3.11-slim 
RUN mkdir -p -m 0777 /home/app
WORKDIR /home/app

COPY requirements.txt /home/app/requirements.txt
RUN pip install -r /home/app/requirements.txt

COPY ./src .

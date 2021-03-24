FROM python:3.8

ENV PYTHONBUFFERED 1

RUN mkdir /code
WORKDIR /code
RUN pip install pip -U
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
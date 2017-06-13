FROM python:3
ENV PYTHONUNBUFFERED 1
ADD requirements/ /requirements/
RUN pip install -r requirements/production.txt
RUN mkdir /code
WORKDIR /code
ADD . /code/

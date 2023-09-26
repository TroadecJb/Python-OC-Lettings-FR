# pull the official base image
FROM python:3.11.5-alpine3.18

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /code
RUN pip install -r requirements.txt

# copy project
COPY . /code

EXPOSE 8000

CMD python3 manage.py runserver 0.0.0.0:8000
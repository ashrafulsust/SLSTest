# pull official base image
FROM python:3

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1  # Prevents Python from writing pyc files to disc
ENV PYTHONUNBUFFERED 1  #  stdout and stderr will be sent to terminal in real time

# set working directory
WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /app

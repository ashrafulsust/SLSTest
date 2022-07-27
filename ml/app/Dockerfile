FROM tensorflow/tensorflow:latest-py3

# set working directory
WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /app

CMD ["flask", "run" ]
#ENTRYPOINT ["tail", "-f", "/dev/null"]

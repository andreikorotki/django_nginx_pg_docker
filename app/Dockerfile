#pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
COPY ./app/requirements.txt .
RUN pip install -r requirements.txt


# copy entrypoint.sh
# COPY ./app/entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/app/entrypoint.sh"]

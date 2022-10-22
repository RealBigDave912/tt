# set base image (host OS)
FROM python:latest

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY ./src .

# set the token for the telegram bot
ENV TOKEN=""
ENV ALLOWED_USER_ID=""


# command to run on container start
CMD [ "python", "./bot.py" ]

# Base image:
FROM python:3.9

LABEL name="sharp-exp-tool"
LABEL version="0.0.3 - testing"
LABEL description="This image is still in development"


############## Things done by the root user ##############
USER root
# Installation of tools and requirements:

RUN mkdir /app
COPY ./requirements.txt ./app/
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./app README.md LICENSE /app/

# create the user (and group) "chaimeleon"
RUN groupadd -g 1000 chaimeleon && \
    useradd --create-home --shell /bin/bash --uid 1000 --gid 1000 chaimeleon 
# Default password "chaimeleon" for chaimeleon user. 
RUN echo "chaimeleon:chaimeleon" | chpasswd

############### Now change to normal user ################
USER chaimeleon:chaimeleon

# create the directories where some volumes will be mounted
RUN mkdir -p /home/chaimeleon/datasets && \
    mkdir -p /home/chaimeleon/persistent-home && \
    mkdir -p /home/chaimeleon/persistent-shared-folder
    
WORKDIR /home/chaimeleon

ENTRYPOINT ["python","/app/main.py"]




# test it on local machine
# FROM python:3.9

# RUN mkdir /app

# COPY ./requirements.txt ./app/
# RUN pip install --no-cache-dir -r /app/requirements.txt

# COPY ./app README.md LICENSE /app/

# WORKDIR /app
# EXPOSE 8000

# CMD ["python", "main.py"]

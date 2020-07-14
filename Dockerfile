# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:latest
# FROM php:7.2-cli

# If you prefer miniconda:
#FROM continuumio/miniconda3


# RUN echo "deb http://ftp.de.debian.org/debian stretch main" >> /etc/apt/sources.list
# RUN apt-get update
# RUN apt-get install -y php7.0
# RUN apt-get clean -y


LABEL Name=core Version=0.0.1
# EXPOSE 3000

WORKDIR /core
#ADD . /
COPY requirements.txt /core/


RUN apt-get install libpq-dev
# Using pip:
RUN pip install -r requirements.txt

EXPOSE 8000


# CMD ["python3", "-m", "nic_central"]

# Using pipenv:
#RUN python3 -m pip install pipenv
#RUN pipenv install --ignore-pipfile
#CMD ["pipenv", "run", "python3", "-m", "nic_central"]

# Using miniconda (make sure to replace 'myenv' w/ your environment name):
#RUN conda env create -f environment.yml
#CMD /bin/bash -c "source activate myenv && python3 -m nic_central"

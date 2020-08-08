FROM ubuntu:latest

# Install basics
RUN apt-get update -y
RUN apt-get install -y git \
        wget \
        htop \
        vim \
        python3 \
        python3-pip \
        python3-dev \
        build-essential \
        && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

# Force usage of Python3
RUN ln -sf /usr/bin/python3 /usr/bin/python
RUN ln -sf /usr/bin/pip3 /usr/bin/pip
RUN /usr/bin/pip install -U pip

COPY {{cookiecutter.app_name}} ./{{cookiecutter.app_name}}
RUN pip install -r {{cookiecutter.app_name}}/requirements.txt

# Expose the correct ports
EXPOSE 8080

WORKDIR ./

CMD ./{{cookiecutter.app_name}}/run.sh

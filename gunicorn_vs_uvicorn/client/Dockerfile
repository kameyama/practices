FROM python:3.9

WORKDIR /workspace

RUN apt-get update &&\
    apt-get install -y curl hey

COPY ./requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./ /workspace/


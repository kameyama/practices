FROM python:3.9

WORKDIR /workspace

COPY ./requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src /workspace/

ENV WAITING_TIME 0.1




FROM python:3.9

WORKDIR /workspace

COPY ./requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src /workspace/src

ENV WAITING_TIME 0.1

CMD ["gunicorn", "--workers=1", "--bind=0000:8000", "--worker-clas=uvicorn.workers.UvicornWorker","src.main:app"]


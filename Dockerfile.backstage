FROM python:3.12-alpine

COPY requirements.txt /tmp

RUN pip3 install -r /tmp/requirements.txt
RUN apk add curl jq

COPY ./src /src

CMD python /src/app.py

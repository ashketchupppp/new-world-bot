# docker build . --build-args <TOKEN>
FROM python:3.9-buster
ARG TOKEN
ARG MONGO_CONN_STR
ENV TOKEN=$TOKEN
ENV MONGO_CONN_STR=$MONGO_CONN_STR

COPY . /discord-bot

RUN pip3 install -r /discord-bot/requirements.txt

ENTRYPOINT python /discord-bot/src/bot.py $TOKEN $MONGO_CONN_STR
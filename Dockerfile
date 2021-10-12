# docker build . --build-args <TOKEN>
FROM python:3.9-buster
ARG TOKEN
ENV TOKEN=$TOKEN

COPY . /discord-bot

RUN pip3 install -r /discord-bot/requirements.txt

ENTRYPOINT python /discord-bot/src/bot.py $TOKEN
FROM            python:3.9-slim
MAINTAINER      elonmoon@gmail.com

# Langugae, Timezone
ENV             LANG C.UTF-8
ENV             TZ Asia/Seoul
ENV             PYTHONDONTWRITEBYTECODE=1
ENV             PYTHONUNBUFFERED=1

COPY            .   /srv/
WORKDIR         /srv/app

RUN             pip3 install --upgrade pip
RUN             pip3 install -r ../requirements.txt
RUN             python3 manage.py migrate

EXPOSE          8000
CMD             python3 manage.py runserver 0.0.0.0:8000
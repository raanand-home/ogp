FROM python:2.7

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true
Copy requirements.txt .
RUN pip install -r requirements.txt
COPY . /queue
WORKDIR /queue
RUN tar -xvf common.tar



ENTRYPOINT celery -A tasks worker --loglevel=info
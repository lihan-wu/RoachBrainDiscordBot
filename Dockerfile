FROM python:3.10-alpine

COPY ./requirements.txt /requirements.txt
COPY ./app /app


WORKDIR /app
EXPOSE 80

RUN python -m venv /py && \
    apk update && \
    apk add --no-cache py-pip && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /requirements.txt




CMD ["python", "./roach_brain.py", "--host=0.0.0.0:"]
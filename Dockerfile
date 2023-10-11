FROM python:alpine3.17

COPY . .

RUN /py/bin/pip install --upgrade pip
RUN python3 -m pip install -U discord.py
RUN python3 -m pip install -U requests
RUN python3 -m pip install -U python-dotenv
RUN python3 -m pip install -U feedparser


CMD ["python", "./roach_brain.py", "--host=0.0.0.0:"]
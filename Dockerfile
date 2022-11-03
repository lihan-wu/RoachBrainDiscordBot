FROM python:latest

COPY . .

RUN python -m pip install -U discord.py
RUN python -m pip install -U requests
RUN python -m pip install -U python-dotenv


CMD ["python", "./roach_brain.py", "--host=0.0.0.0:"]
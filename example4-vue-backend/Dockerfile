from python:3.9-slim-bullseye

COPY app /app
RUN python /app/setup.py install

ENTRYPOINT cd /app && python main.py
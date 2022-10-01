from python:3.9-slim-bullseye

COPY app /app
RUN python /app/setup.py install

LABEL version="1.0"
# TODO: Add a Volume for persistence across boots
LABEL permissions '\
{\
    "NetworkMode": "host"\
}'
LABEL reasonings = '{\
    "network_mode": "Default option"\
}'
LABEL requirements="core >= 1"

ENTRYPOINT cd /app && python main.py
from python:3.9-slim-bullseye

COPY static /static

LABEL version="1.0"
LABEL permissions '\
{\
    "NetworkMode": "host"\
}'
LABEL reasonings = '{\
    "network_mode": "Default option"\
}'
LABEL requirements="core >= 1"

ENTRYPOINT cd /static && python -m http.server 8346
from python:3.9-slim-bullseye

COPY static /static

LABEL version="1.0"
LABEL permissions '{\
  "ExposedPorts": {\
    "80/tcp": {}\
  },\
  "HostConfig": {\
    "PortBindings": {\
      "80/tcp": [\
        {\
          "HostPort": ""\
        }\
      ]\
    }\
  }\
}'
LABEL reasonings = '{\
    "network_mode": "Default option"\
}'
LABEL requirements="core >= 1"

ENTRYPOINT cd /static && python -m http.server 80
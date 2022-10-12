from python:3.9-slim-bullseye

COPY install.sh /install.sh

RUN /install.sh

COPY app /app
RUN python /app/setup.py install

EXPOSE 80/tcp

LABEL version="1.0.0"
# TODO: Add a Volume for persistence across boots
LABEL permissions '\
{\
  "ExposedPorts": {\
    "80/tcp": {}\
  },\
  "HostConfig": {\
    "Privileged": true,\
    "Binds":["/root/.config:/root/.config"],\
    "PortBindings": {\
      "80/tcp": [\
        {\
          "HostPort": ""\
        }\
      ]\
    }\
  }\
}'
LABEL authors '[\
    {\
        "name": "Willian Galvani",\
        "email": "willian@bluerobotics.com"\
    }\
]'
LABEL docs ''
LABEL company '{\
        "about": "",\
        "name": "Blue Robotics",\
        "email": "support@bluerobotics.com"\
    }'
LABEL readme 'https://raw.githubusercontent.com/Williangalvani/BlueOS-examples/{tag}/example5-gpio-control/Readme.md'
LABEL website 'https://github.com/Williangalvani/BlueOS-examples/'
LABEL support 'https://github.com/Williangalvani/BlueOS-examples/'
LABEL requirements="core >= 1"

ENTRYPOINT pigpiod && cd /app && GPIOZERO_PIN_FACTORY=pigpio python main.py
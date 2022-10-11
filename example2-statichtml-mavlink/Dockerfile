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
LABEL authors '[\
    {\
        "name": "Willian Galvani",\
        "email": "willian@bluerobotics.com"\
    }\
]'
LABEL docs ''
LABEL company='{\
        "about": "",\
        "name": "Blue Robotics",\
        "email": "support@bluerobotics.com"\
    }'
LABEL readme 'https://raw.githubusercontent.com/Williangalvani/BlueOS-examples/{tag}/example2-statichtml-mavlink/Readme.md'
LABEL website 'https://github.com/Williangalvani/BlueOS-examples/'
LABEL support 'https://github.com/Williangalvani/BlueOS-examples/'
LABEL requirements="core >= 1"
ENTRYPOINT cd /static && python -m http.server 80
# Stage 1: Build the frontend
# The platform is hardcoded because bun does not support armv7. The result of this build is architecture agnostic.
FROM --platform=amd64 oven/bun:1 AS frontend_amd64
WORKDIR /frontend
COPY ./frontend/ .
RUN bun install
RUN bun run build

# Stage 2: Build the backend
FROM python:3.11-slim-bookworm AS backend
RUN apt update && apt install -y curl --no-install-recommends && rm -rf /var/lib/apt/lists/*
WORKDIR /backend

COPY ./backend/pyproject.toml .
RUN pip install . --extra-index-url https://www.piwheels.org/simple
COPY ./backend/ .

COPY --from=frontend_amd64 /frontend/dist /frontend

LABEL version="1.0.0"
LABEL permissions='{\
    "ExposedPorts": {\
    "8123/tcp": {}\
    },\
    "HostConfig": {\
    "PortBindings": {\
        "8123/tcp": [\
        {\
            "HostPort": ""\
        }\
        ]\
    }\
    }\
}'
LABEL authors='[\
    {\
        "name": "Nicole Schmidt",\
        "email": "nicole@bluerobotics.com"\
    }\
]'
LABEL company='{\
        "about": "",\
        "name": "Blue Robotics",\
        "email": "support@bluerobotics.com"\
    }'
LABEL type="example"
LABEL readme='https://raw.githubusercontent.com/nicoschmdt/BlueOS-examples/example6/example6-vue-robyn-multistage/README.md'
LABEL links='{\
        "website": "https://github.com/nicoschmdt/BlueOS-examples/",\
        "support": "https://github.com/nicoschmdt/BlueOS-examples/"\
    }'
LABEL requirements="core >= 1.3"


CMD ["python", "main.py"]

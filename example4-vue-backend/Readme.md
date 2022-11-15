# Static Webpage extension

This uses python to serve a static HTML page using Vue and Vuetify as an extension. The static page in this example talks to a simple python backend.

to build:

Enable qemu static support with a docker

```
docker buildx create --name multiarch --driver docker-container --use
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
```

Then build it:

`docker buildx build --platform linux/amd64,linux/arm/v7 . -t YOURDOCKERHUBUSER/YOURDOCKERHUBREPO:latest --output type=registry
`
# Vue3 Webpage extension

This template uses Robyn as a backend API which serves the Vue3 frontend.

## Build

Enable qemu static support with a docker

```
docker buildx create --name multiarch --driver docker-container --use
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
```

Then build it:

`docker buildx build --platform linux/amd64,linux/arm/v7,linux/arm64/v8 . -t YOURDOCKERHUBUSER/YOURDOCKERHUBREPO:latest --output type=registry
`

Then pull it in blueos:

```
red-pill
sudo docker run -d --net=host --name=blueos-example6 --restart=unless-stopped YOURDOCKERHUBUSER/YOURDOCKERHUBREPO:latest
```
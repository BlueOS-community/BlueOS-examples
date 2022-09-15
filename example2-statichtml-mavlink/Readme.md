# Static Webpage extension

This uses python to serve a basic static HTML page as an extension. This example includes MAVLink2Rest communication via http

to build:

Enable qemu static support with a docker

```
docker buildx create --name multiarch --driver docker-container --use
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
```

Then build it:

`docker buildx build --platform linux/amd64,linux/arm/v7 . -t YOURDOCKERHUBUSER/YOURDOCKERHUBREPO:latest --output type=registry
`

Then pull it in blueos:


```
red-pill
sudo docker run -d --net=host --name=blueos-example2 --restart=unless-stopped YOURDOCKERHUBUSER/YOURDOCKERHUBREPO:latest
```
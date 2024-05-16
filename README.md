# Comparative study of community detection methods: Investigating the influence of Network Structure on Measurement Accuracy.

## Prerequisites

1. Install Docker

- [for Mac](https://docs.docker.com/docker-for-mac/install/)
- [for Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- [for Windows](https://docs.docker.com/docker-for-windows/install/)

## Setup

```sh
# build
docker build -t image .

# run container
docker run --name test image

# copy file from container
docker cp test:/src/figure.png ./src

# remove container
docker rm -f test

# build and run
./run.sh
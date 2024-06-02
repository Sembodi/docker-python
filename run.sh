#!/bin/sh

docker build -t image .

docker run --name test image

# docker cp test:/src/figure.png ./src

docker rm -f test
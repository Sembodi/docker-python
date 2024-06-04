#!/bin/sh

docker build -t image .

docker run --name test image

docker cp test:/src/test.csv ./src

docker rm -f test
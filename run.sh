#!/bin/sh

# Build docker image
docker build -t image .

# Run docker image
docker run --name test image

# Create data folder
DIR="/data"
if [ ! -d "$DIR" ]; then
  sudo mkdir -p "$DIR"
fi

# Retrieve data from docker container
docker cp test:/src/data ./data

# Remove docket image
docker rm -f test
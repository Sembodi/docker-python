# Investigating the influence of Network Structure on Measurement Accuracy  

## Prerequisites

1. Install Docker

- [for Mac](https://docs.docker.com/docker-for-mac/install/)
- [for Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- [for Windows](https://docs.docker.com/docker-for-windows/install/)

Or have python installed with the libraries defined in *requirements.txt*.

```sh
# Install the used libraries
pip install -r requirements.txt
```

## Setup

Docker commands:

```sh
# build
docker build -t image .

# run container
docker run --name test image

# copy file from container
docker cp test:/path/to/source/ ./path/to/destination/

# remove container
docker rm -f test
```

Or just run the following script:

```sh
# build and run
./run.sh
```

To use it without docker:
```sh
# Run the program to generate data
python src/main.py

# Run the program to generate figures based on the data
python src/dataProcessing.py

```

## Data collection
This program stores a *csv* file for each graph type combined with the specified measure in the */data* folder.
For all iterations in each file it stores:
  - *LFR graph parameters* that are used to generate the graph and the ground truth (Including the Seed).
  - *NMI score* of the detected communities using generalized Louvain with the specified measure compared to the ground truth.
  - *Computation time* of finding the best partition.   

## Data Analysis

The *dataProcessing.py* program is used to generate figures regarding the NMI score, Quality Score, and computation time.
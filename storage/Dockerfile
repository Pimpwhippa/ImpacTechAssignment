#!/bin/bash
FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    wget \
    nano 
WORKDIR irisdataset
RUN wget https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv \
    wget https://storage.googleapis.com/download.tensorflow.org/data/iris_test.csv

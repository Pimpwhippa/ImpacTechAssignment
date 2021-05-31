FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
	#libopencv-dev \
    python3-pip
	#python3-opencv && \

RUN pip3 install tensorflow && \
    pip3 install numpy pandas sklearn matplotlib seaborn jupyter pyyaml h5py && \
    pip3 install keras --no-deps
    #pip3 install opencv-python && \
    #pip3 install imutils

WORKDIR /model
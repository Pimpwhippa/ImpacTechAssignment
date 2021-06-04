ROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3-pip

RUN pip3 install tensorflow && \
    pip3 install numpy pandas sklearn matplotlib seaborn jupyter pyyaml h5py && \
    pip3 install keras --no-deps

WORKDIR /eval

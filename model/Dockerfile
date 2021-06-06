FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3-pip \
    pip3 install tensorflow && \
    pip3 install numpy pandas sklearn matplotlib seaborn jupyter pyyaml h5py && \
    pip3 install keras --no-deps 
    
COPY create_and_train_model.sh create_and_train_model.sh
    
RUN chmod +rx create_and_train_model.sh
#chmod +x datapreprocess.py create_keras_model.py train_model.py 
CMD /bin/bash -c './create_and_train_model.sh; /bin/bash'
WORKDIR /model

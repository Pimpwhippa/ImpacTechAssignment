FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    curl \
    nano \
    python3-pip 
    #pip3 install kfp --upgrade
    #curl https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl \
    #chmod +x ./kubectl \
    #mv ./kubectl /usr/local/bin
#CMD kubectl get po
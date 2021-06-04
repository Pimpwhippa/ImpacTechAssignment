#!/bin/bash
FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    curl \
    nano 

WORKDIR /irisdataset

COPY curl.sh curl.sh
RUN chmod +rx curl.sh
CMD /bin/bash -c './curl.sh; /bin/bash'

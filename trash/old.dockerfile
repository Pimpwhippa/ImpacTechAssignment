FROM ubuntu:xenial

ENV DRIVE_PATH "/drive"

RUN echo "deb http://ppa.launchpad.net/alessandro-strada/ppa/ubuntu xenial main" >> /etc/apt/sources.list \
 && echo "deb-src http://ppa.launchpad.net/alessandro-strada/ppa/ubuntu xenial main" >> /etc/apt/sources.list \
 && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys F639B041 \
 && apt-get update \
 && apt-get install -yy fuse google-drive-ocamlfuse \
 && apt-get clean all \
 && rm /var/log/apt/* /var/log/alternatives.log /var/log/bootstrap.log /var/log/dpkg.log

RUN useradd -u 1001 -m pimwipa
RUN usermod -a -G root pimwipa

COPY docker-entrypoint.sh .
#COPY docker-entrypoint.sh /usr/local/bin/
RUN ["chmod", "+x", "docker-entrypoint.sh"]
CMD ["./docker-entrypoint.sh"]

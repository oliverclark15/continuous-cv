FROM ubuntu:xenial
ENV DEBIAN_FRONTEND noninteractive


RUN apt-get update -q && apt-get install -qy \
    texlive-full \
    make git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /data
VOLUME ["/data"]

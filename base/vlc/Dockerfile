FROM debian:buster
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get -y upgrade && apt-get install -y vlc && rm -rf /var/lib/apt/lists/*
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser
ENTRYPOINT ["vlc"]
# FROM ubuntu:latest
FROM ghcr.io/inti-cmnb/kicad7_auto_full:latest

LABEL description="KiCad environment"
MAINTAINER Torsten Wylegala <mail@twyleg.de>

ARG DEBIAN_FRONTEND=noninteractive

RUN \
    apt-get update && \
    apt-get install -y \ 
        kicad-packages3d
# 
# 
# RUN wget https://set-soft.github.io/debian/kibot.list && \
#     cp kibot.list /etc/apt/sources.list.d/ && \
#     wget https://set-soft.github.io/debian/kibot.gpg && \
#     cp kibot.gpg /etc/apt/ && \
#     add-apt-repository --yes ppa:kicad/kicad-7.0-releases && \
#     apt-get update && \
#     apt-get install -y \ 
#         kicad \
#         kibot \
#         blender

# CMD ["kibot", "-c", "external/twyleg_kicad_utils/kibot/default.kibot.yaml"]
# CMD ["ls", "-l"]
# CMD ["blender", "--version"]


# docker run -v ./:/root/project/ -w /root/project ghcr.io/inti-cmnb/kicad7_auto_full:latest kibot -c external/twyleg_kicad_utils/kibot/default.kibot.yaml

FROM python:3.12.5-alpine3.20

ARG DEVUSER=devuser
ARG DEVUID=1000
ARG DEVGID=1000

RUN apk add \
        g++ \
        gcc \
        gfortran \
        make \
        cmake \
        pkgconfig \
        git \
        lapack-dev \
        openssh \
        sudo

RUN python3 -m pip install --upgrade pip \
 && python3 -m pip install discord

RUN adduser --uid ${DEVUID} --disabled-password --gecos "" ${DEVUSER} \
    && echo "${DEVUSER} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${DEVUSER}
USER ${DEVUSER}

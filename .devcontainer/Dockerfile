FROM python:3.12.5-alpine3.20

ARG BOTNAME=BindBot
ARG DEVUSER=devuser
ARG DEVUID=1000
ARG DEVGID=1000

# Install everything needed to build Gromacs
RUN apk add \
        g++ \
        gcc \
        gfortran \
        make \
        cmake \
        ccmake \
        pkgconfig \
        git \
        lapack-dev \
        fftw-dev \
        openmpi-dev \
        openssh \
        sudo

# Pip upgrade and discord module install
RUN python3 -m pip install --upgrade pip \
 && python3 -m pip install discord

# Acquire and build gromacs
RUN wget https://ftp.gromacs.org/gromacs/gromacs-2024.2.tar.gz \
 && tar xvf gromacs-2024.2.tar.gz \
 && cd gromacs-2024.2 \
 && cmake -Bbuild -S. -DCMAKE_INSTALL_PREFIX=/workspaces/${BOTNAME}/install \
 && cmake --build build \
 && cmake --build build --target install

# Install gmxapi, pointing it to the fresh gromacs install path
RUN gmxapi_ROOT=/workspaces/${BOTNAME}/install python3 -m pip install gmxapi

# Add non-root user with password-free sudo
RUN adduser --uid ${DEVUID} --disabled-password --gecos "" ${DEVUSER} \
    && echo "${DEVUSER} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${DEVUSER}
USER ${DEVUSER}
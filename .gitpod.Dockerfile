FROM gitpod/workspace-full

# Python Dependencies
ARG PYTHON_VERSION=3.10
ARG PYTHON_VERSION_MINOR=7

RUN pyenv install ${PYTHON_VERSION}.${PYTHON_VERSION_MINOR} && pyenv local ${PYTHON_VERSION}.${PYTHON_VERSION_MINOR}

RUN sudo add-apt-repository ppa:deadsnakes/ppa -y
RUN sudo apt install python${PYTHON_VERSION} -y
RUN sudo apt install python${PYTHON_VERSION}-venv python3-dev portaudio19-dev python3-pyaudio -y
RUN sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python${PYTHON_VERSION} 2
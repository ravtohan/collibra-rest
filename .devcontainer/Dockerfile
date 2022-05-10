# syntax=docker/dockerfile:1
FROM python:3-slim-bullseye

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y upgrade --no-install-recommends \
    && apt-get -y install --no-install-recommends sudo \
	git \
	vim \
	openssh-client \
	gnupg2 \
	ca-certificates \
	apt-transport-https \
	procps \
	man-db \
	manpages \
	manpages-dev \
	curl \
	libpq-dev \
	gcc \
	libc6-dev \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --shell /bin/bash --uid $USER_UID --gid $USERNAME --create-home $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && su - vscode -c "mkdir -p /home/${USERNAME}/.vscode-server/extensions"

USER ${USERNAME}
WORKDIR ${HOME}/workspace
COPY --chown=${USERNAME}:${USERNAME} requirements.txt /tmp/pip-tmp/
RUN pip install --user --disable-pip-version-check --no-cache-dir --no-warn-script-location --no-input --upgrade pip \
    && pip3 install --user --disable-pip-version-check --no-cache-dir --no-input --no-warn-script-location -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp
CMD ["/bin/bash"]

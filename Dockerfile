FROM python:3.14.0-bullseye

WORKDIR /app

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1
ENV PROCESSES 1

RUN apt-get -yq update \
    && apt-get -yq install \
    apt-transport-https \
    ca-certificates \
    curl \
    git \
    gnupg-agent \
    software-properties-common \
    zsh \
    && apt-get -yq autoremove --purge \
    && apt-get -yq autoclean \
    && apt-get -yq clean \
    && rm -rf /var/lib/apt/lists/* \
    && chsh -s $(which zsh) root \
    && sh -c "RUNZSH=no $(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh) --skip-chsh"

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

COPY uv.lock pyproject.toml /app/

RUN uv venv --python 3.14.0 \
    && uv sync

EXPOSE 9999

CMD ["uv", "run", "jupyter", "lab", "--ContentsManager.allow_hidden=True", "--allow-root", "--no-browser", "--ip=0.0.0.0", "--port=9999"]

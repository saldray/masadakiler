FROM silex/emacs:master-ci

RUN apt-get update && \
    apt-get install -y python3 && \
    rm -rf /var/lib/apt/list/*

RUN git clone https://github.com/cask/cask /root/.cask
ENV PATH="/root/.cask/bin:$PATH"

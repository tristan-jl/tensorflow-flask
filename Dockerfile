FROM ubuntu:focal

RUN : \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        software-properties-common \
    && add-apt-repository ppa:deadsnakes \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential \
        nginx \
        python3.9 \
        python3.9-dev \
        python3.9-venv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src

COPY requirements.txt .
ENV PATH=/venv/bin:$PATH
RUN :\
    && python3.9 -m venv /venv \
    && pip --disable-pip-version-check --no-cache-dir install -r requirements.txt

COPY nginx.conf /etc/nginx
COPY gb_model gb_model
COPY app.py uwsgi.ini /src/

CMD service nginx start && uwsgi --ini uwsgi.ini

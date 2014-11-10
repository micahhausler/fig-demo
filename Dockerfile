# Fig Demo in Docker
#
# IMAGE_NAME=${USER}/fig-demo
# docker build -t ${IMAGE_NAME} .
# docker run -it -v $(pwd):/var/www/fig-demo ${IMAGE_NAME} /bin/bash

FROM debian:jessie

MAINTAINER Micah Hausler, <micah.hausler@ambition.com>

RUN apt-get update && \
    apt-get -y install \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" | tee /etc/apt/sources.list.d/pgdg.list && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install \
    curl \
    htop \
    jq \
    libffi-dev \
    libjansson-dev \
    libpcre3-dev \
    libpng12-dev \
    libpq-dev \
    libssl-dev \
    man \
    net-tools \
    netcat-openbsd \
    postgresql-client-9.3 \
    python-dev \
    python-pip \
    sudo \
    vim \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip install \
    uwsgi \
    virtualenv

# We explicitly install Django and IPython since the versions don't change a lot
# and they're our largest dependencies. It just makes rebuilding the image faster
RUN /bin/mkdir -p /var/www/ && \
    virtualenv /var/www/env && \
    /var/www/env/bin/pip install \
    cryptography==0.6.1 \
    Django==1.7.1 \
    pyzmq==14.4.1 \
    werkzeug==0.9.6 \
    tornado==4.0.2 \
    Jinja2==2.7.3 \
    IPython==2.3.0 && \
    mkdir -p /var/www/fig-demo/

###############
# Set up Demo #
###############

WORKDIR /var/www/fig-demo

ADD ./ /var/www/fig-demo

RUN /var/www/env/bin/pip install \
    -r /var/www/fig-demo/requirements/test.txt && \
    chown -R www-data:www-data /var/www

ENV VIRTUAL_ENV /var/www/env
ENV PATH $VIRTUAL_ENV/bin:$PATH
ENV PS1 (env)$PS1
ENV TERM xterm
ENV CLICOLOR 1
ENV HOME /var/www/

EXPOSE 8000
USER www-data

#CMD /var/www/env/bin/python manage.py runserver_plus 0.0.0.0:8000
CMD /usr/local/bin/uwsgi --json uwsgi.json

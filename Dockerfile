FROM python:3.9

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get -y install git python3-pip python3-distutils python3-dev tzdata locales locales-all fonts-wqy-microhei fonts-wqy-zenhei fontconfig libxt6 libxrender1 \
    libjpeg-dev libpng-dev libtiff-dev libwebp-dev libopenjp2-7-dev libfreetype6-dev liblcms2-dev libmagickwand-dev libx11-dev fonts-courier-prime && \
    locale-gen de_DE.UTF-8 &&\
    echo "Europe/Berlin" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

ENV LANG "de_DE.UTF-8"
ENV LANGUAGE "de_DE.UTF-8"
ENV LC_ALL "de_DE.UTF-8"
ENV TZ "Europe/Berlin"

# INSTALL REQUIREMENTS
WORKDIR /tmp
COPY /server/requirements.txt /tmp/requirements.txt
RUN pip install -r requirements.txt

# CREATE USER
RUN groupadd -r -g 1033 worker && \
    useradd -r -g worker -u 1033 -d /home/worker -s /bin/bash worker

USER worker
WORKDIR /home/worker

# COPY FILEs
COPY --chown=worker:worker server /home/worker

# ENTRY
EXPOSE 5000

RUN chmod +x /home/worker/entrypoint.sh

CMD ["sh", "-c", "/home/worker/entrypoint.sh"]

FROM registry.fedoraproject.org/fedora:33

RUN : \
 && dnf -y --refresh update \
 && dnf -y install \
      wget \
      unzip \
      python3-gunicorn \
      python3-flask \
      python3-requests \
      python3-xunitparser \
 && dnf -y clean all \
 && useradd web \
 && :

WORKDIR /app/static

RUN : \
  && wget https://github.com/twbs/bootstrap/releases/download/v5.0.0-beta2/bootstrap-5.0.0-beta2-dist.zip \
  && wget https://github.com/FortAwesome/Font-Awesome/releases/download/5.15.2/fontawesome-free-5.15.2-web.zip \
  && wget https://code.jquery.com/jquery-3.5.1.slim.min.js \
  && unzip bootstrap-5.0.0-beta2-dist.zip \
  && unzip fontawesome-free-5.15.2-web.zip \
  && rm *.zip \
  && mv bootstrap-* bootstrap \
  && mv fontawesome-* fontawesome \
  && :

WORKDIR /app
COPY . /app
EXPOSE 8080
USER web
CMD gunicorn --bind 0.0.0.0:8080 front:app

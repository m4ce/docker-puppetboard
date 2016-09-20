FROM alpine:3.4
MAINTAINER Matteo Cerutti <matteo.cerutti@hotmail.co.uk>

ENV PUPPETBOARD_VERSION "0.2.0"

RUN apk add --no-cache py-pip
RUN pip install puppetboard==$PUPPETBOARD_VERSION gunicorn

COPY run.sh /
RUN mkdir -p /app
COPY settings.py /app/
COPY wsgi.py /app/

EXPOSE 8000

WORKDIR /app
CMD ["/run.sh"]

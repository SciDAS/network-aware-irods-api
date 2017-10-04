FROM python:3
MAINTAINER Michael J. Stealey <michael.j.stealey@gmail.com>

# Set default environment variables
# [connexion/api-server]
ENV CONNEXION_SERVER=''
ENV CONNEXION_DEBUG=True
ENV API_SERVER_HOST=localhost
ENV API_SERVER_PORT=5000
ENV API_SERVER_KEYFILE=''
ENV API_SERVER_CERTFILE=''
# [sys-path]
ENV SYS_PATH_CONTROLLERS=/network-irods/controllers
# [irods]
ENV IRODS_HOST=''
ENV IRODS_PORT=''
ENV IRODS_USER=''
ENV IRODS_PASSWORD=''
ENV IRODS_ZONE=''
ENV IRODS_CLIENT_USER=''
ENV IRODS_CLIENT_ZONE=''

COPY . /network-irods
WORKDIR /network-irods

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

ENTRYPOINT ["/network-irods/docker-entrypoint.sh"]
EXPOSE 5000
CMD ["app.py"]

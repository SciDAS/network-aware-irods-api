#!/usr/bin/env bash

PATH_TO_DOCKERFILE=../server/
LOCAL_PORT=5000
PATH_TO_ENV_FILE=./network-aware-irods.env
PATH_TO_SSL_CERTS=

cd $PATH_TO_DOCKERFILE
docker build -t network-irods .
cd -

docker stop network-irods
sleep 2s
docker rm -fv network-irods
sleep 2s
if [[ ! -z ${PATH_TO_SSL_CERTS} ]]; then
    docker run -d --name network-irods \
        --env-file=${PATH_TO_ENV_FILE} \
        -p ${LOCAL_PORT}:5000 \
        -v ${PATH_TO_SSL_CERTS}:/certs \
        network-irods
    echo "Network Aware iRODS API running over https"
else
    docker run -d --name network-irods \
        --env-file=${PATH_TO_ENV_FILE} \
        -p ${LOCAL_PORT}:5000 \
        network-irods
    echo "Network Aware iRODS API running over http"
fi

exit 0;

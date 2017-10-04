#!/usr/bin/env bash

_set_connection_ini() {
    > ini/connexion.ini
    echo "[connexion]" >> ini/connexion.ini
    if [[ -z ${CONNEXION_SERVER} ]]; then
        echo "server = " >> ini/connexion.ini
    else
        echo "server = "${CONNEXION_SERVER} >> ini/connexion.ini
    fi
    echo "debug = "${CONNEXION_DEBUG} >> ini/connexion.ini
    echo "port = "${API_SERVER_PORT} >> ini/connexion.ini
    if [[ -z ${API_SERVER_KEYFILE} ]]; then
        echo "keyfile = " >> ini/connexion.ini
    else
        echo "keyfile = "${API_SERVER_KEYFILE} >> ini/connexion.ini
    fi
    if [[ -z ${API_SERVER_CERTFILE} ]]; then
        echo "certfile = ">> ini/connexion.ini
    else
        echo "certfile = "${API_SERVER_CERTFILE} >> ini/connexion.ini
    fi
    echo "" >> ini/connexion.ini
    echo "[sys-path]" >> ini/connexion.ini
    echo "controllers = "${SYS_PATH_CONTROLLERS} >> ini/connexion.ini
    echo "" >> ini/connexion.ini
    echo "[irods]" >> ini/connexion.ini
    echo "host = "${IRODS_HOST} >> ini/connexion.ini
    echo "port = "${IRODS_PORT} >> ini/connexion.ini
    echo "user = "${IRODS_USER} >> ini/connexion.ini
    echo "password = "${IRODS_PASSWORD} >> ini/connexion.ini
    echo "zone = "${IRODS_ZONE} >> ini/connexion.ini
    echo "client_user = "${IRODS_CLIENT_USER} >> ini/connexion.ini
    echo "client_zone = "${IRODS_CLIENT_ZONE} >> ini/connexion.ini
}

if [[ "$1" = 'app.py' ]]; then
    # set connexion.ini file
    _set_connection_ini

    # update swagger.yaml file
    if [[ ! -z ${SWAGGER_HOST} ]]; then
        sed -i 's/host: "localhost:5000"/host: \"'${SWAGGER_HOST}'\"/g' /network-irods/swagger/swagger.yaml
    fi

    # run the app
    python app.py
else
    exec "$@"
fi
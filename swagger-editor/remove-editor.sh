#!/usr/bin/env bash

docker stop swagger-editor
docker rm -fv swagger-editor
docker rmi -f swagger-editor
docker rmi -f alpine:3.4  # Version may change over time
rm -rf swagger-editor

exit 0;

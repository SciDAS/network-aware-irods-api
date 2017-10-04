#!/usr/bin/env bash

git clone https://github.com/swagger-api/swagger-editor.git
cd swagger-editor/
docker build -t swagger-editor .
docker run -p 8000:8080 --name swagger-editor swagger-editor &
echo "Swagger Editor running at http://localhost:8000"

exit 0;

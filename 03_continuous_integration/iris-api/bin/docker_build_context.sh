#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"/..

rm -rf ${DIR}/build/docker

mkdir -p ${DIR}/build/docker
mkdir -p ${DIR}/build/docker/resources
mkdir -p ${DIR}/build/docker/models


cp ${DIR}/Dockerfile ${DIR}/build/docker

cp ${DIR}/resources/*.py ${DIR}/build/docker/resources
cp ${DIR}/*.py ${DIR}/build/docker
cp ${DIR}/models/*.sav ${DIR}/build/docker/models
cp ${DIR}/service.yaml ${DIR}/build/docker

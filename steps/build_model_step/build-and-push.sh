#!/bin/bash
#tag::buildandpush[]
IMAGE=gcr.io/compose-flask/build:v1
docker build  -t "${IMAGE}" -f Dockerfile .
docker push "${IMAGE}"
#end::buildandpush[]

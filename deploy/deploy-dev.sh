#!/bin/bash
set -e

echo $GCLOUD_SERVICE_KEY_PRD | base64 --decode -i > ${HOME}/gcloud-service-key.json
gcloud auth activate-service-account --key-file ${HOME}/gcloud-service-key.json

gcloud --quiet config set project $PROJECT_NAME_PRD
gcloud --quiet config set container/cluster $CLUSTER_NAME_PRD
gcloud --quiet config set compute/zone ${CLOUDSDK_COMPUTE_ZONE}
gcloud --quiet container clusters get-credentials $CLUSTER_NAME_PRD

gcloud docker -- push gcr.io/${PROJECT_NAME_PRD}/${DOCKER_REACT_IMAGE_NAME}
gcloud docker -- push gcr.io/${PROJECT_NAME_PRD}/${DOCKER_FLASK_IMAGE_NAME}
kubectl config view
kubectl config current-context
kubectl set image deployment/${KUBE_DEPLOYMENT_REACT_CONTAINER_NAME} ${KUBE_DEPLOYMENT_REACT_CONTAINER_NAME}=gcr.io/${PROJECT_NAME_PRD}/${DOCKER_REACT_IMAGE_NAME}
kubectl set image deployment/${KUBE_DEPLOYMENT_FLASK_CONTAINER_NAME} ${KUBE_DEPLOYMENT_FLASK_CONTAINER_NAME}=gcr.io/${PROJECT_NAME_PRD}/${DOCKER_FLASK_IMAGE_NAME}:latest 
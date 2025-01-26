#!/bin/bash

# Apply blue deployment
kubectl apply -f blue_deployment.yaml

kubectl rollout status deployment/django-messaging-app-blue

kubectl logs -l app=messaging-app,version=blue

# Apply green deployment
kubectl apply -f green_deployment.yaml

kubectl rollout status deployment/django-messaging-app-green

kubectl logs -l app=messaging-app,version=green

#!/bin/bash

set -e

echo "Deploying blue version..."
kubectl apply -f blue_deployment.yaml
kubectl apply -f kubeservice.yaml

echo "Waiting for blue pods to be ready..."
kubectl rollout status deployment/messaging_app-blue

echo "Deploying green version..."
kubectl apply -f green_deployment.yaml

echo "Waiting for green pods to be ready..."
kubectl rollout status deployment/messaging_app-green

echo "Switching service selector to green version..."
kubectl patch service messaging_app-service -p '{"spec":{"selector":{"app":"messaging_app","version":"green"}}}'

echo "Checking logs of green deployment pods..."
green_pods=$(kubectl get pods -l app=messaging_app,version=green -o jsonpath='{.items[*].metadata.name}')
for pod in $green_pods; do
  echo "Logs from pod $pod:"
  kubectl logs $pod | tail -20
done

echo "Blue-green deployment completed successfully!"

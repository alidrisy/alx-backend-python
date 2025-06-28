#!/bin/bash

set -e

SERVICE_URL="http://localhost:31000"   # Adjust this if needed (NodePort of your service)
NAMESPACE=default
DEPLOYMENT_NAME=messaging_app-blue

echo "Applying updated deployment with image version 2.0..."
kubectl apply -f blue_deployment.yaml

echo "Waiting for rolling update to complete..."
kubectl rollout status deployment/$DEPLOYMENT_NAME -n $NAMESPACE &

# Capture rollout status PID to stop later
ROLLOUT_PID=$!

echo "Testing app availability during rollout..."

while kill -0 $ROLLOUT_PID 2> /dev/null; do
  # Send a request, fail allowed but print a dot to show progress
  if curl --silent --fail $SERVICE_URL > /dev/null; then
    echo -n "."
  else
    echo -n "x"
  fi
  sleep 1
done

wait $ROLLOUT_PID

echo -e "\nRolling update finished."

echo "Current pods:"
kubectl get pods -l app=messaging_app,version=blue -n $NAMESPACE

echo "Script complete."

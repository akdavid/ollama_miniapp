#!/bin/bash

# Start the Ollama service
ollama serve &

# Wait for the service to become available
until curl -s http://localhost:11434 > /dev/null; do
  echo "Waiting for Ollama to start...";
  sleep 2;
done;

# Check if the LLM_MODELS variable is set
if [ -z "$LLM_MODELS" ]; then
  echo "LLM_MODELS is not set. Exiting.";
  exit 1;
fi;

# Download the models specified in LLM_MODELS
IFS=',' read -r -a models <<< "$LLM_MODELS"
for model in "${models[@]}"; do
  echo "Pulling LLM model: $model";
  ollama pull "$model" || echo "Failed to pull LLM model: $model";
done;

# Check if the VLM_MODEL variable is set
if [ -n "$VLM_MODEL" ]; then
  echo "Pulling VLM model: $VLM_MODEL";
  ollama pull "$VLM_MODEL" || echo "Failed to pull VLM model: $VLM_MODEL";
fi;

# Wait for all processes to finish
wait

#!/bin/bash

# Fail immediately on errors
set -e

# Start the Ollama service in the background
ollama serve &

# Wait for the service to become available
echo "Starting Ollama service..."
until curl -sf http://localhost:11434 > /dev/null; do
  echo "Waiting for Ollama to start...";
  sleep 2;
done;

# Check if LLM_MODELS is set and not empty
if [ -z "$LLM_MODELS" ]; then
  echo "Error: LLM_MODELS is not set. Exiting.";
  exit 1;
fi;

# Pull specified LLM models
IFS=',' read -r -a models <<< "$LLM_MODELS"
for model in "${models[@]}"; do
  if [[ "$model" =~ ^[a-zA-Z0-9._:-]+$ ]]; then
    echo "Pulling LLM model: $model";
    ollama pull "$model" || echo "Warning: Failed to pull LLM model: $model";
  else
    echo "Error: Invalid model name: $model";
    exit 1;
  fi;
done;

# Pull VLM model if set
if [ -n "$VLM_MODEL" ]; then
  if [[ "$VLM_MODEL" =~ ^[a-zA-Z0-9._:-]+$ ]]; then
    echo "Pulling VLM model: $VLM_MODEL";
    ollama pull "$VLM_MODEL" || echo "Warning: Failed to pull VLM model: $VLM_MODEL";
  else
    echo "Error: Invalid VLM model name: $VLM_MODEL";
    exit 1;
  fi;
fi;

# Wait for all background processes to finish
wait

#!/bin/bash

# Démarrer le service Ollama
ollama serve &

# Attendre que le service soit disponible
until curl -s http://localhost:11434 > /dev/null; do
  echo "Waiting for Ollama to start...";
  sleep 2;
done;

# Vérifier si la variable LLM_MODELS est définie
if [ -z "$LLM_MODELS" ]; then
  echo "LLM_MODELS is not set. Exiting.";
  exit 1;
fi;

# Télécharger les modèles spécifiés dans LLM_MODELS
IFS=',' read -r -a models <<< "$LLM_MODELS"
for model in "${models[@]}"; do
  echo "Pulling model: $model";
  ollama pull "$model" || echo "Failed to pull model: $model";
done;

# Attendre que tous les processus se terminent
wait

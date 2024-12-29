#!/bin/bash

# install ollama
curl -fsSL https://ollama.com/install.sh | sh

# install required python packeges
pip install --upgrade pip
pip install transformers flask ollama


# run ollama
ollama create llama-3 -f Modelfile
nohup ollama run llama-3



export FLASK_RUN_PORT=5000

echo "Installing required Python packages..."


# export port
featurize port export ${FLASK_RUN_PORT}

# start Flask 
export FLASK_APP=app-llama.py
echo "Starting Flask server on 0.0.0.0:${FLASK_RUN_PORT}..."
flask run --host=0.0.0.0 --port=${FLASK_RUN_PORT}

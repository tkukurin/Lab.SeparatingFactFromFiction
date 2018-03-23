#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

docker run --name syntaxnet --rm -ti -p 8888:8888 -d \
    -v "$DIR/data":/data \
    -v "$DIR/syntaxnet":/code \
    -v /home/toni/nlp_data/conll17:/models \
    tensorflow/syntaxnet

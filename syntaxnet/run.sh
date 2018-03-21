#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo $DIR
DATA=$DIR/data
docker run --name syntaxnet --rm -ti -p 8888:8888 -d \
    -v "$DATA":/data \
    -v /home/toni/data/conll17:/models \
    tensorflow/syntaxnet

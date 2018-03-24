#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# "barebones" syntaxnet
#docker run --name syntaxnet --rm -ti -p 8888:8888 -d \
#    -v "$DIR/data":/data \
#    -v "$DIR/syntaxnet":/opt/tensorflow/syntaxnet/examples/local \
#    -v /home/toni/nlp_data/conll17:/models \
#    tensorflow/syntaxnet

# parser with wrapper
docker run -d --rm -it \
    --name syntaxnet-wrap \
    -v "$DIR/data":/data \
    -v "$DIR/syntaxnet":/usr/local/runner \
    -v ~/nlp_data/conll17:/usr/local/tfmodels/ \
    nardeas/tensorflow-syntaxnet

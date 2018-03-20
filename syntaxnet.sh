#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DATA=$DIR/data
docker run --name syntaxnet --rm -ti -p 8888:8888 -d -v"$DATA":/data tensorflow/syntaxnet

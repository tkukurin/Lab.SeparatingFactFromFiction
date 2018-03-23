#!/bin/bash
docker logs syntaxnet | grep localhost -m1 | awk '{$1=$1};1' | xclip -selection c
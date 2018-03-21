#!/bin/bash
docker logs syntaxnet | grep localhost | awk '{$1=$1};1' | xclip -selection c
#!/bin/bash
# Usage: ./script.sh dirname

if [[ -d "$1" ]]; then
  echo "Directory already exists."
else
  mkdir "$1"
  echo "Created!"
fi


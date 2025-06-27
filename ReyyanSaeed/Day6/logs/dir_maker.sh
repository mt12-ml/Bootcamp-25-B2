#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <dirname>"
  exit 1
fi

dirname="$1"

# Check if the directory exists
if [ ! -d "$dirname" ]; then
  mkdir "$dirname"
  echo "The directory '$dirname' has been created."
else
  echo "The directory '$dirname' already exists."
fi


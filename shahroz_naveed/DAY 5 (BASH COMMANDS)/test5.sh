#!/bin/bash
# Usage: ./script.sh filename.txt

if [[ -w "$1" ]]; then
  echo "Hello" >> "$1"
  echo "Appended Hello to $1"
else
  echo "Error: File does not exist or is not writable."
fi

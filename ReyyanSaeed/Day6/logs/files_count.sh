#!/bin/bash

if [ -z "$1" ] || [ ! -d "$1" ]; then
  echo "Usage: $0 directory_path"
  exit 1
fi

for file in "$1"/*; do
  if [ -f "$file" ]; then
    line_count=$(wc -l < "$file")
    echo "The file '$file' has $line_count lines."
  fi
done


#!/bin/bash
# Usage: ./script.sh filename.txt

if [[ -f "$1" ]]; then
  lines=$(wc -l < "$1")
  echo "The file has $lines lines."
else
  echo "File not found."
fi

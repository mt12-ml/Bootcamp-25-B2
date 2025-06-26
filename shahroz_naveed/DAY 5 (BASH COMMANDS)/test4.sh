#!/bin/bash
# Usage: ./script.sh file1.txt file2.txt ...

for file in "$@"
do
  if [[ -f "$file" ]]; then
    echo -n "$file: "
    wc -l < "$file"
  else
    echo "$file: File not found"
  fi
done

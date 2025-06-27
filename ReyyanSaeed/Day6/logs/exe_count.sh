#!bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <dir"
  exit 1
fi

dir="$1"
for file in "$dir"/*; do
    if [ -x "$file" ]; then
        echo "File '$file' is executable."
    else
        echo "File '$file' is not executable or does not exist."
    fi
done




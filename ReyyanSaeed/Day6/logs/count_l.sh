#!/bin/bash

# Check if a filename is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <filename>"
  exit 1
fi

filename="$1"

# Check if the file exists
if [ ! -f "$filename" ]; then
  echo "Error: File '$filename' not found."
  exit 1
fi

# Count the lines using wc -l and store the result
line_count=$(wc -l < "$filename")

# Display the result
echo "The file '$filename' has $line_count lines."

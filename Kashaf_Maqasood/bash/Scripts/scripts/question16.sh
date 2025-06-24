#!/bin/bash

# Check if a filename was provided
if [ -z "$1" ]; then
  echo "Usage: $0 filename"
  exit 1
fi

# Check if the file exists and is writable
if [ -w "$1" ]; then
  echo "Hello" >> "$1"
  echo "'Hello' appended to $1"
else
  echo "Error: File does not exist or is not writable"
  exit 1
fi
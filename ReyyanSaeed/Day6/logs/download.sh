#!/bin/bash


url="$1"
filename=$(basename "$url")

# Download the file
curl -O "$url"

# Check if the download was successful
if [ $? -eq 0 ]; then
  echo "Download successful: $filename"
else
  echo "Download failed."
  exit 1
fi

#!/bin/bash

# Check if a URL was provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL="$1"
FILENAME=$(basename "$URL")

# Download the file
curl -O "$URL"

# Check if curl succeeded
if [ $? -eq 0 ]; then
    echo "✅ Download successful: $FILENAME"
else
    echo "❌ Download failed."
    exit 1
fi
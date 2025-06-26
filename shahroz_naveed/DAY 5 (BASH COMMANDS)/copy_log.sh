#!/bin/bash

# Define the source directory (replace with your mock folder path if not /var/log)
SOURCE_DIR="logs/" 

# Define the backup base directory
BACKUP_BASE_DIR="./backup" # Creates a 'backup' directory in the script's location

# Get the current timestamp in YYYYMMDD_HHMMSS format
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Create the timestamped backup directory
BACKUP_DIR="$BACKUP_BASE_DIR/logs_$TIMESTAMP"
mkdir -p "$BACKUP_DIR"

# Check if the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' does not exist."
    echo "Please create it or modify SOURCE_DIR in the script."
    exit 1
fi

# Copy all .log files from the source to the backup directory
# The -v flag provides verbose output, showing which files are being copied
cp -v "$SOURCE_DIR"/*.log "$BACKUP_DIR/"

echo "Log files copied to: $BACKUP_DIR"

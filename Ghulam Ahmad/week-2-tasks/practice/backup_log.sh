#!/bin/bash

# Set source and destination directories
SOURCE_DIR="./mock_logs"  # Change to "/var/log" for real logs
BACKUP_DIR="./backup"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Get current timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Create a subfolder with the timestamp
DEST_DIR="$BACKUP_DIR/logs_backup_$TIMESTAMP"
mkdir -p "$DEST_DIR"

# Copy all .log files to the backup folder
find "$SOURCE_DIR" -type f -name "*.log" -exec cp {} "$DEST_DIR" \;

echo "Backup completed: $DEST_DIR"

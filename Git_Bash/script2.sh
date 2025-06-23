#!/bin/bash

# Define log file and backup directory
LOG_FILES=("app.log", "system.log", "auth.log")
mkdir backup
BACKUP_DIR="backup/"
BACKUP_FILE="$BACKUP_DIR/$FILE_$(date +%Y%m%d_%H%M%S).log"

# Create backup directory if it doesn't exist
if [ ! -d "$BACKUP_DIR" ]; then
  mkdir -p "$BACKUP_DIR"
fi

# Copy the log file to the backup directory
for file in "${LOG_FILES[@]}"; do
  > BACKUP_FILE="$BACKUP_DIR/${FILE}_$(date +%Y%m%d_%H%M%S).log"
  > cp "$LOG_FILE" "$BACKUP_FILE"

done

# Check if the copy was successful
if [ $? -eq 0 ]; then
  echo "Log file backed up to: $BACKUP_FILE"
else
  echo "Error: Failed to backup log file."
fi

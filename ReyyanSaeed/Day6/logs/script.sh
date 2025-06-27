LOG_FILES=("app.log" "system.log" "auth.log")


for file in "${LOG_FILES[@]}"; do
  > "$file"
done

# Function to generate random IP
random_ip() {
  echo "$((RANDOM % 255)).$((RANDOM % 255)).$((RANDOM % 255)).$((RANDOM % 255))"
}

# Generate fake log entries
for i in {1..50}; do
  TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
  LEVELS=("INFO" "WARNING" "ERROR" "DEBUG")
  USERS=("alice" "bob" "charlie" "root" "admin")
  LEVEL=${LEVELS[$RANDOM % ${#LEVELS[@]}]}
  USER=${USERS[$RANDOM % ${#USERS[@]}]}
  IP=$(random_ip)
  MESSAGE="[$TIMESTAMP] [$LEVEL] User=$USER IP=$IP Action=login"

  # Append to different log files randomly
  TARGET_LOG=${LOG_FILES[$RANDOM % ${#LOG_FILES[@]}]}
  echo "$MESSAGE" >> "$TARGET_LOG"
done

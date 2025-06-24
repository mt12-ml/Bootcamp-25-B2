#!/bin/bash

# Specify the directory name
dir="my_folder"

# Check if the directory exists
if [ ! -d "$dir" ]; then
  mkdir "$dir"
  echo "Created!"
else
  echo "Directory already exists."
fi
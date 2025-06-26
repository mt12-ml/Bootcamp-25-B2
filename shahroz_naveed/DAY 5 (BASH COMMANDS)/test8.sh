#!/bin/bash

for file in *.sh
do
  if [[ -x "$file" ]]; then
    echo "$file is executable"
  else
    echo "$file is not executable"
  fi
done

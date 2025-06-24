#!/bin/bash

for i in {1..10}; do
  if [ "$i" -eq 5 ]; then
    continue  # Skip number 5
  fi
  echo "$i"
dones
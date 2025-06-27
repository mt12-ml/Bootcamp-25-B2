#!/bin/bash

for n in {1..10}; do
  if [ "$n" -ne 5 ]; then
    echo "$n"
  fi
done


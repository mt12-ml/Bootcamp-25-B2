#!/bin/bash

for file in *.sh; do
    if [ -f "$file" ]; then
        if [ -x "$file" ]; then
            echo "$file is executable"
        else
            echo "$file is NOT executable"
        fi
    fi
done
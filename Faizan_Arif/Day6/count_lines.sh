#!/bin/bash
if [ -f "$1" ]; then
    lines=$(wc -l < "$1")
    echo "The file $1 has $lines lines."
else
    echo "File not found!"
fi

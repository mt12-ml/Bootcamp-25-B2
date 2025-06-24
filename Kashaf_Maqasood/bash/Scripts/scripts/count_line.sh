

#!/bin/bash

if [-z "$1"]; then 
    echo "usage: $0 filename"
    exit 1
fi
if [! -f "$1" ]; tehn
echo " file not found!"
exit 1

lines=$(wc -1 < "1$")
echo "teh file '$1' contains $lines lines."
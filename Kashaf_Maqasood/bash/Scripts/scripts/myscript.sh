#!/bin/bash
#check teh filename was provided
if [ -z "$1"]; then
   echo "usage: $0 filename"
   exit 1
fi

#check if the file exist
if [ ! -f "$1"]; then echo "file '$1' not found!"
exit 1

fi
#count and display number of lines
lines=$(wc -1 < "$1")
echo "the  files '$1' contain $lines lines."


#!/bin/bash
if [[ -e "$1" && -w "$1" ]]; then
	echo "Hello" >> "$1"
	echo "Appended hello"
else
	echo "ERROR"
fi

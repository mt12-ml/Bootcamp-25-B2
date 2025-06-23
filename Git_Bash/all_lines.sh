#!/bin/bash
files="$@"
for file in "$@"; do
	wc -l "${file}"
done

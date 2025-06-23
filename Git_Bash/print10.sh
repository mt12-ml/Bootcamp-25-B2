#!/bin/bash
for i in {1..10}; do
	if [[ "${i}" -ne 5 ]]; then
		echo "${i}"
	fi
done

#!/bin/bash
c=10
while [[ $c -ge 1 ]]; do
	echo $c
	c=$((c-1))
	sleep 1
done

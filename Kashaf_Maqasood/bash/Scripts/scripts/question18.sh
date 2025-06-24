#!/bin/bash

count=10
while [ $count -ge 0 ]; do
    echo "$count"
    sleep 1
    ((count--))
done
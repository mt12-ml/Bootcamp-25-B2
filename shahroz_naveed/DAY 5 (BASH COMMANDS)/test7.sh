#!/bin/bash

i=10
while [ $i -ge 0 ]
do
  echo $i
  sleep 1
  ((i--))
done

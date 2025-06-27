#!/bin/bash


for ((i=10; i>0; i--)); do
   sleep 1 &
   echo "$i"
   wait
done


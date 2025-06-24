#!/bin/bash

# Function to calculate square
square() {
    local num=$1
    echo $((num * num))
}

# Call the function with input 4
result=$(square 4)
echo "The square of 4 is: $result"
#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Define the variables to be sent in the POST request
email="test@gmail.com"
subject="I will always be here for PLD"

# Send POST request using curl with variables in the body and display body of response
response=$(curl -s -X POST -d "email=$email&subject=$subject" "$1")

# Display the body of the response
echo "$response"


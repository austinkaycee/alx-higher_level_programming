#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send DELETE request using curl and display body of response
response=$(curl -s -X DELETE "$1")

# Display the body of the response
echo "$response"


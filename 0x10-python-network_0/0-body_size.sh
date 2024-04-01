#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request using curl and get the size of the response body
response=$(curl -s -w "%{size_download}" -o /dev/null "$1")

# Display the size of the response body
echo "Size of the response body: $response bytes"


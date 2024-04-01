#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send GET request using curl with custom header and display body of response
response=$(curl -s -H "X-School-User-Id: 98" "$1")

# Display the body of the response
echo "$response"


#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send GET request using curl and display body of response if status code is 200
response=$(curl -s -w "%{http_code}" -o response_body.txt "$1")

# Extract the status code
status_code=$(tail -n1 response_body.txt)

# Check if status code is 200 and display body
if [ "$status_code" == "200" ]; then
    cat response_body.txt
else
    echo "Error: Non-200 status code received: $status_code"
fi

# Clean up temporary files
rm -f response_body.txt


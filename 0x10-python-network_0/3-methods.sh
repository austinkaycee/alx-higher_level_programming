#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send OPTIONS request using curl and display allowed methods
allowed_methods=$(curl -s -X OPTIONS -I "$1" | grep -i "Allow:" | sed 's/Allow: //I')

# Display the allowed HTTP methods
echo "Allowed HTTP methods for $1: $allowed_methods"


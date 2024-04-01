#!/bin/bash

# Check if the number of arguments provided is correct
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <file>"
    exit 1
fi

# Assign arguments to variables
URL=$1
FILE=$2

# Check if the file exists
if [ ! -f "$FILE" ]; then
    echo "Error: File '$FILE' not found"
    exit 1
fi

# Send POST request with curl
RESPONSE=$(curl -X POST -H "Content-Type: application/json" --data-binary "@$FILE" "$URL")

# Display the response body
echo "$RESPONSE"


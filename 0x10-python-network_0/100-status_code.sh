#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send HEAD request using curl to get only headers
curl -s -I -o /dev/null -w "%{http_code}" "$1"


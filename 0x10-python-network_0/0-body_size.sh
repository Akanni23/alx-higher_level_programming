#!/usr/bin/python3

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to the URL and get the body size
response=$(curl -s -o /dev/null -w "%{size_download}" "$1")

# Check if curl was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to retrieve URL"
    exit 1
fi

# Display the size of the body of the response in bytes
echo "Size of the body: $response bytes"

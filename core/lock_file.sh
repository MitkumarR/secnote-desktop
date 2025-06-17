#!/bin/bash

# Check if file is provided
if [ -z "$1" ]; then
    echo "Usage: ./lock_file.sh <file_path>"
    exit 1
fi

FILE="$1"

# Remove write permissions for everyone
chmod a-w "$FILE"

# Make the file immutable (requires sudo/root)
sudo chattr +i "$FILE"

echo "File locked successfully on Unix."

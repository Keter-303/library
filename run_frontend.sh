#!/bin/bash

# Check for Node.js and npm
if ! command -v node &> /dev/null
then
    echo "Node.js is not installed. Please install Node.js to proceed."
    exit 1
fi

if ! command -v npm &> /dev/null
then
    echo "npm is not installed. Please install npm to proceed."
    exit 1
fi

# Navigate to the frontend directory
SCRIPT_DIR=$(dirname "$0")
cd "$SCRIPT_DIR/frontend"

# Install frontend dependencies
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies..."
    npm install
fi

echo "Starting React frontend server..."
npm start

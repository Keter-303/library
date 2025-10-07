#!/bin/bash

# Check for Python 3
if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed. Please install Python 3 to proceed."
    exit 1
fi

# Navigate to the project root (assuming script is in root)
SCRIPT_DIR=$(dirname "$0")
cd "$SCRIPT_DIR"

# Create and activate virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

# Install backend dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing backend dependencies..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Please create it."
    deactivate
    exit 1
fi

# Navigate to Django project directory
cd library

# Apply migrations
echo "Applying database migrations..."
python manage.py migrate

# Populate database (optional)
if [ -f "../populate_db.py" ]; then
    echo "Populating database with sample data..."
    python ../populate_db.py
else
    echo "populate_db.py not found. Skipping database population."
fi

echo "Starting Django backend server..."
python manage.py runserver

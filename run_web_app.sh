#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Check if LM Studio is running
echo "Checking LM Studio connection..."
curl -s http://localhost:1234/v1/models > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ LM Studio is running"
else
    echo "⚠️  Warning: LM Studio is not running"
    echo "Please start LM Studio and load a model before using the web app"
fi

# Start the web application
echo "Starting web application on http://localhost:5001"
echo "Press Ctrl+C to stop the server"
python web_app.py 
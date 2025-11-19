#!/bin/bash

# Setup script for Cold Mail Generator
echo "Setting up Cold Mail Generator..."

# Check Python version
python_version=$(python3 --version 2>&1 | cut -d" " -f2)
echo "Python version: $python_version"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "⬆Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f "app/.env" ]; then
    echo "Creating environment file..."
    cp app/.env.template app/.env
    echo "Please edit app/.env and add your Groq API key"
fi

echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit app/.env and add your Groq API key"
echo "2. Run: streamlit run app/main.py"
echo "3. Open your browser to the displayed URL"
echo ""
echo "For more information, see README.md"
#!/bin/bash

# Qiskit Environment Setup Script
# This script sets up the Qiskit environment for quantum programming

echo "Setting up Qiskit environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Installing pip..."
    sudo apt-get update
    sudo apt-get install -y python3-pip
fi

# Upgrade pip
echo "Upgrading pip..."
pip3 install --upgrade pip

# Install Qiskit and dependencies
echo "Installing Qiskit and dependencies..."
pip3 install -r requirements.txt

echo "Qiskit environment setup complete!"
echo "You can now run the Qiskit examples in this directory."
echo ""
echo "To get started, try running:"
echo "  python3 hello_world.py"
echo "  python3 quantum_circuits.py"
echo ""
echo "For Jupyter notebooks:"
echo "  jupyter notebook"
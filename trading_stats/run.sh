#!/bin/bash

# Get the directory where the script is located
DIR=$(dirname "$(readlink -f "$0")")
PARENT_DIR=$(dirname "$DIR")

# Set PYTHONPATH to the parent directory
PYTHONPATH=$PARENT_DIR

# Change to the script directory
cd $DIR

# Run the main module
python3 -m trading_stats.main

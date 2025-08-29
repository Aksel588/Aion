#!/usr/bin/env python3
"""
LinkAI-Aion v0.1.6 - Enhanced AI Utilities Library
===================================================

Main entry point for the LinkAI-Aion utility library.
Provides command-line interface and core functionality access.

Author: Aksel Aghajanyan
License: Apache-2.0
Copyright: 2025 LinkAI
"""

# Import the sys module for system-specific parameters and functions
import sys

# Import the CLI module from the aion package for command-line interface functionality
from aion import cli

def main():
    """
    Main entry point for the LinkAI-Aion CLI application.
    
    This function serves as the primary entry point for the application,
    handling command-line argument parsing and delegating to appropriate
    CLI handlers for different utility functions.
    """
    # Call the main function from the CLI module to start the application
    cli.main()

# Standard Python idiom to check if this script is being run directly
if __name__ == "__main__":
    # Execute the main function when the script is run directly
    main()

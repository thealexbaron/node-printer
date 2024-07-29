import shutil
import sys
import os

def remove_directory(directory):
    try:
        shutil.rmtree(directory)
    except OSError as e:
        print(f"Error: {directory} : {e.strerror}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if the directory argument is provided
    if len(sys.argv) < 2:
        print("Usage: python remove_directory.py <directory>")
        sys.exit(1)

    # Get the directory to remove from command line argument
    directory = sys.argv[1]

    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        sys.exit(1)

    # Call the function to remove the directory
    remove_directory(directory)

import hashlib
import os

# Get the current directory
current_dir = os.getcwd()

# Iterate over all files in the current directory
for file_name in os.listdir(current_dir):
    # Check if the file has a .tar.bz2 extension
    if file_name.endswith(".tar.bz2"):
        # Open the file in binary mode
        with open(file_name, "r") as file:
            # Calculate the MD5 hash of the file
            md5_hash = hashlib.md5(file.read()).hexdigest()
            
            # Write the MD5 hash to stdout
            print(file_name, md5_hash)
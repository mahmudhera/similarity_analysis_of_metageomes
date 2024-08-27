import os

def concatenate_files_in_directory(path):
    # List all directories in the specified path
    for directory in os.listdir(path):
        dir_path = os.path.join(path, directory)
        
        # Check if it's a directory and its name starts with "SRS"
        if os.path.isdir(dir_path) and directory.startswith("SRS"):
            output_file = os.path.join(dir_path, f"{directory}.fastq")
            
            # use cat command to concatenate all files in the directory
            os.system(f"cat {dir_path}/*.fastq > {output_file}")
                            
            print(f"Concatenated files in {dir_path} into {output_file}")

# Replace 'your_path_here' with the path where your directories are located
path = '.'
concatenate_files_in_directory(path)

import os
import pandas as pd

# Get the current directory
current_dir = os.getcwd()

df = pd.read_csv('HMASM.csv')
# create a dict: SRS ID -> Reads MD5
srs_to_md5 = dict(zip(df['SRS ID'], df['Reads MD5']))

# Iterate over all files in the current directory
for file_name in os.listdir(current_dir):
    # Check if the file has a .tar.bz2 extension
    if file_name.endswith(".tar.bz2"):
        # Get the SRS ID from the file name
        srs_id = file_name.split('.')[0]
        # call command: md5sum file_name, read the output and split it to get the md5
        md5 = os.popen(f'md5sum {file_name}').read().split()[0]
        # Get the md5 from the dict
        expected_md5 = srs_to_md5[srs_id]
        # Compare the md5s
        if md5 != expected_md5:
            print(f'{file_name} is incorrect')
        else:
            print(f'{file_name} is correct')
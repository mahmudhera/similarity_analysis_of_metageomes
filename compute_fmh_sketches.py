import os
import subprocess

# List all files with extension .fastq in the current directory
fastq_files = [f for f in os.listdir('./concated_fastqs') if f.endswith('.fastq')]

# Set parameters
k = 21
scaled = 1000
seed = 42
n = 16  # threads per file

# Create a list to hold all subprocesses
processes = []

# Spawn processes
for fastq_file in fastq_files:
    sketch_file_name = fastq_file.replace('.fastq', '.sketch')
    cmd = [
        "fracKmcSketch", 
        f"./concated_fastqs/{fastq_file}", 
        sketch_file_name, 
        "--ksize", str(k), 
        "--scaled", str(scaled), 
        "--seed", str(seed), 
        "--fq", 
        "--n", str(n)
    ]
    # Start the process and add it to the list
    process = subprocess.Popen(cmd)
    processes.append(process)

# Wait until all child processes are done
for process in processes:
    process.wait()

print("All processes have finished.")

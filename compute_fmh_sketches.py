import os
import subprocess

# List all files with extension .fastq in the current directory
fastq_files = [f for f in os.listdir('./concated_fastqs') if f.endswith('.fastq')]

# Set parameters
k = 21
scaled = 1000
seed = 42
n = 32  # threads per file

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



"""
Command being timed: "python compute_fmh_sketches.py"
        User time (seconds): 7386.15
        System time (seconds): 2042.89
        Percent of CPU this job got: 12922%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 1:12.96
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 11742360
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 40
        Minor (reclaiming a frame) page faults: 184604998
        Voluntary context switches: 1697864
        Involuntary context switches: 733669
        Swaps: 0
        File system inputs: 0
        File system outputs: 177684368
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0
"""



"""
Command being timed: "sourmash sketch dna concated_fastqs/SRS045127.fastq -p k=21 -o SRS045127.sig"
        User time (seconds): 214.95
        System time (seconds): 2.90
        Percent of CPU this job got: 107%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 3:23.58
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 140868
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 3
        Minor (reclaiming a frame) page faults: 60114
        Voluntary context switches: 1158
        Involuntary context switches: 669
        Swaps: 0
        File system inputs: 0
        File system outputs: 19328
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0
"""
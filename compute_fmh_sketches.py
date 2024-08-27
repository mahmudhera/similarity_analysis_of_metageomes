import os

# list all files with extension .fastq in the current directory
fastq_files = [f for f in os.listdir('./concated_fastqs') if f.endswith('.fastq')]

# k = 21
# scaled = 1000
# seed = 42
# n = 16 threads per file. all files run in parallel

for fastq_file in fastq_files:
    sketch_file_name = fastq_file.replace('.fastq', '.sketch')
    cmd = f"fracKmcSketch ./concated_fastqs/{fastq_file} {sketch_file_name} --ksize 21 --scaled 1000 --seed 42 --fq --n 16 &"
    # execute the command
    os.system(cmd)

# wait for all the sketches to be computed
os.system("wait")
print("All sketches computed!")
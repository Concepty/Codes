import subprocess

def run_cmd(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print("Output:")
    print(stdout.decode('EUC-KR'))
    print("StdOut:")
    print(stderr.decode('EUC-KR'))
"""
# Example usage:
command = "dir"
run_cmd(command)
"""
# debug_controller.py
import subprocess
import sys

def run_debugger(script_path):
    cmd = [sys.executable, "-m", "pdb", script_path]
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Send debugger commands
    commands = [
        "break main",
        "continue",
        "step",
        "print x",
        "step",
        "print y",
        "continue",
        "quit"
    ]
    
    for command in commands:
        process.stdin.write(command + "\n")
        process.stdin.flush()
    
    # Read and print the output
    output, errors = process.communicate()
    print("Debugger output:")
    print(output)
    
    if errors:
        print("Errors:")
        print(errors)

if __name__ == "__main__":
    run_debugger("target_script.py")

# debug_controller.py
import subprocess
import sys

def run_debugger(script_path):
    cmd = [sys.executable, "-m", "pdb", script_path]
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1, universal_newlines=True)
    
    # Send debugger commands
    commands = [
        "b main",
        "c",
        "s",
        "p x",
        "n",
        "p y",
        "s",
        "pp locals()",
        "pp globals()",
        "c",
        "q"
    ]
    
    print("Sending commands to pdb:")
    for command in commands:
        print(f"==> {command}")
        process.stdin.write(command + "\n")
        process.stdin.flush()
        
        # Read and print the output for each command
        while True:
            output_line = process.stdout.readline()
            if not output_line or "(Pdb)" in output_line:
                break
            print(output_line.strip())
    
    # Read any remaining output
    remaining_output, errors = process.communicate()
    if remaining_output:
        print("Remaining output:")
        print(remaining_output)
    
    if errors:
        print("Errors:")
        print(errors)

if __name__ == "__main__":
    run_debugger("target_script.py")

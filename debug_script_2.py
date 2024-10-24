import pdb
import io

def target_function():
    x = 1
    y = 2
    z = x + y
    print("Result:", z)

if __name__ == "__main__":
    # Prepare the command script
    command_script = '\n'.join([
        'b 5',        # Set breakpoint at line 5
        'continue',   # Continue execution until breakpoint
        'print(x)',   # Print value of x
        'print(y)',   # Print value of y
        'next',       # Execute next line
        'print(z)',   # Print value of z
        'continue'    # Continue execution
    ])
    
    # Redirect stdin and stdout
    debugger_input = io.StringIO(command_script)
    debugger_output = io.StringIO()
    
    # Initialize the debugger with redirected input/output
    debugger = pdb.Pdb(stdin=debugger_input, stdout=debugger_output)
    
    # Run the target function under debugger control
    debugger.run('target_function()')
    
    # Retrieve and print the debugger output
    output = debugger_output.getvalue()
    print("Debugger Output:")
    print(output)

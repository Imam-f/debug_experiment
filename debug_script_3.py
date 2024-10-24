import pdb

def target_function():
    x = 1
    y = 2
    z = x + y
    print("Result:", z)

if __name__ == "__main__":
    # Define the debugger commands
    commands = [
        'b 5',       # Set breakpoint at line 5
        'continue',  # Continue execution until breakpoint
        'print(x)',  # Print value of x
        'print(y)',  # Print value of y
        'next',      # Execute next line
        'print(z)',  # Print value of z
        'continue'   # Continue execution
    ]
    
    # Create a Pdb instance and set rcLines
    debugger = pdb.Pdb()
    debugger.rcLines = commands
    
    # Run the target function under debugger control
    debugger.run('target_function()')

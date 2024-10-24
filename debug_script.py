# debug_script.py

import pdb

def debug_target_script():
    # Create an instance of the Pdb class
    debugger = pdb.Pdb()

    # Set breakpoints (optional)
    debugger.set_break('script_to_debug.py', 3)  # Set breakpoint at line 3

    # Start debugging session
    debugger.run('import script_to_debug')


if __name__ == "__main__":
    debug_target_script()

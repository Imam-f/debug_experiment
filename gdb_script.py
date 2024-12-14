import gdb
import json

class AdvancedDebugger:
    def __init__(self, executable, breakpoints=None):
        """
        Initialize the debugger with an executable and optional breakpoints
        
        :param executable: Path to the executable to debug
        :param breakpoints: List of breakpoint specifications
        """
        self.executable = executable
        self.breakpoints = breakpoints or []
        self.captured_values = {}
    
    def set_breakpoints(self):
        """Set breakpoints for the debug session"""
        for bp_spec in self.breakpoints:
            try:
                # Create breakpoint with optional conditions
                bp = gdb.Breakpoint(bp_spec.get('location'))
                
                # Set condition if provided
                if 'condition' in bp_spec:
                    bp.condition = bp_spec['condition']
                
                # Optional commands to execute at breakpoint
                if 'commands' in bp_spec:
                    for cmd in bp_spec['commands']:
                        gdb.execute(cmd)
            
            except Exception as e:
                print(f"Error setting breakpoint {bp_spec}: {e}")
    
    def process_value(self, var_name):
        """
        Process and capture a value from the current context
        
        :param var_name: Name of the variable to process
        :return: Processed value information
        """
        try:
            # Evaluate the variable in the current context
            value = gdb.parse_and_eval(var_name)
            
            # Determine value type and process
            type_code = value.type.code
            processed_value = {
                'name': var_name,
                'type': str(value.type),
                'raw_value': str(value)
            }
            
            # Type-specific processing
            if type_code == gdb.TYPE_CODE_INT:
                processed_value.update({
                    'int_value': int(value),
                    'hex_value': hex(int(value)),
                    'binary_value': bin(int(value))
                })
            
            elif type_code in [gdb.TYPE_CODE_PTR, gdb.TYPE_CODE_ARRAY]:
                # Handle string pointers
                if str(value.type.target()) in ['char', 'const char']:
                    try:
                        processed_value['string_value'] = value.string()
                    except:
                        processed_value['string_value'] = None
            
            elif type_code == gdb.TYPE_CODE_STRUCT:
                # Process struct fields
                processed_value['fields'] = {}
                for field in value.type.fields():
                    try:
                        field_val = value[field.name]
                        processed_value['fields'][field.name] = {
                            'value': str(field_val),
                            'type': str(field_val.type)
                        }
                    except Exception as field_err:
                        processed_value['fields'][field.name] = str(field_err)
            
            return processed_value
        
        except Exception as e:
            return {
                'name': var_name,
                'error': str(e)
            }
    
    def run_debug_session(self, variables_to_track=None):
        """
        Run the full debug session
        
        :param variables_to_track: List of variable names to track
        :return: Captured values during the debug session
        """
        try:
            # Load the executable
            gdb.execute(f"file {self.executable}")
            
            # Set breakpoints
            self.set_breakpoints()
            
            # Prepare tracking of variables
            self.captured_values = {}
            variables_to_track = variables_to_track or []
            
            # Custom Python breakpoint to capture variables
            class ValueCaptureBreakpoint(gdb.Breakpoint):
                def __init__(self, debugger, variables):
                    super().__init__('main')
                    self.debugger = debugger
                    self.variables = variables
                
                def stop(self):
                    # Capture values at this breakpoint
                    for var in self.variables:
                        try:
                            processed_value = self.debugger.process_value(var)
                            self.debugger.captured_values[var] = processed_value
                        except Exception as e:
                            print(f"Error capturing {var}: {e}")
                    
                    # Optional: can add more complex logic here
                    return True  # Stop at this breakpoint
            
            # Create the value capture breakpoint
            ValueCaptureBreakpoint(self, variables_to_track)
            
            # Run the program
            gdb.execute("run")
            
            return self.captured_values
        
        except Exception as e:
            print(f"Debug session error: {e}")
            return None
    
    def save_debug_results(self, output_file='debug_results.json'):
        """
        Save debug results to a JSON file
        
        :param output_file: Path to save the results
        """
        try:
            with open(output_file, 'w') as f:
                json.dump(self.captured_values, f, indent=2)
            print(f"Debug results saved to {output_file}")
        except Exception as e:
            print(f"Error saving debug results: {e}")

# Example usage script for GDB
def debug_example_program():
    # Breakpoint specifications
    breakpoints = [
        {
            'location': 'main',
            'commands': ['print "Entered main"']
        }
    ]
    
    # Initialize debugger
    debugger = AdvancedDebugger(
        executable='./example',  # Replace with your program path
        breakpoints=breakpoints
    )
    
    # Run debug session and track specific variables
    results = debugger.run_debug_session(
        variables_to_track=['x', 'message', 'p']
    )
    
    # Print or process results
    if results:
        print("Captured Values:")
        print(json.dumps(results, indent=2))
    
    # Optionally save results
    debugger.save_debug_results()

# Register with GDB
debug_example_program()

print("Advanced GDB Debugger initialized.")
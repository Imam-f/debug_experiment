import gdb

source_name = "example2.c"

class BreakpointManager:
    @staticmethod
    def simple_function_breakpoint():
        """
        Set a breakpoint at a specific function
        """
        # Break at main function
        gdb.Breakpoint('main')
        
        # Break at a specific named function
        gdb.Breakpoint('calculate_sum')
    
    @staticmethod
    def conditional_breakpoint():
        """
        Set breakpoints with conditions
        """
        # Break only when a specific condition is met
        bp = gdb.Breakpoint('main')
        bp.condition = 'x > 100'
        
        # Another example with multiple conditions
        complex_bp = gdb.Breakpoint('process_user_data')
        complex_bp.condition = 'global_counter < 10 && error_flag == 0'
    
    @staticmethod
    def line_number_breakpoint():
        """
        Set breakpoints at specific source code lines
        """
        # Break at a specific line in a file
        gdb.Breakpoint(f'{source_name}:30')
        
        # Break at multiple specific lines
        gdb.Breakpoint(f'{source_name}:10')
        gdb.Breakpoint(f'{source_name}:20')
    
    @staticmethod
    def regex_function_breakpoint():
        """
        Set breakpoints using regex patterns
        """
        class RegexBreakpoint(gdb.Breakpoint):
            def __init__(self, regex):
                # Use regex to match multiple functions
                super().__init__(regex, type=gdb.BP_BREAKPOINT, internal=False)
            
            def stop(self):
                # Custom stop logic
                frame = gdb.selected_frame()
                func_name = frame.function().name
                print(f"Matched function: {func_name}")
                return True
        
        # Break on all functions starting with 'process_'
        RegexBreakpoint('^process_.*')
    
    @staticmethod
    def temporary_breakpoint():
        """
        Create temporary breakpoints that auto-delete
        """
        # Temporary breakpoint that deletes after first hit
        bp = gdb.Breakpoint('main', temporary=True)
        
        # Another approach with custom temporary behavior
        class OneTimeBreakpoint(gdb.Breakpoint):
            def __init__(self, location):
                super().__init__(location, temporary=True)
                self.hit_count = 0
            
            def stop(self):
                self.hit_count += 1
                if self.hit_count > 1:
                    # Disable after first real stop
                    self.delete()
                return True
        
        OneTimeBreakpoint('critical_section')
    
    @staticmethod
    def hardware_breakpoint():
        """
        Set hardware breakpoints for specific memory addresses
        """
        # Hardware breakpoint on a specific memory address
        class HardwareBreakpoint(gdb.Breakpoint):
            def __init__(self, address):
                # Use hardware breakpoint type
                super().__init__('*' + str(address), 
                                 type=gdb.BP_HARDWARE_BREAKPOINT)
            
            def stop(self):
                print("Hardware breakpoint triggered!")
                return True
        
        # Example: Set hardware breakpoint (address would be from your program)
        # HardwareBreakpoint(0x400abc)
    
    @staticmethod
    def watchpoint_example():
        """
        Create watchpoints to track variable changes
        """
        class VariableWatchpoint(gdb.Breakpoint):
            def __init__(self, variable):
                # Watch for read/write/change of a variable
                super().__init__(variable, type=gdb.BP_WATCHPOINT)
            
            def stop(self):
                # Custom logic when variable is modified
                print("Variable changed!")
                return True
        
        # Watch a specific variable
        VariableWatchpoint('global_counter')
    
    @staticmethod
    def exception_breakpoint():
        """
        Break on exceptions or specific error conditions
        """
        class ExceptionBreakpoint(gdb.Breakpoint):
            def __init__(self):
                # Break on exception handling
                super().__init__('__cxa_throw', internal=False)
            
            def stop(self):
                # Get current frame and exception details
                frame = gdb.selected_frame()
                print("Exception detected!")
                return True
        
        ExceptionBreakpoint()

# Demonstration of how to use these techniques
def setup_debug_breakpoints():
    print("Setting up advanced breakpoints...")
    
    # Demonstrate various breakpoint techniques
    BreakpointManager.simple_function_breakpoint()
    BreakpointManager.conditional_breakpoint()
    BreakpointManager.line_number_breakpoint()
    BreakpointManager.regex_function_breakpoint()
    BreakpointManager.temporary_breakpoint()
    # BreakpointManager.hardware_breakpoint()  # Uncomment with actual address
    BreakpointManager.watchpoint_example()
    BreakpointManager.exception_breakpoint()

# Register with GDB
setup_debug_breakpoints()
print("Advanced breakpoint techniques loaded.")
# script_to_debug.py

def buggy_function(x):
    y = x + 1
    z = y * 2
    return z

if __name__ == "__main__":
    result = buggy_function(10)
    print("Result:", result)

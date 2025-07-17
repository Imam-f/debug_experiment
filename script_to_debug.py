# script_to_debug.py

# run with python -i script_to_debug.py
# or ipython -i script_to_debug.py
# exec(open('script_to_debug.py').read())

# import readline
# readline.write_history_file('my_history.txt')
# ~/.ipython/profile_default/history.sqlite

def buggy_function(x):
    y = x + 1
    z = y * 2
    return z

if __name__ == "__main__":
    result = buggy_function(10)
    print("Result:", result)

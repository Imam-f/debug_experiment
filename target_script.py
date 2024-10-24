# target_script.py
globs = 23

def add(a, b):
    result = a + b
    return result

def main():
    x = 5
    y = 7
    sum_result = add(x, y)
    print(f"The sum of {x} and {y} is {sum_result}")

if __name__ == "__main__":
    main()


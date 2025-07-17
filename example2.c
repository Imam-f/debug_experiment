#include <stdio.h>

// Global variable for watchpoint example
int global_counter = 0;
int error_flag = 0;

// Function for regex breakpoint example
void process_user_data(int x) {
    printf("Processing user data: %d\n", x);
}

// Another function for regex breakpoint
void process_system_data(int y) {
    printf("Processing system data: %d\n", y);
}

int calculate_sum(int a, int b) {
    return a + b;
}

typedef struct hello { int x; } HELLO;
typedef struct there { int x; } THERE;
THERE extract(HELLO x) {
    return (struct there){.x = x.x};
}

int main() {
    int x = 50;
    
    // typedef int HELLO;
    HELLO y = {.x = 3};

    THERE t = {.x = 4};

    HELLO f = extract(x);

    // Trigger various breakpoint scenarios
    global_counter++;
    
    process_user_data(x);
    process_system_data(x + 10);
    
    int sum = calculate_sum(10, 20);
    printf("Sum: %d\n", sum);
    
    return 0;
}
// gcc -g your_program.c -o your_program
#include <stdio.h>

struct Person {
    int age;
    char* name;
};

int main() {
    int x = 42;
    char* message = "Hello, GDB!";
    struct Person p = {30, "John Doe"};
    
    // Breakpoint will be set here
    printf("Debug point reached\n");
    
    return 0;
}
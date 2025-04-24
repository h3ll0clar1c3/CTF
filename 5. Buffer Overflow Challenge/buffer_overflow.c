// File: buffer_overflow.c
#include <stdio.h>
#include <string.h>

void vulnerable_function() {
    char buffer[16];
    printf("Enter some text: ");
    gets(buffer); // Vulnerable function
    printf("You entered: %s\n", buffer);
}

int main() {
    printf("Welcome to the Buffer Overflow Challenge!\n");
    vulnerable_function();
    return 0;
}
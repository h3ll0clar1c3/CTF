// File: reverse_engineering.c
#include <stdio.h>

void print_flag() {
    char flag[] = {67, 84, 70, 123, 114, 101, 118, 101, 114, 115, 101, 95, 102, 108, 97, 103, 125};
    for (int i = 0; i < sizeof(flag); i++) {
        printf("%c", flag[i]);
    }
    printf("\n");
}

int main() {
    printf("Solve the challenge to retrieve the flag!\n");
    return 0;
}
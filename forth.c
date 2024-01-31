#include <stdio.h>
#include <string.h>

#define MAX_INPUT_SIZE 256 // Okay for now I guess.

void execute(char *input_str) {
    printf("Executing: %s\n", input_str);
}

int main() {

    char input_str[MAX_INPUT_SIZE];

    while(1)
    {
        printf("Forth> ");
        fgets(input_str, sizeof(input_str), stdin);
        input_str[strcspn(input_str, "\n")] = '\0'; // Remove newline char.

        if(strcasecmp(input_str, "quit") == 0)
            break;

        execute(input_str);
    }

    return 0;
}

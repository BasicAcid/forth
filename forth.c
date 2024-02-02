#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_INPUT_SIZE 256 // Okay for now I guess.

void execute(char *input_str, size_t str_size)
{
    /* for(size_t i = 0; i < str_size; ++i) */
    /*     printf("%c" , input_str[i]); */

    char *token, *str_copy;

    // Copy the string just in case, as it will be modified by strstep.
    str_copy = strdup(input_str);

    while((token = strsep(&input_str, " ")))
        printf("%s" , token);

    free(str_copy);
}

int
main()
{
    char input_str[MAX_INPUT_SIZE];

    while(1)
    {
        printf("Forth> ");
        fgets(input_str, sizeof(input_str), stdin);
        input_str[strcspn(input_str, "\n")] = '\0'; // Remove newline char.

        if(strcasecmp(input_str, "quit") == 0)
            break;

        execute(input_str, strlen(input_str));
    }

    return 0;
}

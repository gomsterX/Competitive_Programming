#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int
main(int args, char** argv){
    int t;
    scanf("%d", &t);
    getchar();

    for(int i = 0; i < t; i++){
        char* colors = malloc(100);
        int amber = 0;
        int brass = 0;

        gets(colors);
        for(int j = 0; j < strlen(colors); j++){
            if(colors[j] == 'a')
                amber++;
            else if(colors[j] == 'b')
                brass++;
        }
        if(amber < brass)
            printf("%d\n", amber);
        else
            printf("%d\n", brass);

        free(colors);
    }

}

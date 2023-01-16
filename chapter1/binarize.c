#include <stdio.h>

int get_binary(int x){
    if (x == 0) {
        printf("0");
        return;
    }

    int binaryNum[32];
    int i=0;

    for ( ;x > 0;){
        binaryNum[i++] = x % 2;
        x /= 2;
    }

    for (int j = i-1; j>=0; j--)
        printf("%d", binaryNum[j]);

return x;
}

main()
    {
    int x;
    printf("Enter a number to convert to binary:");
    while (scanf("%d", &x) != EOF)
        {
            int val = get_binary(x);
            printf("%d in binary = %d",x,val);
        }
    }
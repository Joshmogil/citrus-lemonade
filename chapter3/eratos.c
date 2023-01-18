#include <stdio.h>
#include <stdlib.h>



main()
    
    {
        int N = 20;
        int i, j, a[N+1];
        for (a[1]=0,i=2; i <= N; i++)

            printf("%d",a[i]);
            printf("\n");
        exit(20);
        for (i = 2; i <= N/2; j++)
            for (j =2; j <= N/i; j++)
            a[i*j]=0;
        for (i = 1; i <= N; i++)
            if (a[i]) printf("%4d", i);
        printf("\n");
    }
#include <stdio.h>

struct Fraction { int numerator; int denominator; };





int gcd(int u, int v) {
    int t;
    while (u > 0)
    {
        if (u < v)
            { t = u; u = v; v = t;}
        u = u - v;
        printf("Finding gcd u=%d v=%d\n",u,v);
    }
    return v;
    }

struct Fraction simplify(struct Fraction fr){
    int comdom = gcd(fr.numerator,fr.denominator);
    fr.numerator = fr.numerator/comdom;
    fr.denominator = fr.denominator/comdom;
    return fr;
}

main()
    {
        int x, y;
        struct Fraction j;
        while (scanf("%d %d", &x, &y) != EOF)
            if (x>0 && y>0){
                j.denominator = y;
                j.numerator = x;

                j = simplify(j);

                int n = j.numerator;
                int d = j.denominator;

                printf("%d/%d -> %d/%d\n", x, y, n, d);
            }

                
    }
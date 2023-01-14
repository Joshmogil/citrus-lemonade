#include <stdio.h>

struct Fraction { int numerator; int denominator; };

struct Fraction gcd(int u, int v) {
    struct Fraction fr;
    fr.numerator=u;
    fr.denominator=v;
    // trying to simplify a fraction here

    while (fr.denominator > 0)
        {
            fr.denominator = fr.denominator-fr.numerator;
        }

    printf("%d",fr.denominator);
    return fr;
    }
main()
    {
        int x, y;
        struct Fraction j;
        while (scanf("%d %d", &x, &y) != EOF)
            if (x>0 && y>0)

                j = gcd(x,y);
                int n = j.numerator;
                int d = j.denominator;

                printf("%d %d %d/%d\n", x, y, n, d);
    }
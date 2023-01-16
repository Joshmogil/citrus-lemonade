#include <stdio.h>

int gcd3(int x, int y, int z){

    int s = 1;
    while (x != y != z){
        if (x < y && x < z){ s = x;}
        if (y < x && y < z){ s = y;}
        if (z < x && z < y){ s = z;}
        while (x > s){
            x = x - s;
        }
        while (y > s){
            y = y - s;
        }
        while (z > s){
            z = z - s;
        }
        printf("%d, %d , %d \n", x , y, z);
    }
    


}

main() {
    gcd3(10, 20, 30);

}
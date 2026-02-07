#include <stdio.h>
#include <stdlib.h>

int addDigits(int num) {
    int sum=0;
    while(num>9){
        sum=0;
        while(num!=0){
            int d;
            d=num%10;
            sum+=d;
            num/=10;
        }
        num=sum;
    }
    return num;
}

int main(int argc, char *argv[]) {
    int n = (argc > 1) ? atoi(argv[1]) : 0;
    if (argc == 1 && scanf("%d", &n) != 1) return 1;
    printf("%d\n", addDigits(n));
    return 0;
}
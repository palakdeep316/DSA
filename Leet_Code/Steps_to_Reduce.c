#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
int numberOfSteps(int num) {
    int step=0;
    while(num!=0){
        if (num%2==0){
            step+=1;
            num/=2;
        }
        else{
            step+=1;
            num-=1;
        }
    }
    return step;
}
int main(int argc, char *argv[]) {
    long val = 0;
    if (argc > 1) {
        char *end;
        val = strtol(argv[1], &end, 10);
        if (*end != '\0') {
            fprintf(stderr, "Invalid integer argument\n");
            return 1;
        }
    } else {
        printf("Enter a non-negative integer: ");
        if (scanf("%ld", &val) != 1) return 1;
    }
    if (val < 0 || val > INT_MAX) {
        fprintf(stderr, "Value out of range\n");
        return 1;
    }
    int n = (int)val;
    int steps = numberOfSteps(n);
    printf("Number of steps to reduce %d to zero: %d\n", n, steps);
    return 0;
}
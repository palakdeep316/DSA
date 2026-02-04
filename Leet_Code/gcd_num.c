#include <stdio.h>
#include <stdlib.h>

int gcdOfOddEvenSums(int n) {
    int so=0, se=0;
    int gcd=0;
    for(int i=1;i<=n;i++){
        so+=(2*i-1);
        se+=(2*i);
        if (so%i==0 && se%i==0){
            gcd=i;
        }
    }
    return gcd;
}

int main(int argc, char *argv[]) {
    long n = 0;
    if (argc > 1) {
        char *end;
        n = strtol(argv[1], &end, 10);
        if (*end != '\0') {
            fprintf(stderr, "Invalid integer argument\n");
            return 1;
        }
    } else {
        printf("Enter n (positive integer): ");
        if (scanf("%ld", &n) != 1) {
            fprintf(stderr, "Invalid input\n");
            return 1;
        }
    }

    if (n <= 0) {
        fprintf(stderr, "n must be a positive integer\n");
        return 1;
    }

    int result = gcdOfOddEvenSums((int)n);
    printf("GCD for n=%ld is %d\n", n, result);
    return 0;
}
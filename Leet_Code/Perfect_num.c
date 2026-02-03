#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool checkPerfectNumber(int num) {
    if (num <= 1)
        return false;

    int sum = 1;   // 1 is always a divisor

    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            sum += i;

            if (i != num / i)
                sum += num / i;
        }
    }
    return (sum==num);
}

int main(int argc, char *argv[]) {
    long input = 0;
    if (argc > 1) {
        input = atol(argv[1]);
    } else {
        printf("Enter a positive integer: ");
        if (scanf("%ld", &input) != 1) return 1;
    }

    if (input <= 0) {
        printf("Please enter a positive integer.\n");
        return 1;
    }

    if (checkPerfectNumber(input))
        printf("%ld is a perfect number.\n", input);
    else
        printf("%ld is not a perfect number.\n", input);

    return 0;
}
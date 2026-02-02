#include <stdio.h>

int sumOfTheDigitsOfHarshadNumber(int x) {
    int sum_d = 0;
    int org = x;

    while (x != 0) {
        int d = x % 10;
        sum_d += d;
        x /= 10;
    }

    if (org % sum_d == 0)
        return sum_d;
    else
        return -1;
}

int main() {
    int x;
    printf("Enter a number: ");
    scanf("%d", &x);
    int result = sumOfTheDigitsOfHarshadNumber(x);
    if (result != -1)
        printf("Harshad Number -Sum of digits = %d\n", result);
    else
        printf("Not a Harshad Number ✖\n");

    return 0;
}
#include <stdio.h>
#include <stdbool.h>

bool isUgly(int n)
{
    while (n > 0)
    {
        if (n % 2 == 0)
            n = n / 2;
        else if (n % 3 == 0)
            n = n / 3;
        else if (n % 5 == 0)
            n = n / 5;
        else
            return n == 1;
    }
    return false;
}

int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);

    if (isUgly(n))
        printf("%d is an Ugly number\n", n);
    else
        printf("%d is NOT an Ugly number\n", n);

    return 0;
}

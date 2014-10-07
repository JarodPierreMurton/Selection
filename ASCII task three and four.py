#Jarod Pierre Murton
#ASCII Task 3
#6/10/14

string = int(input("Please input an 8 bit binary string: "))

#completely roamed google for 'python parity code' searched both odd and even
#the was code but far beyond my comprehension
#here is some code that i found:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
#include <stdio.h>
 
/* Parity testing using bitwise AND.
 */
static void parity_and(int n)
{
    if (n & 1)
        printf("%i is odd\n", n);
    else
        printf("%i is even\n", n);
}
 
/* Parity testing using the modulus operator.
 */
static void parity_mod(int n)
{
    if (n % 2)
        printf("%i is odd\n", n);
    else
        printf("%i is even\n", n);
}
 
int main(void)
{
    int n = 132469;
    int m = 132470;
 
    printf("Parity testing using modulus operator\n");
    parity_mod(n);
    parity_mod(m);
    printf("Parity testing using bitwise AND\n");
    parity_and(n);
    parity_and(m);
 
    return 0;
}


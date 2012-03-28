#include <stdio.h>

int main(void)
{
	int a = 1919;
	int *b = &a;
	int **c = &b;
	printf("&c : %d\n", &c);
	printf("c : %d\n", c);
	printf("*c : %d\n", *c);
	printf("**c : %d\n", **c);
	getchar();
	return 0;
}

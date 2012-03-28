#include <stdio.h>
int main(void)
{
	int *a = &a;
	printf("a == *a ifadesinin dogruluk degeri : %d\n", (a == *a));
	getchar();
	return 0;
}

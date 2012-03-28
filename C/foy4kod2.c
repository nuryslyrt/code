#include <stdio.h>

int main()
{
	char *dizi5 = "istambul";
	printf("dizi5 eski deger : %s\n", dizi5);
	char *dizi6 = "istanbul";
	dizi5 = dizi6;
	printf("dizi5 yeni deger : %s\n", dizi5);
	getchar();
return 0;
}

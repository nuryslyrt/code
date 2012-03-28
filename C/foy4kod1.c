#include <stdio.h>
int main()
{
	char dizi1[] ="yonca";
	char * dizi2 ="yonca";
	char dizi3[] ="yonca";
	char * dizi4 ="yonca";

	printf("dizi1 : %s\ndizi2 : %s\n\n", dizi1, dizi2);
	getchar();
	
	dizi2 = dizi1;
	dizi2[0] = 'g';
	printf("dizi1 : %s\ndizi2 : %s\n\n", dizi1, dizi2);
	getchar();
	
	printf("dizi3 : %s\ndizi4 : %s\n\n", dizi3, dizi4);
	getchar();
	
	dizi3 = dizi4;
	dizi3[3] = 'g';
	printf("dizi3 : %s\ndizi4 : %s\n\n", dizi3, dizi4);
	getchar();
	
	return 0;
}

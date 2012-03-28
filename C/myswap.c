#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int main(void)
{
	myswap();
}

int myswap(void) 
{
	char *str;
	int t;

	str = (char *) malloc(sizeof(char));

	if(!str) 
	{
		printf("yine bekleriz.\n");
        exit(1);
	}
	
	printf("String nerde: ");
	scanf("%s", str);

	for (t = strlen(str)-1; t >= 0; t--)
		putchar(str[t]);	
	printf("\n");
	free (str);

	return 0;
}

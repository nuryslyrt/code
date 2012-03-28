#include <stdio.h>
#include <string.h>

int main()
{
	int a=0,b=0,c=0;
	char cumle[9999],kontrol[9999];

	puts("stringi gir bakalim\n");
	scanf("%s", cumle);
	b = strlen(cumle);

	for(a=b-1;a>=0;a--)
	{
		kontrol[c] = cumle[a];
		c++;
	}
	if(!strcmp(cumle,kontrol))
		printf("Bunlar aynilar bence!\n");
	else
		printf("Olmamış ki yazinca böyle\n ", puts(kontrol));
	return 0;
}

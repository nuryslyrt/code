#include <stdio.h>
#include <string.h>
int main(void)
{
	char metin[] = "Kugu, ordekgiller ailesine ait, iri ve beyaz su kusu turlerinin ortak adidir.";
	int ulama = 0, i = 0;
	char *sesli = "aeiouAEIOU";
	char *sessiz = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
	while (metin[i+2] != '\0')
	{
		if ( (strchr(sessiz, (int)metin[i]) != NULL) && (metin[i+1]==' ') && (strchr(sesli, (int)metin[i + 2]) != NULL))
			ulama ++;
		i++;
	}
	printf("Ulama sayisi : %d\n", ulama);
	getchar();
	return 0;
}


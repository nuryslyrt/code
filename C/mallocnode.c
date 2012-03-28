#include <stdio.h>
#include <stdlib.h>

#define DUGUM_SAYISI 10000

struct dugum {
	int i;
	struct dugum *sonraki;
};
typedef struct dugum DUGUM;

DUGUM *dugum_ekle(DUGUM *yigin, int i);
DUGUM *yeni_dugum(void);


DUGUM *dugum_ekle(DUGUM *yigin, int i)
{
	DUGUM *yeni_dugum;
	if((yeni_dugum = (DUGUM *) malloc(sizeof(DUGUM))) == NULL)
	{
		printf("Bellek ayirmada problem!\n");
		exit(1);
	}
	
	yeni_dugum->i = i;
	yeni_dugum->sonraki = yigin;
	yigin = yeni_dugum;
	
	return yeni_dugum;
}

DUGUM *yeni_dugum()
{
	DUGUM *yeni = NULL;
	
	if((yeni = (DUGUM *) malloc(sizeof(DUGUM))) == NULL)
	{
		printf("Bellek ayirmada problem!\n");
		exit(1);
	}
	yeni->sonraki = NULL;
	
	return yeni;
}

int main()
{
	DUGUM *yigin = NULL;

	yigin = dugum_ekle(yigin, 5);
	yigin = dugum_ekle(yigin, 7);
	yigin = dugum_ekle(yigin, 8);
	return yigin;
}


#include <stdio.h>

void KaresiniYaz(int sayi)
{
	printf("\n%d sayisinin karesi : %d\n", sayi, sayi*sayi);
}

void KupunuYaz(int sayi)
{
	printf("\n%d sayisinin kupu : %d\n", sayi, sayi*sayi*sayi);
}

void Islem(int s, void (*fonkPtr)(int))
{
	fonkPtr(s);
}

int main(void)
{
	Islem(5, KaresiniYaz);
	Islem(7, KupunuYaz);
	getchar();
	return 0;
}



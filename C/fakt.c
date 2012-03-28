#include <stdio.h>

int main(void)
{
	int sayi;
    int sonuc = 1;

	printf("faktoriyeli bulunacak sayi: ");
	scanf("%d", &sayi);

	if (sayi == 0)
		printf("%d! = %d\n", sayi, 1);
	else
	{
		printf("%d ! = ", sayi);

		while (0 < sayi)
		{
			sonuc *= sayi;
			sayi -= 1;
		}

		printf("%d\n", sonuc);
	}
    getchar();
	return 0;
}

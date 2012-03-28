#include <stdio.h>
// DikdPrizm adinda; tamsayi turunde "en", "boy" ve "yukseklik" alt alanlarina
// sahip bir tur tanimlayiniz.
typedef struct {
	int en;
	int boy;
	int yukseklik;
} DikPrizm;
int hacim(DikPrizm * DdP)
{
	int sonuc = (DdP->en) * (DdP->boy) * (DdP->yukseklik);
	return sonuc;
}
int alan(DikPrizm * DdP)
{
	int sonuc = 2 * ((DdP->en) * (DdP->boy)) + 2 * ((DdP->yukseklik) * (DdP->boy)) + 2 * ((DdP->yukseklik) * (DdP->en));
	return sonuc;
}
int main(void)
{
	DikPrizm x;
	x.en = 3;
	x.boy = 4;
	x.yukseklik = 5;
// Tamamlayiniz. x' in "en" degeri 3, "boy" degeri 4,
// "yukseklik" degeri ise 5 olmalidir.
	printf("Eni %d birim, boyu %d birim, yuksekligi %d birim olan dikdortgenler prizmasinin ", x.en, x.boy, x.yukseklik);
	printf("alani %d birimkare, ", alan(&x));
	printf("hacmi ise %d birimkuptur.", hacim(&x));
	getchar();
	return 0;
}

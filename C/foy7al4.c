#include <stdio.h>
void Yap1(void)
{
	printf("1 numarali is yapildi!\n\n");
}
void Yap2(void)
{
	printf("2 numarali is yapildi!\n\n");
}
void Yaptir(void(* ptr1) (void))
{
	printf("Yaptir --> ");
	ptr1();
}
void YaptiranaYaptir(void(* ptr2) (void(*) (void)), void(* ptr3) (void))
{
	printf("YaptiranaYaptir --> ");
	ptr2(ptr3);
}
int main(void)
{
	YaptiranaYaptir(Yaptir, Yap1);
	Yaptir(Yap2);
	Yap1();
	getchar();
return 0;
}


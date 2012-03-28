#include<stdio.h>

int main()
{

        int enuzunluk =0;
        int boyuzunluk =0;
        char karakter=0;
        int i=0;
        int j=0;

        printf("Seklini cizmek istediginiz Dörtgenin en ve boy uzunlugunu giriniz: ");
        scanf("%d%d",&enuzunluk,&boyuzunluk);
        printf("\n\n");

        karakter=218; /*sol üst köse */
        printf("%c",karakter);

        karakter=196; /*üst düz yatay çizgi*/
        for(i=0;i<enuzunluk;i++)
        {
        printf("%c",karakter);
        }
        karakter=191; /*sag köseyi ciziyoruz*/
        printf("%c\n",karakter);
         /*gövdenin orta kısmı */
        for(i=0;i<boyuzunluk;i++)
        {
         karakter=179;   /*sol dik çizgi*/
         printf("%c",karakter);
         karakter=32;   /*bosluk*/
         for(j=0;j<enuzunluk;j++)  /*aradaki çizgi*/
         {
         printf("%c",karakter);
         }
         karakter=179;  /*sag dik çizgi*/
         printf("%c\n",karakter);
         }
         karakter=192;     /*sol alt kenar çizgisi*/
         printf("%c",karakter);
         karakter=196;    /*düz yatay çizgi*/
         for(i=0;i<enuzunluk;i++)
         {
         printf("%c",karakter);
         }
         karakter=217;   /*sag kenar*/
         printf("%c\n",karakter);



       getchar();  getchar();
       return 0;
}

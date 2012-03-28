#include <stdio.h>

int asal()
{
     int s;
     int i;
     
        printf (" Bir sayi giriniz: ");
        scanf  ("%d", &s);

        printf ("\n");
        for (i = 2; s != 1; i ++)
        {	
            if (s % i == 0)
          {
              s /= i;
              printf ("%5d", i);
              i --;
           }
        }
      printf ("\n");
      return 0;
}

int main() 
{
	asal();
}


#include <stdio.h>
#include <ctype.h>

int main(void)
{
   int c;
   c=getchar();
   while((c=getchar()) != EOF)
   {
      if (islower(c))
        c = toupper(c);
   putchar(c);
   }
   return 0;
}
    

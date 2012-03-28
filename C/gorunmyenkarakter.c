#include <stdio.h>

int main(void)
{    
     char c ;
     int n = 0;
     
     c = getchar();
     if ( 'c' >= 10 ||  'c' <= 32){
       
       n++;
       
      }
      printf("%d karakterlerin sayisi: " , n); 
     return 0;

}        
    
             

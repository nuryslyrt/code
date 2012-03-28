#include <stdio.h>

int main()
{
	float x = 99999999.0;
	float *f;
	int *i;
	char *c;
	
	f = (float *)malloc(sizeof(float));
	f = &x;
	
	i = (int *)f;
	c = (char *)f;
	
	 
  printf("x in degeri %f \n", x);
  printf("f nin gosterdigi yer %f\n", *f);
  printf("i nin gosterdigi yer %d\n" , *i);
  printf("c nin gosterdigi yer %d\n", *c);
    
  return 0;
}
	
	
	

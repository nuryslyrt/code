#include <stdio.h>  
#include <stdlib.h>

int main()
{
	float *f;
	int *i ;
	char *c;
	f = (float*) malloc(1*sizeof(float));
	*f = 7.12;
    i = (int *)f ;
	c = (char *)f ; 
	f = (float *)f ;
	
	printf("%f %d %d",*f, *i, *c);
}

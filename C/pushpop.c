#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int *p;
int *tos;
int *bos;

void push(int i);
int pop(void);

int main(void)
{
	int *t;
	t = (int *) malloc(MAX * sizeof(int));
	if(!t)
	{
		printf("Allocation Failure");
		exit(1);
	}
	tos = t;
	bos = t + MAX-1;
	
	push(1);
	push(2);
	push(10);
	push(20);
	push(6);
	pop();
	
	return *t;
}

void push(int i)
{
	if(p > bos)
	{
		printf("Stack Full\n");
		return;
	}
	*p = i;
	p++;
}

int pop(void)
{
	p--;
	if(p < tos) 
	{
		printf("Stack Underflow\n");
		return 0;
	}
	return *p;
}
	
	
	
	
	
	
	

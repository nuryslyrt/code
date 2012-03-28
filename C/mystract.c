#include<stdio.h>
#include<string.h>

int j, x, y;

char a[50], *q, b[50];

void strekle(char *p) {
	
    int i;
    for(i = 0; i < strlen(q)+1; i++)
        *(p+i) = *(q+i);                         
}
int main() {
	
    printf("1.Metin(bosluk koymayin!) => ");
    scanf("%s", a);
    
    x = strlen(a);          
    printf("Eklenecek Metin(bosluk koymayin!) => ");
    scanf("%s", b);
    
    y = strlen(b);
    q = &b[0];
    strekle(&a[x+1]);
    for(j=0; j <= x+y; j++)
        printf("%c", a[j]);               
    return 0;                               
}    

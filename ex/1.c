#include <stdio.h>
static int c=2;
int func (int a);

int main(void){
int a, b;
a=1;
b=func(a+c);
printf("%d\n", b+c)


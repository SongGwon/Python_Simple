//============================================================================
// Name        : 0.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>


int main() {
	int a,b,ave;
	puts("input 2 int\n");
	scanf("%d %d", &a, &b);
	ave = (a+b)/2;
	printf("ave의 부호반전한 값은%d", -ave);
	return 0;
}

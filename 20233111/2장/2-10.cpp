//============================================================================
// Name        : 0.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>


int main() {

	int a,b;

	puts("2개의 정수를 입력하세요.");
	printf("정수 a : "); scanf("%d", &a);
	printf("정수 b : "); scanf("%d", &b);

	printf("a 값은 b의 %f%%입니다.\n", (double)a / b *100.0);

	return 0;
}

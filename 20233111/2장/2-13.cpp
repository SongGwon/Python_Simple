//============================================================================
// Name        : 0.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>


int main() {

	double a,b;
	printf("키 입력 : "); scanf("%lf", &a);
	printf("몸무게 입력 : "); scanf("%lf", &b);

	printf("BMI는 %.2f 입니다.\n", b/((a/100.0)*(a/100.0)));

	return 0;


}

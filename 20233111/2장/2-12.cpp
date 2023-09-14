//============================================================================
// Name        : 0.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>


int main() {

	 int a;
	 printf("키를 입력하세요 : ");
	 scanf("%d", &a);
	 printf("표준체중은 %0.1lf입니다.", (a-100) * 0.9);

	return 0;


}

/*
To test, go web Compiler https://www.onlinegdb.com/online_c_compiler
Referenced code: http://www.geeksforgeeks.org/dynamic-programming-set-1/
�Ʒ��� integer �ִ밪�� 45�� �ϰ�, ������� ��� ����ϴ� ������ ������ ���̴�.
*/
#include <stdio.h>
#define NIL -1
#define MAX 45

int fib[MAX];

int fibonacci(n){
	/*check and skip already calculated fib[n]*/
	if ( fib[n] == NIL ) {
		if ( n <= 1 ) fib[n] = n;
		else fib[n] = fibonacci(n-1) + fibonacci(n-2);
	}
	return fib[n];
}

int main(){
	/*initialize and input(default is 40)*/
	int i;
	int fib_num=40;
	for ( i=0; i<=MAX; i++ ) fib[i] = NIL;
	printf ("Enter a number of Fibonacci between 0~45 :");
	scanf ("%d", &fib_num);

	/*calculate fibonacci*/
	for (i=0;i<fib_num;i++) printf("\n%dth Fibonacci Number is \t %d",i,fibonacci(i));
	printf("\n%dth Fibonacci number is \t %d",
		fib_num, fibonacci(fib_num));

	return 0;
}
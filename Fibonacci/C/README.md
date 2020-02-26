# Fibonacci sequences for C language


## 1. Fibonacci Sequences

```
Fibonacci Sequences
Fn = 0 if n=0,
Fn = 1 if n=1,
Fn = (Fn-1) + (Fn-2) if n>2.

C language, recursive way

long fib(long n){
	if(n<2) return n;
	else return (fib(n-1) + fib(n-2));
```

## 2. Limitation

```
For using integer to count Fibonacci, maximum sequence number is 45
```

## 3. Flow

```
1. Input the sequence order between integer number 0 and 45.
2. Output sequence number's Fibonacci number.
```

## 4. TEST, Web complie and run

- Web compile and run : https://www.onlinegdb.com/online_c_compiler


# Fibonacci sequences for Python


## 1. Fibonacci Sequences

```
Fibonacci Sequences
Fn = 0 if n=0,
Fn = 1 if n=1,
Fn = (Fn-1) + (Fn-2) if n>2.

Python language, recursive way

def func_fibonacci(n) :
    # Check and skip already calculated list_fib[n]
    if list_fib[n] == -1:
        if n <= 1:
            list_fib[n] = n
        else:
            list_fib[n] = func_fibonacci(n-1) + func_fibonacci(n-2)
    return list_fib[n]
```

## 2. Limitation

```
For using integer to count Fibonacci, maximum sequence number is 45
```

## 3. Flow

```
1. Input the sequence order between integer number 0 and 45.
2. Output sequence order's Fibonacci number.
```

## 4. TEST, Web complie and run

- Web compile and run : https://www.onlinegdb.com/online_python_compiler


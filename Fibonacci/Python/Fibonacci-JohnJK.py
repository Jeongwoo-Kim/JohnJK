#!/usr/bin/env python
# -*- coding: utf-8 -*-
# To test, go web Compiler ( https://www.onlinegdb.com/online_python_compiler ) and copy below and run

# Initialize
max_num = 45
list_fib = [-1 for i in range(max_num)]

# Define Fibonacci function
def func_fibonacci(n) :
    # Check and skip already calculated list_fib[n]
    if list_fib[n] == -1:
        if n <= 1:
            list_fib[n] = n
        else:
            list_fib[n] = func_fibonacci(n-1) + func_fibonacci(n-2)
    return list_fib[n]

#Get order of Fibonacci sequence
fib_num = int(input("Enter a sequence order of Fibonacci between 0~45 : "))

#Call Fibonacci funtion to calculate fibonacci and print it
list_st = ["st ", "nd ", "rd ", "th "]
for i in range(fib_num):
    if i <= 2:
        print(i+1, list_st[i], "Fibonacci number is \t", func_fibonacci(i))
    else:
        print (i+1, list_st[3], "Fibonacci number is \t", func_fibonacci(i))

'''
Задача 1.
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
'''
a = int(input())
fib_prev = -1
fib_curr = 1
n = 0
while fib_curr < a:
    fib_next = fib_prev + fib_curr
    fib_prev = fib_curr
    fib_curr = fib_next
    n += 1
if fib_curr == a:
    print(n)
else:
    print(-1)

"""
Project Euler #2 - Even Fibonacci Numbers
Methodology: Sum even numbers of iterative fibonacci
implementation which uses a generator.
"""
def fib(limit):
    a, b = 0, 1
    while a < limit:
        if not a % 2:         
            yield a
        a, b = b, a + b

print(sum(fib(4000000)))
# Dynamic Programming
# Fibonacci sequence using memoization
def fib(n, memo=None):
    if memo is None:
        memo = [None] * (n + 1)
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        memo[n] = 1
        return 1
    else:
        results = fib(n-1, memo) + fib(n-2, memo)
        memo[n] = results
        return results

print(fib(7))

# Bottom-Up approach

def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    fib_table = [0] * (n + 1)
    fib_table[1] = 1
    fib_table[2] = 1
    for i in range(3, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    return fib_table[n]

print(fib_bottom_up(7))

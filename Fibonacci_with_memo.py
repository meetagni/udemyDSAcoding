import time
memo = [None] * 100
counter = 0
def fib(n):
    global counter
    counter += 1
    if memo[n] is not None:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

start = time.perf_counter()
n = 40
print('With memoization, Fib of ', n, ' is: ', fib(n))
end = time.perf_counter()
print('Time taken: ', end - start)
print('Function calls: ', counter)
import time
counter = 0
def fib(n):
    global counter
    counter += 1
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

start = time.perf_counter()
n = 40
print('Without memoization, Fib of ', n, ' is: ', fib(n))
end = time.perf_counter()
print('Time taken: ', end - start)
print('Function calls: ', counter)
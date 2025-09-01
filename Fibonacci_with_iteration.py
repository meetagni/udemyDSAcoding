import time
counter = 0
def fib(n):
    fib_list = [0,1]
    global counter
    for index in range(2, n+1):
        counter += 1
        next_fib = fib_list[index-1] + fib_list[index-2]
        fib_list.append(next_fib)
    return fib_list[n]

start = time.perf_counter()
n = 40
print('With memoization, Fib of ', n, ' is: ', fib(n))
end = time.perf_counter()
print('Time taken: ', end - start)
print('Function calls: ', counter)
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a  
        a, b = b, a + b
        
fib_iter = iter(fibonacci_generator())
fib_sequence = [next(fib_iter) for _ in range(10)]
print(fib_sequence)


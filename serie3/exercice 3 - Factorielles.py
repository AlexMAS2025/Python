def fact(n=10):
    print(f"factorielle de {n}: ")
    result = 1
    for i in range(2, n+1):
        result *= i
        yield result

values = list(fact())
print(values[-1])

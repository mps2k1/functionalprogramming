def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Utwórz generator
fib_gen = fibonacci()

# Wydrukuj pierwsze 10 liczb Fibonacciego
for _ in range(10):
    print(next(fib_gen))
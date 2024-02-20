def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.rstrip()

# Przykład użycia generatora ciągu liczb Fibonacciego
fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))

# Przykład użycia generatora czytającego duży plik tekstowy linia po linii
file_path = 'duzy_plik.txt'  # Ścieżka do dużego pliku tekstowego
lines_gen = read_large_file(file_path)
for line in lines_gen:
    print(line)


    def read_large_file(file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    yield line.rstrip()
        except FileNotFoundError:
            print("Plik nie został znaleziony.")
        except Exception as e:
            print("Wystąpił błąd podczas czytania pliku:", str(e))


    # Przykład użycia
    file_path = 'file.txt'  # Ścieżka do dużego pliku tekstowego
    lines_gen = read_large_file(file_path)
    for line in lines_gen:
        print(line)
from functools import reduce

# Funkcja znajdująca największą liczbę w liście
def find_max(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)

# Funkcja obliczająca średnią z listy liczb
def calculate_average(numbers):
    total = reduce(lambda x, y: x + y, numbers)
    return total / len(numbers) if len(numbers) > 0 else float('nan')

# Lista liczb
numbers = [3, 8, 1, 6, 2, 9, 4, 7, 5]

# Znajdowanie największej liczby w liście
max_number = find_max(numbers)
print("Największa liczba:", max_number)

# Obliczanie średniej z listy liczb
average = calculate_average(numbers)
print("Średnia z listy liczb:", average)
from itertools import combinations

def generate_combinations(elements):
    return list(combinations(elements, 2))

# Przykładowe użycie funkcji
elements = [1, 2, 3, 4]
result = generate_combinations(elements)
print(result)
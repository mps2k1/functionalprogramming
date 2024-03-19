from itertools import product

# Dwie listy
list1 = ['A', 'B']
list2 = ['C', 'D']

# Wygenerowanie i wydrukowanie wszystkich możliwych kombinacji
for combination in product(list1, list2):
    print(combination)


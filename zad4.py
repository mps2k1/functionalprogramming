numbers = [3, 6, 9, 12, 15]

# List comprehension z wyrażeniem walrus operator
squares_greater_than_10 = [square for num in numbers if (square := num ** 2) > 10]

print(squares_greater_than_10)
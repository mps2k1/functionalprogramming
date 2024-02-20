
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate(operation, x, y):
    return operation(x, y)

# Przekazanie funkcji jako argumentu
result_addition = calculate(add, 5, 3)
print("Addition:", result_addition)

result_subtraction = calculate(subtract, 10, 7)
print("Subtraction:", result_subtraction)
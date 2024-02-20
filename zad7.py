##7
# Funkcja podnosząca liczbę do kwadratu
def square(x):
    return x ** 2

# Funkcja dodająca 10 do liczby
def add_ten(x):
    return x + 10

# Funkcja aplikująca listę funkcji do wartości
def apply_functions_to_value(value, functions):
    result = value
    for func in functions:
        result = func(result)
    return result

# Lista funkcji
functions_list = [square, add_ten]

# Wartość początkowa
initial_value = 5

# Wywołanie funkcji apply_functions_to_value() dla listy funkcji i wartości początkowej
final_result = apply_functions_to_value(initial_value, functions_list)

# Wyświetlenie wyniku
print("Final result:", final_result)

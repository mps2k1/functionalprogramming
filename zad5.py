get_even_numbers = lambda numbers: [num for num in numbers if num % 2 == 0]

# Przykładowe użycie funkcji
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print("Even numbers:", even_numbers)
# Funkcja obliczająca pole prostokąta przy użyciu wyrażenia lambda
calculate_rectangle_area = lambda length, width: length * width

# Przykładowe użycie funkcji
length = 5
width = 3
area = calculate_rectangle_area(length, width)
print("Rectangle area:", area)
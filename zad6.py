words = ["apple", "banana", "avocado", "kiwi", "orange", "apricot"]

# Wykorzystanie funkcji filter() do wyodrębnienia słów zaczynających się na literę "a"
words_starting_with_a = list(filter(lambda word: word.startswith("a"), words))

# Wykorzystanie funkcji map() do przekształcenia listy liczb w listę ich kwadratów
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))

# Wyświetlenie wyników
print("Words starting with 'a':", words_starting_with_a)
print("Squared numbers:", squared_numbers)
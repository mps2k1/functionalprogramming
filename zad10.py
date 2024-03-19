def concat_strings(*args):
    """
    Łączy przekazane argumenty typu string w jeden ciąg znaków, rozdzielając spacją.

    Args:
        *args: Nieokreślona liczba argumentów typu string.

    Returns:
        str: Połączony ciąg znaków.
    """
    return ' '.join(args)


# Testowanie funkcji na kilku zestawach stringów
print(concat_strings("Hello", "world"))  # Wydrukuje: Hello world
print(concat_strings("The", "quick", "brown", "fox"))  # Wydrukuje: The quick brown fox
print(concat_strings("Python", "is", "awesome"))  # Wydrukuje: Python is awesome
print(concat_strings("This", "is", "a", "test"))

global_variable = 10  # Zmienna globalna

def function_with_global_variable():
    # Używanie zmiennej globalnej
    print("Global variable inside the function:", global_variable)

def function_with_local_variable():
    local_variable = 20  # Zmienna lokalna
    # Używanie zmiennej lokalnej
    print("Local variable inside the function:", local_variable)

def function_with_functional_variable():
    functional_variable = global_variable * 2  # Używanie zmiennej globalnej
    # Używanie zmiennej funkcyjnej
    print("Functional variable inside the function:", functional_variable)

# Wywołanie funkcji
function_with_global_variable()
function_with_local_variable()
function_with_functional_variable()

# Sprawdzenie zmiennej globalnej po wywołaniu funkcji
print("Global variable outside the functions:", global_variable)
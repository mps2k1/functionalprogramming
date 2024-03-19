
def square(x):
    return x ** 2

def add_ten(x):
    return x + 10

def apply_functions_to_value(value, functions):
    result = value
    for func in functions:
        result = func(result)
    return result

functions_list = [square, add_ten]

initial_value = 5

final_result = apply_functions_to_value(initial_value, functions_list)

print("Final result:", final_result)

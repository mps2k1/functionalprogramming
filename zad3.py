def recursive_sum(nested_list):
    total = 0
    for item in nested_list:
        if isinstance(item, list):
            total += recursive_sum(item)
        else:
            total += item
    return total
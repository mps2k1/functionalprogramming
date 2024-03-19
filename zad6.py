def map_nested(func, nested_list):
    return [map_nested(func, x) if isinstance(x, list) else func(x) for x in nested_list]

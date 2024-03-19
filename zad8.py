def partition_list(lst, condition):
    return [x for x in lst if condition(x)], [x for x in lst if not condition(x)]

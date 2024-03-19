def rotate_list(lst, steps):
    steps %= len(lst)
    return lst[-steps:] + lst[:-steps]

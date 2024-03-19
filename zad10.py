def cumulative_sum(lst):
    total = 0
    result = []
    for num in lst:
        total += num
        result.append(total)
    return result
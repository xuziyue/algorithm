def insertion_sort(l: list) -> NoneType:
    """Sort given list l in non-decreasing order using insertion sort.
    """
    for j in range(1, len(l)):
        key = l[j]
        i = j - 1
        while i >= 0 and key > l[i]:
            l[i + 1] = l[i]
            i -= 1
        l[i + 1] = key
        
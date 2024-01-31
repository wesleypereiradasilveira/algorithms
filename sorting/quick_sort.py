

def quick_sort(values: list, start: int = 0, end: int = None) -> list:
    if end is None:
        end = len(values) - 1

    if start < end:
        pivot = partition(values, start, end)
        quick_sort(values, start, pivot - 1)
        quick_sort(values, pivot + 1, end)

    return values

def partition(values: list, start: int = 0, end: int = None):
    pivot = values[end]
    index = start

    for j in range(start, end):
        if values[j] <= pivot:
            values[j], values[index] = values[index], values[j]
            index = index + 1

    values[index], values[end] = values[end], values[index]

    return index


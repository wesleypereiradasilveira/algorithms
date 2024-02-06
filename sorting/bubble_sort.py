

def bubble_sort(values: list) -> list:
    for i in range(len(values) -1, 0, -1):
        for j in range(i):
            if values[j] > values[j+1]:
                temp = values[j]
                values[j] = values[j+1]
                values[j+1] = temp

    return values

def bubble_sort_v2(values: list) -> list:
    n = len(values)
    for i in range(n - 1, 0, -1):
        swapped = False
        for j in range(i):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True

        if not swapped:
            break

    return values

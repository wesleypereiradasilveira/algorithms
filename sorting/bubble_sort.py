

def bubble_sort(values: list) -> list:
    for i in range(len(values) -1, 0, -1):
        for j in range(i):
            if values[j] > values[j+1]:
                temp = values[j]
                values[j] = values[j+1]
                values[j+1] = temp

    return values

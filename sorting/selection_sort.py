

def selection_sort(values: list) -> list:
    for i in range(len(values) - 1):
        min_position = i
        for j in range(i, len(values)):
            if values[j] < values[min_position]:
                min_position = j

        temp = values[i]
        values[i] = values[min_position]
        values[min_position] = temp

    return values

def selection_sort_v2(values: list) -> list:
    size = len(values)
    for j in range(size - 1):
        min_index = j
        for i in range(j, size):
            if values[i] < values[min_index]:
                min_index = i
        
        values[j], values[min_index] = values[min_index], values[j]

    return values

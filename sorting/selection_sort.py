

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

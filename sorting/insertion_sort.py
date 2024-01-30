


def insertion_sort(values: list) -> list:
    for i in range(1, len(values)):
        while values[i - 1] > values[i] and i > 0:
            temp = values[i]
            values[i] = values[i - 1]
            values[i - 1] = temp

            i = i - 1

    return values

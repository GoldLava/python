bike = {"make": "Honda",
        "model": "250 dream",
        "color": "red",
        "engine_size": 250
        }


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([1, 5, 2, 1, 7, 3, 1, 9, 6, 1, 5, 4, 8, 5]))

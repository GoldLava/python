pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
# sorted leaves the original unchanged, the sort method changes the original

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]
names.sort(key=str.casefold)
print(names)

letters.sort()
print(letters)


# def insertion_sort(numbers):
#     indexing_length = range(1, len(numbers))
#     for x in indexing_length:
#         value_to_sort = numbers[x]
#
#         while numbers[x-1] > value_to_sort and x > 0:
#             numbers[x], numbers[x-1] = numbers[x-1], numbers[x]
#             i = i - 1
#     return numbers
#
# print(insertion_sort(numbers), "sorted by insertion_sort")

# def insertion_sort(A):
#     indexing_length = range(1, len(A))
#     for x in indexing_length:
#         value_to_sort = A[x]
#
#         while A[x-1] > value_to_sort and x > 0:
#             A[x], A[x-1] = A[x-1], A[x]
#             x = x - 1
#
#     return A
#
# print(insertion_sort(numbers), "by Kevin Titco")

# def selection_sort(A):
#     indexing_length = range(0, len(A)-1)
#
#     for x in indexing_length:
#         min_value = x
#
#         for y in range(x+1, len(A)):
#             if A[y] < A[min_value]:
#                 min_value = y
#             if min_value != x:
#                 A[x], A[min_value] = A[min_value], A[x]
#
#     return A
#
# print(selection_sort(numbers), "sorted by KT")

# def bubble_sort(A):
#     indexing_length = len(A) - 1
#     sorted = False
#
#     while not sorted:
#         sorted = True
#         for x in range(0, indexing_length):
#             if A[x] > A[x+1]:
#                 # the swap
#                 sorted = False
#                 A[x], A[x+1] = A[x+1], A[x]
#
#     return A
#
# print(bubble_sort(numbers), "sorted by bubble sort")
#


# def quick_sort(sequence):
#     length = len(sequence)
#     if length <= 1:
#         return sequence
#     else:
#         pivot = sequence.pop()
#
#     items_right = []
#     items_left = []
#
#     for item in sequence:
#         if item > pivot:
#             items_right.append(item)
#         else:
#             items_left.append(item)
#
#     return quick_sort(items_left) + [pivot] + quick_sort(items_right)
#
# print(quick_sort(numbers), "by quick sort")

# def bubble_sort(A):
#     indexing_length = len(A) - 1
#     sorted = False
#
#     while not sorted:
#         sorted = True
#         for x in range(0, indexing_length):
#             if A[x] > A[x+1]:
#                 sorted = False
#                 A[x], A[x+1] = A[x+1], A[x]
#
#     return A
#
# print(bubble_sort(numbers), "by bubble sort")

# def insertion_sort(A):
#     indexing_length = range(1, len(A))
#     for x in indexing_length:
#         value_to_sort = A[x]
#         if A[x-1] > A[x] and x > 0:
#             A[x-1], A[x] = A[x], A[x-1]
#             x = x - 1
#     return A
#
#
# print(insertion_sort(numbers), "by insertion sort")


# def selection_sort(A):
#     indexing_length = range(0, len(A)-1)
#     for x in indexing_length:
#         min_value = x
#
#         for y in range(x + 1, len(A)):
#             if A[y] < A[min_value]:
#                 min_value = y
#
#         if min_value != x:
#             # A[x], A[min_value] = A[min_value], A[x]
#             A[min_value], A[x] = A[x], A[min_value]
#     return A
#
# print(selection_sort(numbers))


# def bubble_sort(A):
#     indexing_length = range(0, len(A) - 1)
#     sorted = False
#
#     while not sorted:
#         sorted = True
#         for x in indexing_length:
#             if A[x+1] < A[x]:
#                 sorted = False
#                 A[x+1], A[x] = A[x], A[x+1]
#     return A
#
# print(bubble_sort(numbers), "bubble")
#
# def insertion_sort(A):
#     indexing_length = range(1, len(A))
#
#     for x in indexing_length:
#         value_to_sort = A[x]
#
#         if A[x-1] > A[x] and x > 0:
#             A[x-1], A[x] = A[x], A[x-1]
#     return A
#
# print(insertion_sort(numbers), "insertion sort")

# def bubble_sort(A):
#     indexing_length = range(0, len(A) -1)
#     sorted = False
#
#     while not sorted:
#         sorted = True
#         for x in indexing_length:
#             if A[x+1] < A[x]:
#                 sorted = False
#                 A[x+1], A[x] = A[x], A[x+1]
#     return A
#
# print(bubble_sort(numbers))

# def insertion_sort(A):
#     indexing_length = range(1, len(A))
#     for x in indexing_length:
#         my_right = A[x]
#         my_left = A[x-1]
#         while my_left > my_right and x > 0:
#             my_left, my_right = my_right, my_left
#             x = x - 1
#
#     return A
#
# print(insertion_sort(numbers), "inesrtion sort success")

# def bubble_sort(A):
#     indexing_length = range(0, len(A)-1)
#     sorted = False
#
#     while not sorted:
#         sorted = True
#         for x in indexing_length:
#             if A[x+1] < A[x]:
#                 A[x+1], A[x] = A[x], A[x+1]
#     return A
#
# print(bubble_sort(numbers))

# def selection_sort(A):
#     indexing_length = range(0, len(A)-1)
#     for x in indexing_length:
#         min_value = x
#         for y in range(x+1, len(A)):
#             if A[y] < min_value:
#                 min_value = y
#         if min_value != x:
#             A[min_value], A[x] = A[x], A[min_value]
#     return A
#
# print(selection_sort(numbers), "selection success")
#
#
# def quick_sort(sequence):
#     length = len(sequence)
#     if length <= 1:
#         return sequence
#     else:
#         pivot = sequence.pop()
#
#     my_left = []        # lesser
#     my_right = []       # greater
#
#     for item in sequence:
#         if item > pivot:
#             my_right.append(item)
#         else:
#             my_left.append(item)
#     return quick_sort(my_left) + [pivot] + quick_sort(my_right)
#
#
# print(quick_sort(numbers), "quick sort success")
#
#

def Fibonacci(n):
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    for x in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    return result


for x in range(70):
    print(x, Fibonacci(x))


def insertion_sort(A):
    indexing_length = range(1, len(A))
    for x in indexing_length:
        my_right = A[x]
        my_left = A[x - 1]

        while my_left > my_right and x > 0:
            A[my_left], A[my_right] = A[my_right], A[my_left]
            x = x - 1
    return A


print(insertion_sort(numbers), "by insertion sort")

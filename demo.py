# from typing import List, Any
#
#
# def quick_sort(sequence) -> object:
#     length = len(sequence)
#     if length <= 1:
#         return sequence
#
#     else:
#         pivot = sequence.pop()
#
#         items_greater = []
#         items_lower = []
#
#     for number in sequence:
#         if number > pivot:
#             items_greater.append(number)
#
#         else:
#             items_lower.append(number)
#
#     return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
#     if length == 0:
#         print()
#
#
# print(quick_sort([4, 5, 2, 1, 3]))

A = [-2, 1, 2, 4, 7, 11]
target = 13


def two_sum_brute_force(A, target):
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False


# Time complexity: 0(n)
# Space complexity: 0(n)
def two_sum_hash_table(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]
    return False


def two_sum(A, target):
    i = 0
    j = len(A) - 1

    while i <= j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:  # A[i] + A[j] > target
            j -= 1
    return False


print(two_sum_brute_force(A, target))
print(two_sum_hash_table(A, target))
print(two_sum(A, target))


def find_two_sum(A, target):
    ht = dict()
    i = 0
    j = len(A) - 1

    while i <= j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return False

print(find_two_sum(A, target))

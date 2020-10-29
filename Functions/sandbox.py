# From an unsorted array, find pair of targeted sum
A = [3, 8, 3, 7, 1, 9, 2, 5, 7, 1, 10, 5]
target_sum = 10

B = sorted(A)
print(B)

#
# def find_target_sum(A, target_sum):
#
#     i = 0
#     j = len(A) - 1
#
#     while i <= j:
#         if A[i] + A[j] == target_sum:
#             print(A[i], A[j])
#             return True
#         elif A[i] + A[j] < target_sum:
#             i += 1
#         else:
#             j -= 1
#     return False
#
#
# print(find_target_sum(B, target_sum))
#
# def quick_sort(sequence):
#     length = len(sequence)
#     if length <= 1:
#         return sequence
#     else:
#         pivot = sequence.pop()
#         items_greater = []
#         items_lesser = []
#         for items in sequence:
#             if items > pivot:
#                 items_greater.append(items)
#             else:
#                 items_lesser.append(items)
#         return quick_sort(items_lesser) + [pivot] + quick_sort(items_greater)
#     if sequence == 0:
#         print()
#
# print(quick_sort(A))
#
# #Fibonacci
#
# def Fibonacci(n):
#     if 0 <= n <= 1:
#         return n
#
#
#     f_minus1, f_minus2 = 0, 1
#     for f in range(n - 1):
#         result = f_minus2 + f_minus1
#         f_minus2 = f_minus1
#         f_minus1 = result
#
#     return result
#
# for i in range(70):
#     print(i, Fibonacci(i))


# def binary_search(sequence, target_num):
#
#     start_index = 0
#     end_index = len(sequence) - 1
#
#     while start_index <= end_index:
#         midpoint = start_index + (end_index - start_index) // 2
#         midpoint_value = sequence[midpoint]
#
#         if midpoint_value == target_num:
#             return midpoint
#
#         elif target_num < midpoint_value:
#             end_index = midpoint - 1
#
#         else:
#             start_index = midpoint + 1
#
#     return None
#
#
# sequence_a = [2,4,5,6,7,8,9,10,12,13,14]
# item_a = 12
# print(binary_search(sequence_a, item_a))
# print(binary_search(B, target_sum))
# def factorial(n):
#     # address that 0! and 1! is still equal 1
#     if n <= 1:
#         return 1
#
#     result = 2
#     for x in range(3, n + 1):
#         result *= x
#
#     return result
#
# for i in range(36):
#     print(i, factorial(i))

# def find_target_sum(A, target_sum):
#
#     the_left = 0
#     the_right = len(A) - 1
#
#     while the_left < the_right:
#         if A[the_left] + A[the_right] == target_sum:
#             print("Our pair includes:", A[the_left], A[the_right])
#             the_left += 1
#             the_right -=1
#
#         elif A[the_left] + A[the_right] < target_sum:
#             the_left += 1
#         else:
#             the_right -=1
#
#     print("Search complete")
#     return False
#
# print(find_target_sum(B, target_sum))

# def find_target_sum(arr, target_sum):
#     # addressing index values
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         # comparing values
#         if arr[left] + arr[right] == target_sum:
#             print("Our pair includes: ", arr[left], arr[right])
#             left += 1
#             right -= 1
#         elif arr[left] + arr[right] < target_sum:
#             left += 1
#         else:
#             right -= 1
#
#     return False
#
# print(find_target_sum(B, target_sum))
# def insertion_sort(arr):
#     indexing_length = range(1, len(arr))
#
#     for x in indexing_length:
#         value_to_sort = arr[x]
#
#         while arr[x - 1] > arr[x] and x > 0:
#             arr[x], arr[x - 1] = arr[x - 1], arr[x]
#             x = x - 1
#     return arr


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
# def insertion_sort(A):
#     indexing_length = range(1, len(A))
#     for x in indexing_length:
#         my_right = A[x]
#         my_left = A[x-1]
#         if my_left > my_right and x > 0:
#             my_left, my_right = my_right, my_left
#             x = x - 1
#     return A


# print(insertion_sort(A), "sorted by insertion")


# finding one pair
# def sum_pair(A):
#     left = 0
#     right = len(A)- 1
#
#     while left < right:
#         if A[left] + A[right] == target_sum:
#             print("our pair includes: {0} and {1}, their positions are {2} and {3}".format(A[left], A[right], left, right))
#             return True
#         if A[left] + A[right] < target_sum:
#             left += 1
#         else:
#             right -= 1
#     return False
# print(sum_pair(B))

# find all pairs

def sum_pair2(A):
    left = 0
    right = len(A) - 1

    while left < right:
        if A[left] + A[right] < target_sum:
            left += 1
        elif A[left] + A[right] > target_sum:
            right -= 1
        elif A[left] + A[right] == target_sum:
            print("our pair includes: {0} and {1}, their positions are {2} and {3}".format(A[left], A[right], left, right))
            left += 1
            
    return(A)

print(sum_pair2(B))
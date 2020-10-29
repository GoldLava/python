# # define variables needed to start
# answer = "open"
# attempt_counter = 0
# keep_going = True
#
#
#
# while(keep_going):
# # allow user to take a guess - input
#     guess = input("Try to guess password: ")
# # attempt counter increase by 1
#     attempt_counter += 1
# # compare guess with answer
# # if guess == answer, return favorable outcome and stop loop
#     if guess == answer:
#         print("Nice! You've guessed it right.")
#         keep_going = False
# # if guess != answer and attempt counter <=3, return try again outcome + loop
#     if guess != answer and attempt_counter <=3:
#         print("Try again")
#         keep_going = True
# # if guess != answer attempt counter >3 return not nice outcome and stop loop
#     if guess != answer and attempt_counter > 3:
#         print("Max attempt has been reached")
#         keep_going = False
#
A = [1, 6, 9, 10, 5, 3, 2]


#
# def quick_sort(A):
#     # define variables, address array manipulation as var
#     length = len(A)
#
#
#     # address recursion of pivot on individual items
#     if length <= 1:
#         return A
#     else:
#         # address pivot, select a number in array to evaluate higher and lower value groups
#         pivot = A.pop()
#     # address lower value and higher value var
#     value_lower = []
#     value_higher = []
#
#     # if pivot <= value_to_sort, then add value_to_sort to upper value
#     for value_to_sort in A:
#         if pivot < value_to_sort:
#             value_higher.append(value_to_sort)
#         # if pivot >= value_to_sort, then add it to lower value
#         else:
#             value_lower.append(value_to_sort)
#         # combine sorted lower values, pivot, and sorted upper values
#     return quick_sort(value_lower) + [pivot] + quick_sort(value_higher)
#
#
#
#
# print(quick_sort(A))

# def selection_sort(A):
#     # address array manipulation var
#     indexing_length = range(0, len(A)-1)
#
#     # list all other items in array and compare their values with our current min_val
#     for x in indexing_length:
#         # grab 1st item and set it as min_value
#         min_value = x
#         for val_to_sort in range(x + 1, len(A)):
#             # if value on right < min_value then set item on right as new min_value
#             if A[val_to_sort] < A[min_value]:
#                 min_value = val_to_sort
#     # if new min value swap right with left
#         if min_value != x:
#             A[x], A[min_value] = A[min_value], A[x]
#     # return back into loop and set next position as min_val
#     return A
#
#
# # outcome: sorted array by selection sort
# print(selection_sort(A))

# take index 0 and and consider it as sorted
# all items after index 0 is unsorted, address it in form of var
# compare sorted index 0 against unsorted index 1
# if value of sorted index 0 > unsorted value of index 1, swap their positions, change their index number
# index 0 and index 1 are now sorted, moving linearly, compare index 1 with index 2
# if index 2 value < index 1 value, swap places and decrement index position continue until left value is < right value

# input: an unsorted array
# def selection_sort(A):
#     # traverse entire array to evaluate current min_val
#     indexing_length = range(0, len(A) - 1)
#     for x in indexing_length:
#         # min_val is always position left
#         min_val = x
#         # compare left position with right position
#         for right in range(x + 1, len(A)):
#             # if left position value is bigger than right position value set right position value as min_val
#             if A[min_val] > A[right]:
#                 min_val = right
#             # swap position of left with position of right
#             if min_val != x:
#                 A[min_val], A[x] = A[x], A[min_val]
#             # loop back to evaluate next left position value as min_val until all sorted
#             # outcome: sorted array by selection_sort
#     return A
#
# print(selection_sort(A))

# input is an arrray
# def insertion_sort(A):
#     # index 0 is always sorted
#     # traverse array linearly to compare last item in sorted w/ next unsorted
#     indexing_length = range(1, len(A))
#     for x in indexing_length:
#         # if last item in sorted on left is greater than unsorted item on right
#         while A[x-1] > A[x]:
#             # swap positions of two items, unsorted to keep swapping until value to its right is greater
#             A[x-1], A[x] = A[x], A[x-1]
#             x -= 1
#             # traverse array linearly, loop back
#             # outcome: sorted array
#     return A
#
# print(insertion_sort(A))

# def bubble_sort(A):
#     indexing_length = range(0, len(A)-1)
#     sorted = False
#     while not sorted:
#         sorted = True
#         for x in indexing_length:
#             if A[x+1] < A[x]:
#                 sorted = False
#                 A[x], A[x+1], =  A[x+1], A[x]
#     return A
#
# print(bubble_sort(A))

# input is an array
# def selection_sort(A):
#     # traverse the array
#     indexing_length = range(0, len(A) - 1)
#     for x in indexing_length:
#         # index 0 starts as min_val
#         min_val = x
#         # compare min_val vs items on the right
#         for right in range(x+1, len(A)):
#             # if value of item on right is less than min_val
#             if A[right] < A[min_val]:
#                 # then set item on right as new min_val
#                 min_val = right
#             if min_val != x:
#                 # swap positions
#                 A[x], A[min_val] = A[min_val], A[x]
#             # return to traversing array comparing next min_val vs items on right
#
#             # outcome: sorted array
#     return A
#
# print(selection_sort(A))
A.sort()

def quick_sort(A):
    length = len(A)
    if length <= 1:
        return A
    else:
        pivot = A.pop()

    items_lesser = []
    items_greater = []

    for item in A:
        if item < pivot:
            items_lesser.append(item)
        elif item > pivot:
            items_greater.append(item)
    return quick_sort(items_lesser) + [pivot] + quick_sort(items_greater)

print(quick_sort(A))

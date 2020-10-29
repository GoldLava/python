empty_list = []
x = [2, 4, 6, 8]
y = [1, 3, 5, 7, 9]

numbers = [x, y]
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)



# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(numbers)
#
# #sorted vs list
# digits = list("432985617")
# print(digits)
#
# # more_numbers = list(numbers)
# # more_numbers = numbers[:]
# more_numbers = numbers.copy()
# print(numbers)
# print(numbers is more_numbers)
# print(numbers == more_numbers)


# print(min(x))
# print(max(x))
# print(min(y))
# print(max(y))
#
# print()
# print(len(x))
# print(len(y))
#
# print()
# print("mississippi".count("s"))

# x.extend(y)
# print(x)
# another_x = x
# print(another_x)
#
# # sort only rearranges items in the list, does not make copies of list
# x.sort(reverse=True)
# print(x)
# print(another_x)

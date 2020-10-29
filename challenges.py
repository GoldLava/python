# for i in range(1, 13):
#     for j in range(1, 13):
#         print("{0:4} times {1:4} is {2:4}".format(j, i, i * j))
#         # print("------------------")
# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
# for i in range(0, 100, 7):
#     print(i)
#     if i // 11 == 7:
#         break
#
# test_int = 77
# print(test_int % 12)
# for x in range(0, 20):
#     print(x)

# for i in range(0, 21):
#     if i > 0 and i % 3 != 0 and i % 5 != 0:
#         print(i)

# number = 5
# multiplier = 8
# answer = 0
#
# # add your loop after this comment
# for i in range(multiplier):
#     answer += number
#
# print(answer)

# number = 17
# multiplier = 80
# answer = 0
#
# for i in range(multiplier):
#     answer += number
#
# print(answer)



# if my_choice in my_list:
#     activity = my_list.index(my_choice)
# if activity is not None:
#     print("Item found at position {}".format(activity))
# else:
#     print("{} not found".format(my_choice))
for x in range(30):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)








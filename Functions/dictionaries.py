my_book = {"orange": "a sweet orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small sweet growing fruit",
         "lime": "a sour, green citrus fruit"}
print(my_book)
print(my_book.items())

f_tuple = tuple(my_book.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))


# for val in fruit.values():
#     print(val)

# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)

# for snack in f_tuple:
#     item, description = snack
#     print(item + " is " + description)
#
# print(dict(f_tuple))

#
# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])
#


# for x in range(32):
#     for item in fruit:
#         print(item + " is a " + fruit[item])
#     print("-" * 40)

# ordered_key = list(fruit.keys())
# ordered_key.sort()
# ordered_key = sorted(list(fruit.keys()))
#
# for f in ordered_key:
#     print(f + " - " + fruit[f])


# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# fruit["pear"] = "great with tequila"
# print(fruit)
# fruit["lime"] = "super great with tequila"
# print(fruit)
# del fruit["orange"]
#
# while True:
    # dict_key = input("Please enter a fruit: ")
    # if dict_key == "quit":
    #     break
    # description = fruit.get(dict_key.casefold(), "We don't have a " + dict_key.casefold())
    # print(description)
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print("we don't have description for a {}.".format(dict_key))

#hashes are not ordered, changes each time we run it
# for description in fruit:
#     print(fruit[description])
#


# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

# better to use keys, val is less efficient
# for val in fruit.values():
#     print(val)
# this below is more efficient
# for key in fruit:
#     print(fruit[key])
# fruit_keys = fruit.keys()
# print(fruit.keys())
#
# print(fruit.values())
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)
# print(fruit)
#
# for snack in fruit:
#     print(fruit[snack])
#
# # a tuple
# print("fruit items:", fruit.items())
# f_tuple = tuple(fruit.items())
# print(f_tuple)
#
# for snack in f_tuple:
#     item, description = snack
#     print(item + " is " + description)
#

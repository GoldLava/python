shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
print(shopping_list)
item_to_find = "spam"
# None is equivalent to null, represents no value:
found_at = None

# for in dex in range(6):
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))

print(shopping_list[-1])

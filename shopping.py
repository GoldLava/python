shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        #cause everything else in the loop to be ignored and to return back to the forloop start process
        continue
    print("Buy " + item)
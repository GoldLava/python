view_my_list = """Please choose one from below:
1.  Wash the dishes
2.  Pick up some groceries,
3.  Do laundry
4.  Clean and organize home
5.  Learn other investing options
6.  Provision current assets
7.  Project management
8.  Learn profound Python skills
9.  Work on websites
0.  Exit"""

print(view_my_list)
print("*" * 80)
print()
user_choice = input("Select an activity by number: ")
user_int = int(user_choice)

my_list = ["Wash the dishes", "Pick up some groceries",
           "Do laundry", "Clean and organize home",
           "Learn other investing options",
           "Provision current assets", "Project management",
           "Learn profound Python skills", "Work on websites",
           "Exit"]


while user_int != 0:
    if user_choice not in view_my_list:
        print(view_my_list)
    if user_choice in view_my_list:
        # print("You have chosen to: {}".format(user_choice))
        x = int(user_choice)
        y = x - 1
        print("You have chosen to: {}.".format(my_list[y]))
        user_choice = input("Select an activity by number: ")
        user_int = int(user_choice)
    else:
        print("Your request to leave the program has been granted.")


#                   1
#         012345678901234
# parrot = "Norwegian Blue"
#
# print(parrot[0:6]) # Norweg, up to but not including
# print(parrot[3:5])
# print(parrot[0:9])
# print(parrot[:9])
#
# print(parrot[10:14])
# print(parrot[10:])
#
# print(parrot[:6])
# print(parrot[6:])
# print(parrot[:6] + parrot[6:])
#
# print(parrot[:])
#
# letters = "abcdefghijklmnopqrstuvwxyz"
#
# print(letters[6:16])
#
# print(parrot[-4:2])
# print(parrot[-14:-8])
# print(parrot[-14])
#
# print(parrot[0:6:2]) #Nre, start, stop, pattern interval
# print(parrot[0:6:3]) #Nw
#data extraction of items that are not numbers provided they are every 4th letter
number = input("Please enter a series of numbers using any separators your like: ")

separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

#print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))


print("*"*80)

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
# caps = ""
# alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for char in quote:
#     if char in alphabet:
#         print(char + caps)
for char in quote:
    if char.isupper():
        print(char)

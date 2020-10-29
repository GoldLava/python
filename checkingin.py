# parrot = "Norwegian Blue"
#
# letter = input("Enter a character: ")
#
# if letter in parrot:
#     print("{} is in {}".format(letter, parrot))
# else:
#     print("I don't need that letter")
activity = input("What would you like to do today? ")
if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")

askName = input("Hello. What's your name?: ")
askAge = int(input("Okay. And age?: "))

print(askName)
if askName:
    print(askAge)
    if 18 <= askAge <= 30:
        print("Welcome to the 18-30 year old's holidays, {}".format(askName))
    else:
        print("Your Holiday permission is denied, {}. You have missed the age range because you are {} years old".format(askName,askAge))



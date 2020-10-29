for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 80)

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("Oh, you are old enough.")
else:
    print("Let's wait {0} years until you are old enough".format(18-age))

moms_age = int(input("How old is your mother?: "))

print("I see. Your mother birthed you when she was {0} years old. You two are {1} years apart!".format(moms_age - age,moms_age - age))

race = input("What is your ethnicity?: ")
print("Your ethnicity is {0}!".format(race))

if race == "white":
    print("Then, you are not Asian.")
else:
    print("You are a minority.")

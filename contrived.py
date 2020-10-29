# for loops always involve a range of numbers ie. for x in
# range(multiplier), the x iterated in the next line usually

numbers = [1, 45, 31, 12, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are fine")
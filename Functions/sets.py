# two ways to create sets, cannot use an empty set for sets, only for dictionaries
# no keys supplied
# dictionaries do not have an add method
# set can have union and subtraction

# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("=" * 40)
#
# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wild_animals)
#
# for animals in wild_animals:
#     print(animals)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

empty_set = set()
empty_set_2 = {}
empty_set.add("a")
# empty_set_2.add("a")

# when creating sets from ranges and tuples, must use set constructor vs. curly braces
# tuples can be used to create a set

# even = set(range(1, 40, 2))
# print(even)
# square_tuple = (4, 6, 9, 16, 25)
# squares = set(square_tuple)
# print(squares)

even = set(range(0, 40, 2))
print(even)
print(len(even))

square_tuple = (4, 6, 9, 16, 25)
squares = set(square_tuple)
print(squares)
print(len(squares))

# UNION COMMAND

print(even.union(squares))
print(len(even.union(squares)))

print(squares.union(even))

print("-" * 40)
# PRINT WHERE THEY ARE THE SAME
print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)

# SUBTRACTION, SUBTRACT ITEMS IN SET B FROM SET A

even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(squares.difference(even))
print(squares - even)

# DIFFERENCE_UPDATE MODIFIES THE SET THAT IT IS CALLED FROM

print("=" * 40)
print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))

# SYMMETRIC_DIFFERENCE DIFFERENCE BETWEEN TWO SETS

print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))
# SAME RESULTS, IT IS OPPOSITE OF INTERSECTION
print("symmetric squares minus even")
print(sorted(squares.symmetric_difference(even)))

squares.discard(4)
squares.remove(16)
squares.discard(8) # no error, does nothing because 8 is not in the set
print(squares)
try:
    squares.remove(8)
except KeyError:
    print("The item 8 is not a member of the set")

# remove raises an error, discard doesn't - that's the difference
squares.remove(8) # now we should get an error

if 8 in squares:
    squares.remove(8)

# YOU CAN CREATE A LIST FROM A SET
# SETS AND SUPER SETS

if squares.issubset(even):
    print("squares is a subet of even")

if even.issuperset(squares):
    print("even is a superset of squares")

# SETS ARE NOT USED TOO OFTEN, BUT USED FOR CASES LIKE THESE
# FROZEN SET IS AN IMMUTABLE SET, WE CAN USE A FROZEN SET AS A DICTIONARY KEY
# REMEMBER NO ADD OR DISCARD METHOD, ONCE CREATED CAN'T BE CHANGED

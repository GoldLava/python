fruit = {"orange": "a sweet orange citrus fruit",
           "apple": "good for making cider",
           "lemon": "a sour, yellow citrus fruit",
           "grape": "a small sweet growing fruit",
           "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmm, lovely",
       "spinach": "can I have some more fruit, please"}

print(veg)

veg.update(fruit)
print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
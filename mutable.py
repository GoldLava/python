shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(another_list)

a = b = c = d = e = f = another_list


print(id(e))

print("Adding cream")
b.append("cream")
print(c)
print(d)
print(a)
print(id(d))

def multiply():
    result = 5 * 5
    return result

answer = multiply()
print(answer v)
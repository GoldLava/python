def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# make our function behave like print
def center_text(*args, sep=''):
    text = " "
    for arg in args:
        text += str(arg) + " " + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# with open("centered", mode='w') as centered_file:

    # call the function here

with open("menu", "w") as menu:
    print(center_text("spam and eggs"), file=menu)
    print(center_text("spam, spam and eggs"), file=menu)
    print(center_text(12), file=menu)
    print(center_text("spam, spam, spam and spam"), file=menu)
    print(center_text("first", "second", 3, 4, "spam"), file=menu)

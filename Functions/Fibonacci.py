def multiply(x: float, y: float) -> float:
    """
    multiply two vars together
    :param x:
    :param y:
    :return:
    """
    result = x * y
    return result


# function annotation and type ints
def is_palindrome(string: str) -> bool:
    """
    reverse a string and compare to original string input, palindrome check
    :param string:
    :return:
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)

# 0, 1, 1, 2, 3, 5, 8,

# def fibonacci(n):
#     if 0 <= n <= 1:
#         return n
#
#     n_minus1, n_minus2 = 0, 1
#
#     result = None
#     for f in range(n - 1):
#         result = n_minus2 + n_minus1
#         n_minus2 = n_minus1
#         n_minus1 = result
#
#     return result
#
#
# for i in range(36):
#     print(i, fibonacci(i))
# #
# #

# def fibonacci(n):
#     if 0 <= n <= 1:
#         return n
#     n_minus1, n_minus2 = 0, 1
#     for f in range(n - 1):
#         result = n_minus2 + n_minus1
#         n_minus2 = n_minus1
#         n_minus1 = result
#
#     return result
#
#
# for x in range(36):
#     print(x, fibonacci(x))


# def fizz_buzz(number: int) -> str:
#     """
#     Play fizz buzz
#     :param number:
#     :return:
#     """
#     if number % 15 == 0:
#         return "fizz buzz"
#     if number % 3 == 0:
#         return "fizz"
#     if number % 5 == 0:
#         return "buzz"
#     else:
#         return str(number)
#
#
# input("Let's play Fizz Buzz. Press ENTER to start!")
# print()
#
# next_number = 0
# while next_number < 99:
#     next_number += 1
#     print(fizz_buzz(next_number))
#     next_number += 1
#     correct_number = fizz_buzz(next_number)
#     players_number = input("Your go: ")
#     if players_number != correct_number:
#         print("Sorry, you lose. The correct answer is: {}".format(correct_number))
#         break


# def fizzbuzz(x: int) -> str:
#     """
#     Play the fizzbuzz game
#     :param x:
#     :return:
#     """
#     if x % 15 == 0:
#         return "fizzbuzz"
#     if x % 3 == 0:
#         return "fizz"
#     if x % 5 == 0:
#         return "buzz"
#     else:
#         return str(x)


# for x in range(1,101):
#     print(x, fizzbuzz(x))


# input("Let's play FizzBuzz! Press ENTER to START.")
# print()
#
# next_number = 0
# while next_number < 99:
#     next_number += 1
#     print(fizzbuzz(next_number))
#     next_number += 1
#     correct_number = fizzbuzz(next_number)
#     players_number = input("Your turn: ")
#     if players_number != correct_number:
#         print("Sorry, you lose. The correct answer is {}.".format(correct_number))
#         break
# else:
#     print("Well done, you reached {}".format(next_number()))

# def fizz_buzz(number: int) -> str:
#     """
#     Let's play fizz_buzz the game
#     :param number:
#     :return:
#     """
#
#     if number % 15 == 0:
#         return "fizzbuzz"
#     if number % 3 == 0:
#         return "fizz"
#     if number % 5 == 0:
#         return "buzz"
#     else:
#         return str(number)
#
#
# input("Let's play a game of FizzBuzz. Press ENTER to START.")
# print()
#
# next_number = 0
# while next_number < 99:
#     next_number += 1
#     print(fizz_buzz(next_number))
#     next_number += 1
#     correct_number = fizz_buzz(next_number)
#     players_number = input("Your turn: ")
#     if players_number != correct_number:
#         print("Sorry, you lose. The correct answer is: {}".format(correct_number))
#         break
# else:
#     print("Congratulations. You win")


# def fizz_buzz(number: int) -> str:
#     """
#         Let's play fizzbuzz game.
#     """
#     if number % 15 == 0:
#         return "fizzbuzz"
#     if number % 3 == 0:
#         return "fizz"
#     if number % 5 == 0:
#         return "buzz"
#     else:
#         return str(number)
#
#
# input("Let's play fizzbuzz. Press ENTER to START.")
# print()
#
#
# next_number = 0
# while next_number < 99:
#     next_number += 1
#     print(fizz_buzz(next_number))
#     next_number += 1
#     correct_number = fizz_buzz(next_number)
#     players_number = input("Your turn: ")
#     if players_number != correct_number:
#         print("Sorry, you lose. The correct answer is: {}".format(correct_number))
#         break
# else:
#     print("Congratulations. You win"

# def factorial(number: int) -> int:
#     """
#     Return n! (0! is 1).
#     :param number:
#     :return:
#     """
#     if number <= 1:
#         return 1
#
#     result = 2
#     for x in range(3, number + 1):
#         result *= x
#
#     return result
#
#
# for i in range(36):
#     print(i, factorial(i))
#
# def factorial(number: int) -> int:
#     if number <= 1:
#         return 1
#     result = 2
#     for x in range(3, number + 1):
#         result *= x
#     return result
#
#
# for x in range(36):
#     print(x, factorial(x))


def factorial(n: int) -> int:
    """Return n! (0! is 1)."""
    if n <= 1:
        return 1

    result = 2
    for x in range(3, n + 1):
        result *= x

    return result


for i in range(36):
    print(i, factorial(i))


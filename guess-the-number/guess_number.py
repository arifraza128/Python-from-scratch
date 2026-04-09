import random
number = random.randint(1,20)

guess = 0

print("Guess a number btw 1 and 20")

while guess != number:
  guess=int(input("Enter your Guess: "))

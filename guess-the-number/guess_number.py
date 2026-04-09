import random
number = random.randint(1,20)

guess = 0

print("Guess a number btw 1 and 20")

while guess != number:
  guess=int(input("Enter your Guess: "))
  if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right ")

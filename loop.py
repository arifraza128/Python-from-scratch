#module
#module
import math

math.factorial(10)

# keyword

import keyword
print(keyword.kwlist)

# random

import random
print(random.randint(1, 10))

# datetime

import datetime
print(datetime.datetime.now())

help('modules')

# loops in python

#while loop

num = int(input("Enter a number: "))
i=1
while i<10:
    print(num*i)
    print(num ,'*' ,i ,'=' ,num*i)
    i+=1

 # while loop with else
x = 1
while x < 3:
  print(x)
  x += 1
else:
  print('limit crossed')
        
#guess number 
import random

jackpot = random.randint(1, 100)
counter = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    counter += 1

    if guess < jackpot:
        print("Too low!")
    elif guess > jackpot:
        print("Too high!")
    else:
        print("Correct ")
        print("You took", counter, "attempts")
        break


# Check even or odd 
for i in range(1, 6):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

# Print numbers and check positive / negative
numbers = [-2, -1, 0, 1, 2]

for num in numbers:
    if num > 0:
        print(num, "is Positive")
    else:
        print(num, "is Negative or Zero")

# Password check (using while loop)
password = "admin"

while True:
    user = input("Enter password: ")
    if user == password:
        print("Login Successful")
        break
    else:
       

#Find largest number from list
numbers = [10, 45, 23, 89, 12]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)

# Voting eligibility check
ages = [16, 18, 20, 15]

for age in ages:
    if age >= 18:
        print(age, "- Eligible to vote")
    else:
        print(age, "- Not eligible to vote")



text = "DevOps Engineer"

freq = {}

for index, char in enumerate(text):
    if char.isalpha():          # ignore spaces and symbols
        char = char.lower()     # case-insensitive
        freq[char] = freq.get(char, 0) + 1

print(freq)

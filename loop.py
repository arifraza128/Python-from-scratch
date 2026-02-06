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
        

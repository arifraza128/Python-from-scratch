age = 18

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# find the sum of a 3 digit number entered by the user
number= int(input('Enter a 3 digit number'))
#345%10-->5
a = number%10

number = number//10
#34%10 --> 4
b = number%10

number = number//10
#3%10 --> 3
c = number%10

print(a+b+c)


#if-else
email= input('enter email')
password= input('enter password')
if 'email==arifraza@gmail.com' and password=='1234':
  print('correct password')
elif 'email==arifraza@gmail.com' and password!='1234':
  print('incorrect password')
  password= input('enter password again')
  if password=='1234':
    print('correct password')
  else:
    print('incorrect password')
else:
  print('incorrect')


# min of  3 number
a = int(input('first num'))
b = int(input('second num'))
c = int(input('third num'))
if a<b and a<c:
  print('smallest is',a)
elif b<c:
  print('smallest is',b)
else:
  print('smallest is',c)
    


# Menu driven program

menu = input("""
Hi! How can I help you?
1. Enter 1 for PIN change
2. Enter 2 for Balance
3. Enter 3 for Withdrawal
4. Enter 4 for Exit
Enter your choice: 
""")

if menu == '1':
    print("PIN change")

elif menu == '2':
    print("Balance")

elif menu == '3':
    print("Withdrawal")

elif menu == '4':
    print("Exit")

else:
    print("Invalid choice")
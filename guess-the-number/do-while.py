num = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    print("You entered:", num)
    
    if num == 0:
        break



#condition

num = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    print("You entered:", num)
    
    if num == 0:
        break

#equivalent

while True:
    print("This runs at least once")
    
    condition = input("Enter 'q' to quit: ")
    
    if condition == 'q':
        break

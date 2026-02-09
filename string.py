name = "Arif"
print(name)

name = input("Enter your name: ")
print("Hello", name)


first = "Hello"
second = "World"
result = first + " " + second
print(result)


first = "Hello"
second = "World"
result = first + " " + second
print(result)

text = "Python"
print(len(text))


word = "Python"
print(word[0])   
print(word[-1])  

text = "Python programming"
print("Python" in text)   
print("Java" in text)     

name = "Arif"
for ch in name:
    print(ch)


s = input("Enter string: ")

clean = s.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


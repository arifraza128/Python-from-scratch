print("today i am starting python from scratch")

print("true")



name= 'arif'
print(name)

a=5
b=6
print(a+b)

# dynamic binding
a=5
print(a)
a='arif'
print(a)

a,b,c=1,2,3
print(a,b,c)
#same value
a=b=c=5
print(a,b,c)
#keywords
print(print)
#get confused

#identifier
#cannot start with digit
first_name='arif'
print(first_name)
#cannot use special symbol
#identifiers cannot be keywords

#input 
input("name:")
#add two number by giving  output
fnum = int(input('enter first number:'))
snum = int(input('enter second number:'))  
sum = fnum + snum
print("sum",sum)

#literals
a = 0b1010 #binary
b = 100 #decimal 
c = 0o310 #octa
d = 0x12c #hexa

print(a,b,c,d)

#float
float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e-3

print(float_1, float_2, float_3)

#complex

x= 3.14j
print(x,x.imag,x.real)

#string
string = "this is python"
print(string)


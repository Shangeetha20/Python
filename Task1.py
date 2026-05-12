#Question 1
'''
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
print("Addition: ", a+b)

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
print("Subraction: ", a-b)


a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
print("Multiplication: ", a*b)


a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
print("Division: ", a/b)


a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
print("Modulus: ", a%b)


a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
print("Floor Division: ", a//b)


a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
print("Exponent: ", a**b)


#Question 2
#Area & Perimeter of Rectangle
leng = int(input("Enter the length: "))
widh = int(input("Enter the width: "))
print ("Area of Rectangle: ", leng*widh)
print ("Perimeter of Rectangle: ",2*(leng)+2*(widh))
            
#Area & Perimeter of Square
leng = int(input("Enter the length: "))
print ("Area of Square: ", leng**2)
print ("Perimeter of Square: ", leng*4)

#Area & Perimeter of Circle
rad = int(input("Enter the length: "))
phi = 3.14
print ("Area of Circle: ", phi*(rad**2))
print ("Perimeter of Circle: ",2*phi*rad)

#Question 3 - Avergae of three nos
a = int (input("Enter a: "))
b = int (input("Enter b: "))
c = int (input("Enter c: "))
avg = (a+b+c)/3
print ("Average:", avg)

#Question 4
#Two numbers are equal
a = int (input("Enter a: "))
b = int (input("Enter b: "))
print ("Equal:", a==b)

#Greater than
a = int (input("Enter a: "))
b = int (input("Enter b: "))
print ("Greater than:", a>b)

#Less than or equal to
a = int (input("Enter a: "))
b = int (input("Enter b: "))
print ("Less than or equal:", a<=b)

#Question 5 - Square root
a = int (input("Enter a: "))
sqrt = a**(1/2)
print ("Square Root:", sqrt)

#Question 6
#Simple Interest
P = int (input("Enter Principle: "))
R = int (input("Enter Rate of Interest: "))
t = int (input("Enter Time: "))
SI = P*R*t
print("Simple Interest: ",SI)
'''
#Coumpond Interest
P = int (input("Enter Principle: "))
r = int (input("Enter Rate of Interest: "))
n = int (input("Enter Net: "))
t = int (input("Enter Time: "))
CI = P*(1+(r/n))**(n*t)
print("Compound Interest: ",CI)


'''
#Question 7

x = int(input("Enter x: "))
x+=5
print(x)
x-=3
print(x)
x*=2
print(x)
x/=4
print(x)
x%=2
print(x)
x**3
print(x)

#Question 8 - Swapping of 2 nos
a = int (input("Enter a: "))
b = int (input("Enter b: "))
a=a+b
b=a-b
a=a-b
#c=a
#a=b
#b=c
print("Swapping of nos: ", a,b)
'''
#Question 9 -Password check
a = input("Enter Username: ")
b = input("Enter Password: ")

print("Username: ", a == "Shan" or b == "Sar20") 

'''
#Question 10 - Cube root
a = int (input("Enter a: "))
cbrt = a**(1/3)
print ("Cube Root:", cbrt)'''


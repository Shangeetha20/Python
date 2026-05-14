'''
#Question 1 - Print 1-10
for i in range(1,11):
    print(i)

#Question 2
for i in range(10,0,-1):
    print(i)
    
#Question 3 - Print 1-10 and square 
for i in range(1,11):
    print(i*i) #print(i**2)

#Question 4 - Multiplication Table
n=int(input("Enter a number: "))
for i in range(1,11):
    print(n,"X",i,"=",n*i)

#Question 5 - Print even nos between 1-50
for i in range(1,50):
    if i%2==0:
        print(i)

#Question  - Print even nos between 2-20
for i in range(2,20):
    if i%2==0:
        print(i)

#Question 6 - Factorial of a number
n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

#Question 7 - Pattern Print
for i in range(1,5):
    for j in range(i):
      print("*",end="")
    print("")

#Question 8 - Palindrome
n=int(input("Enter: "))
s=str(n)
r=""
for i in s:
    r=i+r
if r==s:
    print("Palindrome")
else:
    print("Not a Palindrome")

#Question 9 - Sum of Number
a=[4,6,8,24,10]
total=0
for i in a:
    total =total+i
    print(total)
print(total)
'''
#Question 10 -Largest & Small Number
#Largest
a=[4,6,8,24,10]
l=a[0]
for i in a:
    if i>l:
        l=i
print(l)
#Smallest
a=[14,0,28,7,20]
s=a[0]
for i in a:
    if i<s:
        s=i
print(s)

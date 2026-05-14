#Question 1 - Even or Odd
a= int(input("Enter a number: "))
if a%2==0:
    print("Even")
else:
    print("Odd")

#Question 2 - Check if number is positive or negative
n=int(input("Enter a number: "))
if n>0:
    print("Positive Number")
elif n<0:
    print("Negative Number")
else:
    print("Zero")
    
#Question 3 - Check if divisible by 2 nos
a= int(input("Enter a number: "))
if a%2==0 and a%5==0: #if a%==0 and a%3==0:
    print("Divisible")
else:
    print("Not Divisible")

#Question 4 - Check if its multiple of 5
a= int(input("Enter a number: "))
if a%5==0:
    print("Multiple of 5")
else:
    print("Not a multiple of 5")

#Question 5 - Leap Year
year= int(input("Enter year: "))
if year%4==0:
    print("Leap Year")
else: print("Not a Leap Year")

#Question 6 - Students Mark & Grade
mark=int(input("Enter the mark: "))
if mark>=90 and mark<=100:
    print("Grade A")
elif mark>=75 and mark<90:
    print("Grade B")
elif mark>60 and mark<75:
    print("Grade C")
elif mark>=40 and mark<=60:
    print("Grade D")
else:
    print("Fail")

#Question 7 - Entry Check
age=int(input("Enter age: "))
ticket=str(input("Whether ticket present or not : "))
if age>18:
    if ticket=="Yes":
        print("Have a Ticket")
    else:
        print("Need a Ticket")
else:
    print("Not Eligible")

#Question 8 - System Login Check
username=str(input("Enter the username: "))
if username=="Shan":
    password=input("Enter password: ")
    if password=="Star20":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

#Question 9 - Vowel or Consonant
cha=str(input("Enter a character: "))
if (cha=='a'or cha=='e'or cha=='i' or cha=='o' or cha=='u'):
    print("Vowel")
else:
    print("Consonants")

#Question 10 - Max and Min of 3 nos
#Maximum
a= int(input("Enter a number: "))  
b= int(input("Enter a number: "))
c= int(input("Enter a number: "))
if a>=b and a>=c:
    max=a
elif b>=a and b>=c:
    max=b
else:
    max=c
    print("Maximum number: ",max)
#Minimum
a= int(input("Enter a number: "))  
b= int(input("Enter a number: "))
c= int(input("Enter a number: "))
if a<=b and a<=c:
    min=a
elif b<=a and b<=c:
    min=b
else:
    min=c
    print("Minimum number: ",min)

#Question 11 - Age Category
age=int(input("Enter the mark: "))
if age>=0 and age<=12:
    print("Child")
elif age>=13 and age<=19:
    print("Teen")
elif age>=20 and age<60:
    print("Adult")
else:
    print("Senior Citizen")

#Question 12 - Basic Calculator
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
operator= input("Enter the operator: ")
if operator =="+":
    print(f"Addition {a}+{b}:", a+b) 
elif operator =="-":
    print(f"Subraction {a}-{b}:", a-b) 
elif operator =="*":
    print(f"Multiplication {a}*{b}:", a*b) 
elif operator =="/":
    if b==0:
        print("Not Divisible")
    else:
        print(f"Division {a}/{b}:", a/b)

#Question 13
n= int(input("Enter a number: "))
if n**3>100:
    print(f"Greater than 100")
elif n**3==100:
    print(f"Equals 100")
else:
    print("Less than 100")

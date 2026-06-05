'''
#Question 1
for i in range(1,101):
    print(i)

#Question 2 - Skip if divisible by 3
for i in range(50):
    if i%3==0:
        continue
    print(i)

#Question 3 - Break if divisible by 9
for i in range(1,50):
    if i%9==0:
        break
    print(i)

#Question 4
n=int(input("Enter a number: "))
a=n
while a<1:
    print(a)
a+=1

#Question 5
for i in range(10):
    if i==5:
        pass
    print(i)

#Question 6

#Question 7
a="PYTHON"
for i in a:
    if i=="H":
        continue
    print(i)

'''

#Question 8
i=20
while i>0:
    if i==17:
        i-=1
        continue
    if i==13:
        i-=1
        break
    print(i)
    i-=1

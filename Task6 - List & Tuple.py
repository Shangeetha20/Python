'''
#List Task with Method
#Question 1
lst=[4,20,7,28,24,17,10,23,30,11]
print("Type:",type(lst))
lst.append(9)
print("Append:",lst)

lst.insert(3,3)
print("Insert:",lst)

lst.remove(4)
print("Remove:",lst)

lst.pop(9)
print("Pop:",lst)

lst=[4,20,7,28,24,17,10,23,30,11]
lst.extend([2,4,5])
print("Extend:",lst)

#Question 2
c=[20,11,7,3,4,28,24,17,10,23,30,9,2,4,6,11]
print("Count:",c.count(10))

#Question 3
a=[20,11,7,3,4,28,24,17,10,23,30,9,2,4,6,11]
print("Index Position:",a.index(20))

#Question 4
b=[1,2,3,4,5,6,7,8,9]
b.reverse()
print("Reverse Order:",b)

#Question 5
lst=[4,20,11,7,28,24,17,10,23,30,11]
lst.sort()
print("Ascending Order:",lst)
lst.sort[::-1] ---------------------------------
print("Descending Order:",lst)

#Question 6
lst=[4,20,7,28,24,17,10,23,30,11]
lst.clear()
print("Clear:",lst)

#Question 7
lst=[4,20,7,28,24,17,10,23,30,11]
a=lst.copy()
print("Copy:",a)

#Tuple Task with Method
#Question 8
t=(20,11,7,3,4,28,24,17,10,23,30)
print("Type:",type(t))
print("Length:",len(t))
print("Maximum:",max(t))
print("Minimum:",min(t))

#Question 9
c=(20,11,7,3,4,28,24,17,10,23,30,9,2,4,6,11)
print("Count:",c.count(11))

#Question 10
a=(20,11,7,3,4,28,24,17,10,23,30,9,2,4,6,11)
print("Index Position:",a.index(28))

#Question 11
t=(20,11,7,3,4,28,24)
l=list(t)
print(t)
l.extend([17,10,23,30,9])
print(l)
t=tuple(l)
print(t)

#Question 12
a=(20,11,7,3,4,28,24)
b=(17,10,23,30,9)
print("Concadenate:",a+b)

#Question 13
t=(20,11,7,3,4,28,24,17,10,23)
l=list(t)

#Question 14
n=(20,11,7,3,4,28,24,17,10,23)
x=int(input("Enter a number:"))
if (x in n):
    print("Exist")
else:
    print("Not Exist")

n = int(input("Enter size of list"))
numbers = list(map(int, input("Enter numbers: ").split()))
print(type(numbers))
highest = max(numbers)
print(highest)
highest.remove()
#highest = max(numbers)
print(highest)

arr=[20,11,7,3,4,28,24,17,10,23]
arr.sort()
highest = max(arr)
arr.pop
print(arr)
print(highest) 


    
N = int(input())
list=[N]
list.insert(0,5)
list.insert(1,10)
list.insert(0,6)
print(list)
list.remove(6)
list.append(9)
list.append(1)
list.sort
print(list)
list.pop
list.reverse()
print(list)

def swap_case(s):
    return swap_case(s)

if __name__ == '__main__':
    s = str(input())
    result = swap_case(s)
    print(result)

s = input()
if s.isalnum():
    print ("True")
elif s.isalpha():
    print("True")
elif s.isdigit():
    print("True")
elif s.islower():
    print("True")
elif s.isupper():
    print("True")
else:
    print("False")
'''
def split_and_join(line):
    #line=line.split(" ")
    #line="-".join(line)
    #print(line)
    result=result.split(" ")
    result="-".join(result)

#split_and_join()
  
#if __name__ == '__main__':
line = input()
result = split_and_join(line)
print(result)

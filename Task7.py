#Question 1 - Student Result System
''''
total = 0
r=int(input("Enter total subjects:"))
for i in range(r):
    m=int(input("Enter the mark:"))
    total += m
print("Total Marks:",total)
avg = total / r
print("Average:",avg)
if avg >= 90:
    print("Grade A")
elif avg > 75 and avg < 90:
    print("Grade B")
elif avg >= 50 and avg <=75:
    print("Grade C")
elif avg < 50:
    print("FAIL")

#Question 2 - ATM Deposit Tracker
bal = 5000
temp = 0
r=int(input("How many times do you want to deposit?" ))
for i in range(r):
    a=int(input("Enter the Amount:"))
    temp += a
    if temp>=100000:
        print("Limit Exceeded for the day.")
        break
print("Total Balance:",bal+temp)

#Question 3 - ATM Simulation
bal = 0
while True:
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Balance")
    print("4.EXIT")
    choice=int(input("Select your choice:"))
    if choice==1:
        dep=int(input("Enter deposit amount:"))
        bal+=dep
        print("Total Balance:",bal)
    elif choice ==2:
        witd=int(input("Enter withdraw amount:"))
        bal-=witd 
        print(f"Withdraw amount is {witd} and Balance Amount is {bal}")
    elif choice ==3:
        print("Total Balance:",bal)
    elif choice ==4:
        print("EXIT")
        break
'''
#Question 4 - Login Security System
attempt = 0
while attempt < 3:
    username=input("Enter your username:")
    password=input("Enter your password:")
    if username == "Shangeetha" and password == "Star@20":
        print ("Login Successful.")
        break
    else:
        print("Enter Valid Credentials")
        attempt=attempt+1
print("Login Attempts Exceeded")

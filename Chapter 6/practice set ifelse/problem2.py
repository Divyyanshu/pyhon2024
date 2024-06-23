#1. Write a program to find the greatest of four numbers entered by the user.

a1 = int(input("ente your number 1 :"))
a2 = int(input("ente your number 2 :"))
a3 = int(input("ente your number 3 :"))
a4 = int(input("ente your number 4 :"))

if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is greater")
elif(a2>a1 and a2>a3 and a2>a4):
    print("a2 is greater")
elif(a3>a2 and a3>a1 and a3>a4):
    print("a3 is greater")
else:
    print("a4 is greater")
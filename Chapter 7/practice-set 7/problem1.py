'''Write a program to print multiplication table of a given number using for loop'''
n = int(input("enter your number : "))

for i in range(1,11):
    print(f"{n} x {i} = {n * i}")


# using while loop also
n = int(input("enter your number : "))

i = 1
while(i<11):
    print(f"{n} x {i} = {n*i}")
    i = i +1
#Create an empty dictionary. Allow 4 friends to enter their favorite language as
#value and use key as their names. Assume that the names are unique.
#7. If the names of 2 friends are same; what will happen to the program in problem 6?
#8. If languages of two friends are same; what will happen to the program in problem 6?


d = {}

name = input("enter your name : ")
lang = input("enter your name : ")
d.update({name : lang})
name = input("enter your name : ")
lang = input("enter your name : ")
d.update({name : lang})
name = input("enter your name : ")
lang = input("enter your name : ")
d.update({name : lang})
name = input("enter your name : ")
lang = input("enter your name : ")
d.update({name : lang})
name = input("enter your name : ")
lang = input("enter your name : ")
d.update({name : lang})
name = input("enter your name : ")
lang = input("enter your name : ")
d.update({name : lang})

print(d)
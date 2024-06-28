class employ :
    name = "divyanshu"
    postion = "software engineer"  #class attribute
    salary = 60000

    def getinfo(self):
       print(f"laungugae is {self.postion} and salary is {self.salary}")
    def greet(self):
        print("good moring bhai log")

d = employ()
d.name = "ram"

d.getinfo()
d.greet()
print(d.name ,d.postion, d.salary)

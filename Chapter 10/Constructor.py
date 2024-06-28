class room:
    # name = "divyanshu"
    # lang = "python"
    company = 'Microsoft'
    def __init__(self , name , lang , salary):
        self.name = name
        self.lang = lang
        self.salary = salary
        # print("hello data is clean")

dt = room("ram" , "java" , 50000)
print(dt.name , dt.lang , dt.salary ,dt.company)
        
kt = room("kalmesh" , "javascript" , 40000)
print(kt.name , kt.lang , kt.salary , kt.company)
        
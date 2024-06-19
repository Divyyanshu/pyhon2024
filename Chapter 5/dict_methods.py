marks = {
    "divyanshu" : 82,
    "ram" : 65,
    "dk": 81,
    "mayank" : True,
    205 : "Room numbeer"
}

# key () items() values() update() get()
print(marks.keys())
print(marks.items())       #give error if value or key is not valid
print(marks.values())
marks.update({"dk" : 82, "dt" :81})
print(marks)

print(marks.get("dk"))  #print none if value or key is not valid
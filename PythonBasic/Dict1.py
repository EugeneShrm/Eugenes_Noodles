#dictionary
dict = {"name": "John", "age": 30, "City": "Tokyo"}
print(dict)
print(dict["City"])
print()
#how add elements
dict["gender"] = "male"
print(dict)
print()
# edit
dict["gender"] = "FEMALE"
print(dict)
del dict["gender"]
print(dict)
for x in dict:
    print(x)
print()
#to check values
for y in dict:
    print(dict[y])
print()
#or
for y in dict.values():
    print(y)
# to show key and value
print()
for x,y in dict.items():
    print(x,y)
print()   
# to copy dict
newDict = dict.copy()
print(newDict)

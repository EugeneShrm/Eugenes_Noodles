#List
name1 = "Anna"
name2 = "Eugene"
name3 = "Tokyo"
print(name1, name2, name3)

#abo use List to make it shorter
names = ["Anna", "Eugene", "Tokyo"]
print(names)

# what can we do with List?
print(names[0])

names[0] = "Annastasiia"
print(names[0])

print(len(names)) # len == amount of points

print(type(names))

#adding elements
names = ["Anna", 40, "Tokyo", True]
names.append(123)
print(names)

names = ["Anna", 40, "Tokyo", True]
names.insert(1, "Boooooob")
print(names)

names = ["Anna", 40, "Tokyo", True]
names2 = ["Archi", "Larysa"]
names.extend(names2)
print(names)

#delete options
names = ["Anna", 40, "Tokyo", True]
names.remove(True)
print(names)

names = ["Anna", 40, "Tokyo", True]
names.pop(2) #remove elements number
print(names)

names = ["Anna", 40, "Tokyo", True]
del names #remove the whole list
# print(names)

# how to render elements on the screen
names = ["Anna", 40, "Tokyo", True]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# or
names = ["Anna", 40, "Tokyo", True]
for a in names:
    print(a)


